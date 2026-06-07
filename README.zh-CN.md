# FH6 Auction House Sniper 中文版

> 本仓库是 `FH6 Auction House Sniper` 的独立中文本地化衍生项目，基于原项目 [FrostyIsBored/FH6-Auction-House-Sniper](https://github.com/FrostyIsBored/FH6-Auction-House-Sniper) 修改。当前项目地址为 [Dr-hydra/FH6-Auction-House-Sniper](https://github.com/Dr-hydra/FH6-Auction-House-Sniper)。项目遵循 [GNU GPLv3](LICENSE) 发布，并保留原作者与贡献者的署名和版权。

[English README](README.md)

## 项目简介

FH6 Auction House Sniper 是一个面向 Forza Horizon 6 拍卖行的自动搜索和一口价工具。它会按照你在游戏中设置好的筛选条件循环搜索车辆，在目标出现时尝试立即买断，买到后可自动领取车辆并继续循环。

原 README 提到该工具约有 10% 的买断成功率，通常可在 5 分钟内尝试狙击到一辆车。实际效果会受到电脑性能、网络、游戏服务器响应和菜单动画速度影响。

## 功能

- 自动搜索并尝试一口价买断。
- 跳过已售出的列表，继续寻找可买车辆。
- 买到车辆后可自动领取。
- 左上角常驻悬浮窗显示实时统计。
- `F8` 开始/停止，`F9` 紧急停止。
- 可按车辆数量或运行时间自动停止。
- 识别当前菜单页面，降低误点到其他页面的概率。
- 支持 `en-US` / `zh-CN` 双语界面和识别资源切换。

## 重要风险

> [!WARNING]
> - 拍卖行自动化可能违反 Forza 的 Enforcement Guidelines。
> - 你可能面临警告、封禁、永久封禁或其他账号风险。
> - 本工具没有任何成功率或安全性保证。
> - 请自行承担使用风险。

## 系统要求

- Windows 10 或 Windows 11。
- PC 版 Forza Horizon 6。
- 分辨率 `1920 x 1080`，全屏，帧率不锁定。
- 图形预设建议设为 Very Low。
- UI 缩放设为 `100`。
- 使用键盘菜单导航；工具通过按键操作，不使用鼠标点击。
- 如果游戏以管理员权限启动，工具也需要以管理员权限运行。
- 强烈建议使用有线网络。

## 语言

程序配置项 `language` 同时控制悬浮窗语言和游戏界面识别语言：

| language | 界面语言 | 适用游戏语言 |
|---|---|---|
| `en-US` | 英文 | 英文 |
| `zh-CN` | 简体中文 | 简体中文 |

切换语言后需要重启程序才能生效。请确保 FH6 的游戏语言与 `config.json` 中的 `language` 保持一致。

## 下载

从 Releases 页面下载最新的 `FH6-Sniper.zip`，解压到电脑上的任意目录。

如果你从源码运行，请安装依赖：

```powershell
pip install -r requirements.txt
```

## 使用步骤

### 1. 打开拍卖行

启动 Forza Horizon 6，进入嘉年华站点的拍卖行。

### 2. 配置搜索条件

打开搜索拍卖并设置筛选条件：

- `Make` / `Model`：你要找的车辆品牌和型号。
- `Max Buyout`：最高一口价上限。工具会买断第一个匹配车辆，不会再判断价格，所以必须谨慎设置。

设置完成后退回到搜索配置页面。工具预期从这个页面开始运行。

### 3. 启动工具

双击 `FH6-Sniper.exe`。屏幕左上角会出现一个小悬浮窗。

点击回到 FH6，按 `F8` 或悬浮窗里的开始按钮启动。停止方式：

- 再按一次 `F8`。
- 按 `F9` 紧急停止。
- 点击悬浮窗里的停止按钮。

## SmartScreen 提示

Windows SmartScreen 可能会因为 exe 未签名而提示警告。若你确认要运行：

1. 点击 `More info`。
2. 点击 `Run anyway`。

## 快捷键

| 按键 | 动作 |
|---|---|
| `F8` | 开始 / 停止 |
| `F9` | 紧急停止 |
| 悬浮窗停止按钮 | 等同于 `F8` |
| 悬浮窗关闭按钮 | 关闭并退出 |

## 设置

首次运行会在 exe 同级目录生成 `config.json`。常用配置：

- `language`：界面和游戏识别语言，支持 `zh-CN` 和 `en-US`。
- `max_cars`：买到多少辆后自动停止，默认 `1`。
- `max_minutes`：运行多少分钟后自动停止，默认 `180`。
- `collect_after_buyout`：设为 `false` 后不自动领取车辆。
- `notify_sound` / `notify_toast`：控制成功提示音和 Windows 通知。
- `buyout_select_delay_ms`：选择一口价后再按确认的额外延迟。若工具偶尔打开出价窗口而不是一口价窗口，可尝试设为 `200`。
- `moving_background`：如果游戏里关闭了动态背景，请设为 `false`。
- `overlay_capturable`：是否允许悬浮窗出现在截图和录屏里。通常保持关闭，避免遮挡识别区域。
- `win32_api_input`：使用 Win32 API 后台按键。开启后 FH6 不在前台时也可继续按键，但游戏仍需运行且不能最小化。

## 注意事项

- 工具默认只在 FH6 是前台窗口时运行。切出游戏后悬浮窗会显示暂停。
- 悬浮窗默认不会进入截图/录屏，避免被识别逻辑误匹配。
- 可以按住悬浮窗标题区域拖动位置。
- 你不会赢下每一次狙击。工具和人工一样受菜单动画与拍卖服务器响应限制。
- 如果服务器很慢或过载，工具可能卡住或恢复失败。

## 排错

**悬浮窗显示“已暂停：FH6 未处于前台”**

点击回到游戏窗口。

**按 F8 没反应**

可能有其他程序占用了 `F8`。关闭相关程序，或在 `config.json` 中修改快捷键。

**工具漏识别某个页面并卡住**

重启 FH6 和工具。确认图形预设为 Very Low，分辨率为 `1920 x 1080`，UI 缩放为 `100`。

**一口价确认窗口打开了，但工具不会确认**

通常是游戏的动态背景设置与工具的 `moving_background` 设置不一致。检查 FH6 视频设置里的动态背景，并在悬浮窗设置或 `config.json` 中保持一致。

**启动后提示无法恢复或语言错误**

常见原因：

- 游戏语言与工具语言不一致。
- 悬浮窗被设置为可截图并遮挡了工具识别区域。
- FH6 没有处于前台窗口，或被其他窗口遮挡。

请确认游戏语言与 `config.json` 中的 `language` 一致，并让 FH6 保持在前台。提交问题时请附上 `sniper.log`。

## 许可证和署名

本中文本地化版本遵循 GNU GPLv3。你可以在 GPLv3 条款下复制、分发和修改本项目；分发修改版时应保留许可证、保留原作者署名，并明确说明你做过修改。

原项目作者：FrostyIsBored  
原项目地址：[FrostyIsBored/FH6-Auction-House-Sniper](https://github.com/FrostyIsBored/FH6-Auction-House-Sniper)  
当前独立项目：[Dr-hydra/FH6-Auction-House-Sniper](https://github.com/Dr-hydra/FH6-Auction-House-Sniper)
