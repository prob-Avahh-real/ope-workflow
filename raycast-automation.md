# Raycast 自动化中枢配置

> OPE macOS Workflow · 2026-05-18

---

## 一、为什么 Raycast

你选了 Raycast 组合（Raycast + Shortcuts + Warp），这是对的。分工如下：

| 工具 | 角色 | 擅长 |
|------|------|------|
| **Raycast** | 自动化中枢 | 快捷启动、窗口管理、剪贴板、Snippets、自定义脚本 |
| **Shortcuts** | 系统编排器 | 跨 app 串联、定时触发、文件批处理 |
| **Warp** | 终端 | CLI 工作、Go 编译、git 操作 |

三者不打架——Raycast 管「手快」、Shortcuts 管「自动」、Warp 管「终端」。

---

## 二、安装

```bash
brew install --cask raycast
```

首次启动按指引完成基础设置，**建议把 Spotlight（Cmd+Space）换成 Raycast**——这是最大的生产力跃升。

> 替换方法: 系统设置 → 键盘 → 键盘快捷键 → Spotlight → 取消勾选「显示 Spotlight 搜索」

---

## 三、核心功能配置

### 3.1 剪贴板历史

Raycast 设置 → Extensions → Clipboard History：

- **快捷键**: `Cmd+Shift+V`（或你习惯的）
- **历史保留时间**: 30 天
- **忽略的应用**: 密码管理器（1Password / Bitwarden）

从此复制过的所有东西都能找回，不再「刚复制就被覆盖」。

### 3.2 窗口管理

Raycast 自带窗口管理，不需要额外装 Rectangle/Magnet：

常用命令（在 Raycast 输入框中搜）：
- `Left Half` — 窗口占左半屏
- `Right Half` — 窗口占右半屏
- `Maximize` — 全屏
- `Top Half` / `Bottom Half` — 上下分屏
- `First Third` / `Center Third` / `Last Third` — 三栏布局

**建议设置快捷键**（Raycast → Extensions → Window Management）：

| 操作 | 建议快捷键 |
|------|------------|
| 左半屏 | `Cmd+Opt+←` |
| 右半屏 | `Cmd+Opt+→` |
| 全屏 | `Cmd+Opt+↑` |
| 居中 1/3 | `Cmd+Opt+C` |

### 3.3 Snippets（文本模板）

OPE 常用 Snippets 预设：

```
// 代码相关
;lic    → MIT License header
;todo   → // TODO(skat): 
;fixme  → // FIXME: 

// 沟通相关
;sig    → "— OPE · building in public"
;pr     → "Please review when you get a chance."
;gm     → "Good morning! ☕"

// 项目相关模板
;readme → README.md 骨架
;changelog → CHANGELOG 条目模板
```

设置路径: Raycast → Extensions → Snippets → Add Snippet

### 3.4 快捷链接

```
;gh     → github.com (打开 GitHub)
;gist   → gist.github.com (快速创建代码片段)
;figma  → figma.com (打开 Figma)
;v0     → v0.dev (Vercel AI 设计工具)
;dash   → 项目 Dashboard URL
```

设置路径: Raycast → Extensions → Quicklinks → Add Quicklink

---

## 四、自定义脚本扩展

Raycast 支持运行自定义 bash/applescript/python 脚本。以下是一些 OPE 场景的实用脚本：

### 4.1 一键打开开发环境

创建 Raycast Script Command: `ope-dev`

```bash
#!/bin/bash
# 一键打开: VS Code + Warp + Chrome(开发用 tab 组)
open -a "Visual Studio Code" ~/projects  # 你的项目目录
open -a "Warp"
```

### 4.2 项目切换器

创建 Raycast Script Command: `ope-switch`

```bash
#!/bin/bash
# 根据选择切换到不同项目
project=$(echo -e "project-alpha\nproject-beta\nlearning-notes" | fzf --height 40%)
if [ -n "$project" ]; then
  code ~/projects/"$project"
  cd ~/projects/"$project" && warp
fi
```

### 4.3 快速新建 Markdown 笔记

```bash
#!/bin/bash
# 创建带 frontmatter 的 Markdown 笔记
filename="$HOME/notes/$(date +%Y-%m-%d)-${1:-note}.md"
cat > "$filename" << EOF
---
date: $(date +%Y-%m-%dT%H:%M:%S%z)
tags: []
---

# $(echo "${1:-note}" | sed 's/-/ /g')
EOF
open -a "Visual Studio Code" "$filename"
```

---

## 五、与 Shortcuts 的分工

| 场景 | 用哪个 | 为什么 |
|------|--------|--------|
| 启动应用 / 搜索文件 / 窗口布局 | Raycast | 毫秒级响应 |
| 定时任务（每天清理下载文件夹） | Shortcuts | 系统级定时器 |
| 跨 app 串联（截图→改尺寸→存指定文件夹） | Shortcuts | 原生 Apple 事件 |
| 复杂条件逻辑（如果周一是月初，生成报表） | Shortcuts | Raycast 脚本不适合做复杂调度 |

### 两个必须配的 Shortcuts 自动化

**1. 每日工作区准备**
```
触发: 每天早上 8:30 自动运行
动作: 打开 Warp → 打开 VS Code → 打开 Chrome → 排列窗口
```

**2. 下载文件夹自动清理**
```
触发: 每周日晚 10:00
动作: 将 7 天前的文件移到 ~/Downloads/_archive/
```

---

## 六、可回撤

```bash
# Raycast 完整卸载
brew uninstall --cask raycast
rm -rf ~/Library/Application\ Support/com.raycast.mac.Raycast

# 单项回撤: 在 Raycast 设置中直接禁用某个 Extension 即可
```

---

## 七、进阶方向（后续按需启用）

- **Raycast Pro**（$8/月）：AI 功能、无限剪贴板、云同步。等基础工作流跑顺后再考虑
- **Hammerspoon**：如果将来需要更底层的窗口自动化（比如特定 app 自动移动到特定显示器），可以加 Hammerspoon 作为 Raycast 的补充
- **Keyboard Maestro**：如果 Shortcuts 的自动化逻辑变得过于复杂，可以升级到 KM。当前阶段不需要
