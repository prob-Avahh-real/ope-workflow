# OPE macOS 工作流 · 完整操作手册

> 以 OPE 之名 · 2026-05-18
> 
> 每步相互独立、可分别回撤。回撤方式标注在每步末尾。
> 操作顺序建议从上到下，但不强制。

---

## 总览：工具链全景

```
┌──────────────────────────────────────────────────────┐
│                    OPE 工作流                          │
├──────────────┬──────────────┬─────────────────────────┤
│   开发层      │   创作层      │   自动化层              │
│              │              │                         │
│ VS Code 主力  │ Figma 设计   │ Raycast 中枢            │
│ Zed 轻量编辑  │ Astro/Next   │ Shortcuts 系统编排      │
│ Go + TS 全栈  │ 博客+社交    │ Warp 终端               │
│ Flutter 移动  │ 公域内容     │ Chrome 策略             │
│ Claude AI     │              │                         │
└──────────────┴──────────────┴─────────────────────────┘
```

---

## 第一步：项目文件整理

**目标**: 从「本地散落」到结构化目录

### 操作

```bash
# 1. 创建目录结构
mkdir -p ~/projects/{active,experiments,archive,lib,templates,.github}

# 2. 盘点现有项目
find ~ -maxdepth 5 -name ".git" -not -path "*/node_modules/*" -not -path "*/Library/*" 2>/dev/null | sed 's/\/.git//' | sort

# 3. 逐个迁移（示例）
mv ~/path/to/old-project ~/projects/active/product-name

# 4. 配置终端别名
cat >> ~/.zshrc << 'EOF'
# OPE 项目快速跳转
alias pj="cd ~/projects"
alias pja="cd ~/projects/active"
alias pjx="cd ~/projects/experiments"
EOF

source ~/.zshrc
```

### 回撤
```bash
# 移回原处
mv ~/projects/active/product-name ~/path/to/old-project
# 删除别名（编辑 ~/.zshrc 删除对应行）
# 删除空目录
rmdir ~/projects/active ~/projects/experiments ~/projects/archive ~/projects/lib ~/projects/templates ~/projects
```

> 详细说明: `project-file-management.md`

---

## 第二步：VS Code 全栈环境

**目标**: 一套配置覆盖 Go + TypeScript + Flutter 开发

### 操作

1. **复制配置文件**

```bash
# settings.json
cp vscode-settings.json ~/Library/Application\ Support/Code/User/settings.json

# keybindings.json
cp vscode-keybindings.json ~/Library/Application\ Support/Code/User/keybindings.json
```

2. **批量安装扩展**（见 `vscode-extensions.md` 中的批量安装命令）

3. **关键决策点**：
   - AI 补全: GitHub Copilot（$10/月，延迟低）或 Cline（按 API 用量）——建议 Copilot 做补全，Cline 做复杂任务
   - 主题: One Dark Pro（已在 settings 中配置）
   - 图标: Material Icon Theme

### 回撤
```bash
# 备份还原
cp ~/Library/Application\ Support/Code/User/settings.json ~/Library/Application\ Support/Code/User/settings.json.bak
# 或删除配置文件恢复默认
rm ~/Library/Application\ Support/Code/User/settings.json
rm ~/Library/Application\ Support/Code/User/keybindings.json
# 逐个卸载扩展: code --uninstall-extension <id>
```

> 详细说明: `vscode-settings.json`, `vscode-keybindings.json`, `vscode-extensions.md`

---

## 第三步：Zed 编辑器（轻量补充）

**目标**: 快速编辑场景用 Zed，不拖慢 VS Code

### 操作

```bash
# 安装
brew install --cask zed

# 创建配置目录和文件
mkdir -p ~/.config/zed
cp zed-settings.json ~/.config/zed/settings.json
```

### 回撤
```bash
brew uninstall --cask zed
rm -rf ~/.config/zed
```

> 详细说明: `zed-claude-cli-setup.md`

---

## 第四步：Claude CLI 配置

