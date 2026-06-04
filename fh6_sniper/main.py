"""Entry point: wires config, templates, sniper, overlay, and hotkeys."""
from __future__ import annotations
import json
import logging
import sys
import threading
from dataclasses import asdict
from pynput import keyboard
from . import capture, notifier, paths, vision
from .config import load_config, save_config
from .i18n import normalize_language, translate
from .overlay import Overlay
from .sniper import GameIO, Sniper


def _log_config(cfg) -> None:
    """Dump the loaded config to the log as a single JSON line.
    Helps when triaging user-submitted logs - we can see what the bot
    was configured with at session start."""
    body = asdict(cfg)
    declared = set(cfg.__dataclass_fields__)
    for key, value in cfg.__dict__.items():           # include extras
        if key not in declared:
            body[key] = value
    body = {k: list(v) if isinstance(v, tuple) else v for k, v in body.items()}
    logging.getLogger("fh6").info("config snapshot: %s",
                                   json.dumps(body, sort_keys=True))


def _setup_logging():
    log_path = paths.app_dir() / "logs" / "sniper.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter(
        "%(asctime)s.%(msecs)03d %(levelname)s %(message)s", "%H:%M:%S")
    file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    file_handler.setFormatter(fmt)
    root = logging.getLogger("fh6")
    root.setLevel(logging.INFO)
    root.handlers.clear()
    root.addHandler(file_handler)
    if sys.stderr is not None:          # no console under --windowed exe
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        root.addHandler(console)
    return log_path


def main() -> None:
    log_path = _setup_logging()
    logging.getLogger("fh6").info("FH6 Sniper starting (log: %s)", log_path)
    cfg = load_config(paths.app_dir() / "config.json")
    _log_config(cfg)
    tr = lambda key, **kwargs: translate(cfg.language, key, **kwargs)
    template_dir = cfg.effective_template_dir()
    try:
        templates = vision.load_templates(
            paths.app_dir() / template_dir,
            moving_background=cfg.moving_background)
    except FileNotFoundError as exc:
        logging.getLogger("fh6").exception(
            "template load failed for language=%s dir=%s",
            cfg.language, template_dir)
        raise FileNotFoundError(
            f"{exc}. For zh-CN, capture the missing template listed in "
            "docs/template-capture-zh-CN.md."
        ) from exc
    io = GameIO(cfg, templates)
    overlay = Overlay(
        hide_from_capture=not getattr(cfg, "overlay_capturable", False),
        language=cfg.language)

    state = {
        "sniper": None,
        "thread": None,
        # display-side running totals - accumulate across stop/start cycles
        # so the overlay's BOUGHT / SEARCHES / FAILS don't reset every run.
        "display": {"searches": 0, "bought": 0, "fails": 0},
        # last raw values seen from the current Sniper - used to compute
        # deltas (new Sniper instances start their internal counters at 0).
        "last_bot_stats": (0, 0, 0),
    }
    purchase_log = paths.app_dir() / cfg.log_path

    def on_purchase(loop_seconds, total):
        notifier.log_purchase(purchase_log, "bought", loop_seconds, total)
        notifier.notify_success(total, cfg.notify_sound, cfg.notify_toast,
                                cfg.language)

    def on_stats(searches, bought, fails):
        last_s, last_b, last_f = state["last_bot_stats"]
        d = state["display"]
        d["searches"] += max(0, searches - last_s)
        d["bought"]   += max(0, bought   - last_b)
        d["fails"]    += max(0, fails    - last_f)
        state["last_bot_stats"] = (searches, bought, fails)
        overlay.set_stats(d["searches"], d["bought"], d["fails"])

    def start():
        if state["thread"] and state["thread"].is_alive():
            return
        capture.focus_window(cfg.window_title)
        capture.reset_normalize_plan()             # detect crop afresh each run
        state["last_bot_stats"] = (0, 0, 0)        # new Sniper, fresh deltas
        sniper = Sniper(io, cfg, on_purchase=on_purchase,
                        on_status=overlay.set_status,
                        on_stats=on_stats,
                        tr=tr)

        def _run_safe():
            try:
                sniper.run()
            except Exception:
                logging.getLogger("fh6.main").exception(
                    "sniper thread crashed")
                try:
                    overlay.set_status(tr("status.crashed"), "stopped")
                except Exception:
                    pass

        thread = threading.Thread(target=_run_safe, daemon=True)
        state["sniper"], state["thread"] = sniper, thread
        thread.start()

    def stop():
        if state["sniper"]:
            state["sniper"].request_stop()

    def toggle():
        if state["thread"] and state["thread"].is_alive():
            stop()
        else:
            start()

    hotkeys_ref = {"listener": None}

    def _bind_hotkeys(start_stop, panic):
        listener = keyboard.GlobalHotKeys({start_stop: toggle, panic: stop})
        listener.start()
        hotkeys_ref["listener"] = listener

    _bind_hotkeys(cfg.hotkey_start_stop, cfg.hotkey_panic)

    def apply_settings(values):
        """Apply settings dict to cfg in-place; persist; reload as needed."""
        log = logging.getLogger("fh6.settings")
        prev_bg = cfg.moving_background
        prev_language = cfg.language
        prev_start = cfg.hotkey_start_stop
        prev_panic = cfg.hotkey_panic
        prev_capturable = getattr(cfg, "overlay_capturable", False)
        diffs = []
        for key, value in values.items():
            if key == "language":
                value = normalize_language(value)
            old = getattr(cfg, key, None)
            if old != value:
                diffs.append(f"{key} {old!r} -> {value!r}")
            setattr(cfg, key, value)
        if diffs:
            log.info("settings changed: %s", ", ".join(diffs))
        if cfg.overlay_capturable != prev_capturable:
            overlay.set_capturable(cfg.overlay_capturable)
            log.info("overlay capturable -> %s", cfg.overlay_capturable)
        try:
            save_config(cfg, paths.app_dir() / "config.json")
        except Exception as exc:
            log.exception("save_config failed")
            return tr("error.save_config", error=exc)
        language_changed = cfg.language != prev_language
        if cfg.moving_background != prev_bg and not language_changed:
            try:
                io.templates = vision.load_templates(
                    paths.app_dir() / cfg.effective_template_dir(),
                    moving_background=cfg.moving_background)
                log.info("templates reloaded (moving_background=%s)",
                         cfg.moving_background)
            except Exception as exc:
                log.exception("template reload failed")
                return tr("error.template_reload", error=exc)
        if (cfg.hotkey_start_stop != prev_start
                or cfg.hotkey_panic != prev_panic):
            try:
                if hotkeys_ref["listener"] is not None:
                    hotkeys_ref["listener"].stop()
                _bind_hotkeys(cfg.hotkey_start_stop, cfg.hotkey_panic)
                log.info("hotkeys rebound (%s / %s)",
                         cfg.hotkey_start_stop, cfg.hotkey_panic)
            except Exception as exc:
                log.exception("hotkey rebind failed")
                return tr("error.hotkey_rebind", error=exc)
        if language_changed:
            log.info("language changed: restart required")
            return tr("save.saved_restart"), False
        return None

    overlay.bind_settings(cfg)
    overlay.on_save(apply_settings)
    overlay.on_toggle(toggle)
    overlay.set_status(tr("status.idle"), "stopped")
    try:
        overlay.run()
    finally:
        stop()
        listener = hotkeys_ref["listener"]
        if listener is not None:
            listener.stop()


if __name__ == "__main__":
    main()
