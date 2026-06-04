"""Purchase CSV logging and sound/toast notifications."""
from __future__ import annotations
import csv
import datetime as dt
from pathlib import Path
from .i18n import translate


def log_purchase(log_path, outcome: str, loop_seconds: float,
                 total: int) -> None:
    """Append one row to the purchase CSV. Writes a header if new."""
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(
                ["timestamp", "outcome", "loop_seconds", "total_bought"])
        writer.writerow([
            dt.datetime.now().isoformat(timespec="seconds"),
            outcome, f"{loop_seconds:.1f}", total,
        ])


def notify_success(car_count: int, sound: bool, toast: bool,
                   language: str = "zh-CN") -> None:
    """Beep + Windows toast after a successful buy."""
    if sound:
        try:
            import winsound
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        except Exception:
            pass
    if toast:
        try:
            from win11toast import toast as show_toast
            show_toast(translate(language, "toast.title"),
                       translate(language, "toast.bought", count=car_count))
        except Exception:
            pass