**目标**: 终端中直接调用 Claude

### 操作

```bash
# 安装
npm install -g @anthropic-ai/claude-agent-sdk

# 配置 API Key（推荐：用 Raycast 的安全存储，而非明文 .zshrc）
# 临时方案：环境变量
export ANTHROPIC_API_KEY="sk-ant-xxx"
# 持久化: 在 ~/.zshrc 中添加上行，或后续用 Raycast 管理
```

### 回撤
```bash
npm uninstall -g @anthropic-ai/claude-agent-sdk
# 从 ~/.zshrc 删除 ANTHROPIC_API_KEY 行
```

> 详细说明: `zed-claude-cli-setup.md`

---

## 第五步：Raycast 自动化中枢

**目标**: 替代 Spotlight，补充窗口管理、剪贴板、Snippets

### 操作

```bash
# 安装
brew install --cask raycast

# 首次启动后：
# 1. 系统设置 → 键盘 → Spotlight → 取消勾选 "显示 Spotlight 搜索"
# 2. Raycast 热键设为 Cmd+Space（继承 Spotlight 习惯）
```

### 必配项（按优先级）

| 优先级 | 功能 | 操作 |
|--------|------|------|
| 🔴 必须 | 剪贴板历史 | Extensions → Clipboard History → 启用，设快捷键 `Cmd+Shift+V` |
| 🔴 必须 | 窗口管理 | Extensions → Window Management → 设快捷键（左半屏/右半屏/全屏） |
| 🟡 推荐 | Snippets | Extensions → Snippets → 添加常用模板（见 `raycast-automation.md` 第四节） |
| 🟡 推荐 | Quicklinks | Extensions → Quicklinks → 添加高频链接 |
| 🟢 可选 | 自定义脚本 | Extensions → Script Commands → 按需添加 |

### 回撤
```bash
brew uninstall --cask raycast
rm -rf ~/Library/Application\ Support/com.raycast.mac.Raycast
# 单项回撤: Raycast → Extensions → 选中 → Disable
```

> 详细说明: `raycast-automation.md`

---

## 第六步：Shortcuts 自动化

**目标**: 系统级定时和跨 app 编排

### 必配项

**1. 每日工作区准备**

Shortcuts app → 新建 → 添加动作：
- Open App: Warp
- Open App: Visual Studio Code
- Open App: Google Chrome
- Wait: 3 seconds
- 排列窗口（如果 Raycast 已接管窗口管理，此步可跳过）

触发: Automation 标签 → Time of Day → 8:30 AM → 工作日

**2. 下载文件夹周清理**

Shortcuts app → 新建 → 添加动作：
- Find Files: ~/Downloads, Created Date in last 7 days → Move to ~/Downloads/_archive/

触发: Automation 标签 → Time of Day → 每周日 22:00

### 回撤
Shortcuts app → Automation → 删除对应自动化即可。

---

## 第七步：Chrome 浏览器治乱

**目标**: Tab 不乱、书签可找、RSS 有策略

### 操作

1. **Tab Groups 规则**（零安装）：
   - 每个项目/场景建一个 Tab Group，命名规范 `[项目名] → 🟢/🔵/🟡`
   - 结束时折叠或关闭非活跃组

2. **Workona 扩展**（推荐安装）：
   - Chrome Web Store 搜 "Workona" → 安装
   - 创建工作区：开发 / 写作 / 设计 / 竞品 / 待读
   - 每个工作区保存对应 tab 集

3. **RSS 订阅**：
   - 注册 Inoreader 免费版
   - 手动添加 15-20 个高质量独立博客

4. **日终习惯**：超过 10 个 tab → 清到 Workona 或关闭

### 回撤
- Tab Groups: Chrome 原生，无需卸载
- Workona: `chrome://extensions` → 移除
- Inoreader: 删除账号或停用

> 详细说明: `chrome-rss-strategy.md`

---

## 第八步：Figma 设计工具

**目标**: UI 设计 + 开发衔接

### 操作

