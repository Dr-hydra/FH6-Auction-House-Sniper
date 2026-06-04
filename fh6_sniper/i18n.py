"""Small runtime translation table for user-facing UI text."""
from __future__ import annotations

DEFAULT_LANGUAGE = "zh-CN"
SUPPORTED_LANGUAGES = ("en-US", "zh-CN")

TEMPLATE_DIR_BY_LANGUAGE = {
    "en-US": "templates",
    "zh-CN": "templates_zh-CN",
}


_TEXT = {
    "en-US": {
        "app.title": "FH6 Sniper",
        "tab.status": "STATUS",
        "tab.settings": "SETTINGS",
        "button.start": "START",
        "button.stop": "STOP",
        "button.save": "SAVE SETTINGS",
        "footer.hotkeys": "F8  start / stop          F9  panic",
        "stats.bought": "BOUGHT",
        "stats.searches": "SEARCHES",
        "stats.fails": "FAILS",
        "stats.uptime": "UPTIME",
        "settings.group.general": "GENERAL",
        "settings.group.feedback": "FEEDBACK",
        "settings.group.behaviour": "SNIPER BEHAVIOUR",
        "settings.group.auto_stop": "AUTO-STOP",
        "settings.group.hotkeys": "HOTKEYS",
        "settings.language": "Language",
        "settings.collect_after_buyout": "Collect won vehicles automatically",
        "settings.moving_background": "Moving background mode (FH6 video)",
        "settings.notify_sound": "Play success beep sounds",
        "settings.notify_toast": "Windows toast on success",
        "settings.hdr_mode": "HDR mode (widens lime detection)",
        "settings.overlay_capturable": "Show overlay in screenshots & recordings",
        "settings.win32_api_input": "Win32 API input (background key presses)",
        "settings.match_threshold": "Match threshold",
        "settings.loop_pace_s": "Loop pace (seconds)",
        "settings.buyout_select_delay_ms": "Buyout select delay (ms)",
        "settings.max_cars": "Max cars",
        "settings.max_minutes": "Max minutes",
        "settings.hotkey_start_stop": "Start / stop hotkey",
        "settings.hotkey_panic": "Panic stop hotkey",
        "save.saved": "Saved",
        "save.saved_restart": "Saved. Restart the app to apply language/template changes.",
        "save.bad_value": "Bad value for {label}",
        "save.failed": "Save failed: {error}",
        "error.save_config": "Could not save config: {error}",
        "error.template_reload": "Saved, but template reload failed: {error}",
        "error.hotkey_rebind": "Saved, but hotkey rebind failed: {error}",
        "status.idle": "Idle",
        "status.running": "Running",
        "status.paused_focus": "Paused: FH6 not focused",
        "status.auto_toggled_bg": "Auto-toggled moving background -> {value}",
        "status.lost_auction_house": "Lost: start the bot in the Auction House",
        "status.lost_language": "Lost: set game language to English",
        "status.opening_search": "Opening Search Auctions",
        "status.recovering": "Recovering",
        "status.listing_sold": "Listing already sold, skipping",
        "status.collecting": "Collecting car",
        "status.searching": "Searching",
        "status.all_sold": "All listings sold, skipping",
        "status.car_found": "Car found, buying out",
        "status.sold_during_nav": "Listing sold during navigation, skipping",
        "status.auto_stop": "Auto-stop limit reached",
        "status.stopped_recover": "Stopped: could not recover",
        "status.stopped_language": "Stopped: set game language to English",
        "status.bought": "Bought {count} car(s)",
        "status.stopped": "Stopped",
        "status.crashed": "Crashed: see sniper.log",
        "toast.title": "FH6 Sniper",
        "toast.bought": "Car bought ({count} this session)",
    },
    "zh-CN": {
        "app.title": "FH6 狙击器",
        "tab.status": "状态",
        "tab.settings": "设置",
        "button.start": "开始",
        "button.stop": "停止",
        "button.save": "保存设置",
        "footer.hotkeys": "F8  开始 / 停止          F9  紧急停止",
        "stats.bought": "买到",
        "stats.searches": "搜索",
        "stats.fails": "失败",
        "stats.uptime": "运行时间",
        "settings.group.general": "通用",
        "settings.group.feedback": "反馈",
        "settings.group.behaviour": "狙击行为",
        "settings.group.auto_stop": "自动停止",
        "settings.group.hotkeys": "快捷键",
        "settings.language": "语言",
        "settings.collect_after_buyout": "买到车辆后自动领取",
        "settings.moving_background": "动态背景模式（FH6 视频背景）",
        "settings.notify_sound": "成功时播放提示音",
        "settings.notify_toast": "成功时显示 Windows 通知",
        "settings.hdr_mode": "HDR 模式（放宽荧光绿识别）",
        "settings.overlay_capturable": "允许在截图和录制中显示悬浮窗",
        "settings.win32_api_input": "Win32 API 输入（后台按键）",
        "settings.match_threshold": "匹配阈值",
        "settings.loop_pace_s": "循环间隔（秒）",
        "settings.buyout_select_delay_ms": "一口价选择延迟（毫秒）",
        "settings.max_cars": "最多车辆数",
        "settings.max_minutes": "最多运行分钟",
        "settings.hotkey_start_stop": "开始 / 停止快捷键",
        "settings.hotkey_panic": "紧急停止快捷键",
        "save.saved": "已保存",
        "save.saved_restart": "已保存。请重启程序以应用语言/模板切换。",
        "save.bad_value": "{label} 的值无效",
        "save.failed": "保存失败：{error}",
        "error.save_config": "无法保存配置：{error}",
        "error.template_reload": "已保存，但模板重新加载失败：{error}",
        "error.hotkey_rebind": "已保存，但快捷键重新绑定失败：{error}",
        "status.idle": "空闲",
        "status.running": "运行中",
        "status.paused_focus": "已暂停：FH6 未处于前台",
        "status.auto_toggled_bg": "已自动切换动态背景 -> {value}",
        "status.lost_auction_house": "已迷失：请在拍卖行内启动",
        "status.lost_language": "已迷失：请将游戏语言设为中文",
        "status.opening_search": "正在打开搜索拍卖",
        "status.recovering": "正在恢复",
        "status.listing_sold": "车辆已售出，跳过",
        "status.collecting": "正在领取车辆",
        "status.searching": "正在搜索",
        "status.all_sold": "列表均已售出，跳过",
        "status.car_found": "发现车辆，正在一口价买断",
        "status.sold_during_nav": "导航过程中车辆已售出，跳过",
        "status.auto_stop": "已达到自动停止限制",
        "status.stopped_recover": "已停止：无法恢复",
        "status.stopped_language": "已停止：请检查游戏语言和模板",
        "status.bought": "已买到 {count} 辆",
        "status.stopped": "已停止",
        "status.crashed": "已崩溃：请查看 sniper.log",
        "toast.title": "FH6 狙击器",
        "toast.bought": "已买到车辆（本次会话第 {count} 辆）",
    },
}


def normalize_language(language: str | None) -> str:
    """Return a supported language code, defaulting to Simplified Chinese."""
    if language in SUPPORTED_LANGUAGES:
        return language
    return DEFAULT_LANGUAGE


def template_dir_for_language(language: str | None) -> str:
    return TEMPLATE_DIR_BY_LANGUAGE[normalize_language(language)]


def translate(language: str | None, key: str, **kwargs) -> str:
    lang = normalize_language(language)
    text = _TEXT.get(lang, {}).get(key, _TEXT["en-US"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text