```bash
brew install --cask figma
```

设计流程 SOP:
1. 找参考（Dribbble / Mobbin）
2. v0.dev 生成初版 UI
3. Figma 精调
4. Dev Mode (`Shift+D`) 出代码
5. VS Code 实现

### 回撤
```bash
brew uninstall --cask figma
# 云端数据保留在 figma.com
```

> 详细说明: `figma-workflow.md`

---

## 第九步：框架策略总结

**目标**: 不同项目用不同框架，不搞全家桶

| 项目类型 | 框架 | 部署 |
|----------|------|------|
| SaaS Web 应用 | Next.js (App Router) | Vercel / Fly.io |
| 内容站点 / 博客 | Astro | Cloudflare Pages |
| 轻量 API / 工具 | Hono + htmx | Cloudflare Workers |
| 移动端 App | Flutter + Dart | App Store / Play Store |
| 核心后端 | Go | Fly.io / Railway |

> 详细说明: `framework-content-strategy.md`

---

## 第十步：内容策略速查

**日常节奏**:
- 朋友圈 1 条/天（做了什么、破什么坑）
- Twitter 3-5 条/周（技术 tip、产品进展）
- 博客 1-2 篇/月（深度复盘、教程）

**漏斗**: 朋友圈碎碎念 → Twitter 短文 → 博客长文 → 自然获客

> 详细说明: `framework-content-strategy.md`

---

## 附录 A：文件索引

本工作流包含以下文件，均位于 `~/ope-workflow/`（或你存放的位置）：

| 文件 | 内容 |
|------|------|
| `README.md`（本文件） | 完整操作手册 |
| `flutter-evaluation.md` | Flutter vs RN 技术评估 + 学习路径 |
| `vscode-settings.json` | VS Code 配置文件 |
| `vscode-keybindings.json` | VS Code 快捷键 |
| `vscode-extensions.md` | VS Code 扩展清单 + 批量安装命令 |
| `zed-claude-cli-setup.md` | Zed 编辑器 + Claude CLI + RSS 技术方案 |
| `raycast-automation.md` | Raycast 完整配置 + 自定义脚本 |
| `chrome-rss-strategy.md` | Chrome Tab 管理 + RSS 订阅策略 |
| `project-file-management.md` | 项目目录规范化方案 |
| `figma-workflow.md` | Figma 设计工作流入门 |
| `framework-content-strategy.md` | Web 框架选型 + 公域内容策略 |

---

## 附录 B：回撤总表

| 步骤 | 回撤命令 |
|------|----------|
| 项目目录 | `mv` 移回原处 |
| VS Code | 删除 settings.json / keybindings.json |
| Zed | `brew uninstall --cask zed && rm -rf ~/.config/zed` |
| Claude CLI | `npm uninstall -g @anthropic-ai/claude-agent-sdk` |
| Raycast | `brew uninstall --cask raycast && rm -rf ~/Library/Application\ Support/com.raycast.mac.Raycast` |
| Shortcuts | Shortcuts app → Automation → 删除 |
| Chrome 扩展 | `chrome://extensions` → 移除 Workona |
| Figma | `brew uninstall --cask figma` |
| Flutter | `rm -rf ~/development/flutter` |

**所有步骤都是纯增量的——没有任何一环依赖另一环必须完成。你可以按任意顺序、任意组合执行，停在任何一步都不影响已完成的配置。**

---

## 附录 C：后续可选项目

这些不在本次范围，但思路已经留好：

1. **RSS 智能评分器**（Go + Claude API）：自动判断文章含金量并订阅，预估 3-5 天开发
2. **Raycast Pro 升级**（$8/月）：AI 搜索、无限剪贴板、云同步
3. **Hammerspoon**：如果将来多显示器、需要更精细的窗口自动化
4. **项目模板脚手架**：在 `~/projects/templates/` 中沉淀 go-api-template、next-app-template
5. **Figma → Flutter 设计 Token 自动化**：用 Material Theme Builder 导出，减少手动翻译
