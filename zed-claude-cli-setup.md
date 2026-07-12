# Zed 编辑器 + Claude CLI 配置指南

> OPE macOS Workflow · 2026-05-18

---

## 一、为什么 Zed + VS Code 组合

| 场景 | 工具 | 原因 |
|------|------|------|
| 大型项目、复杂重构、多文件编辑 | VS Code | 插件生态、AI agent、调试器 |
| 快速编辑、单文件修改、临时脚本 | Zed | 秒开、极简、不占资源 |
| 协作编程 | Zed | 原生协作、共享光标 |
| Git 操作、PR review | VS Code | GitLens 生态 |

Zed 不是替代品，是互补工具——当你只想「打开改一行就跑」，Zed 比 VS Code 快 10 倍。

---

## 二、Zed 安装与基础配置

### 安装

```bash
brew install --cask zed
```

### 配置文件

路径: `~/.config/zed/settings.json`

```json
{
  "theme": "One Dark",
  "ui_font_size": 14,
  "buffer_font_size": 14,
  "buffer_font_family": "JetBrains Mono",
  "tab_size": 2,
  "soft_wrap": "prefer_line",
  "vim_mode": false,
  "telemetry": {
    "diagnostics": false,
    "metrics": false
  },
  "features": {
    "copilot": false
  },
  "languages": {
    "Go": {
      "language_servers": ["gopls"],
      "format_on_save": "on",
      "tab_size": 4
    },
    "TypeScript": {
      "format_on_save": "on",
      "tab_size": 2,
      "prettier": { "singleQuote": true, "trailingComma": "all" }
    },
    "Dart": {
      "tab_size": 2,
      "format_on_save": "on"
    }
  }
}
```

### 关键快捷键（和 VS Code 对齐）

| 操作 | VS Code | Zed |
|------|---------|-----|
| 命令面板 | `Cmd+Shift+P` | `Cmd+Shift+P` |
| 文件搜索 | `Cmd+P` | `Cmd+P` |
| 全局搜索 | `Cmd+Shift+F` | `Cmd+Shift+F` |
| 终端 | ``Ctrl+` `` | ``Ctrl+` `` |
| 注释 | `Cmd+/` | `Cmd+/` |
| 多光标 | `Opt+Click` | `Opt+Click` |

几乎一致，切换无痛。

### 可回撤

```bash
brew uninstall --cask zed
rm -rf ~/.config/zed
```

---

## 三、Claude CLI（claude-agent-sdk）配置

### 前置条件

```bash
# 确认 Node.js >= 18
node --version

# 如未安装
brew install node
```

### 安装 Claude Agent SDK

```bash
npm install -g @anthropic-ai/claude-agent-sdk
```

### 验证安装

```bash
claude --version
```

### 认证配置

SDK 需要 Anthropic API Key。假设你已有 API key：

```bash
# 写入环境变量（推荐用 Raycast 存，不写明文到 .zshrc）
export ANTHROPIC_API_KEY="sk-ant-xxx"

# 或通过 claude 命令配置
claude auth
```

### 在 VS Code 中使用 Claude

安装 Cline 扩展后（已在扩展清单中），配置 provider 为 Anthropic API：

1. `Cmd+Shift+P` → `Cline: Open Settings`
2. API Provider: Anthropic
3. 填入 API Key
4. Model: `claude-sonnet-4-20250514`（或最新模型）

### Zed 中集成 Claude

Zed 原生支持 AI 面板，配置路径 `~/.config/zed/settings.json` 追加：

```json
{
  "assistant": {
    "enabled": true,
    "default_model": {
      "provider": "anthropic",
      "name": "claude-sonnet-4-20250514"
    },
    "version": "2"
  },
  "provider": {
    "name": "anthropic",
    "api_key": "$ANTHROPIC_API_KEY"
  }
}
```

> **注意**: API key 走环境变量，别明文写在配置文件里。

### 可回撤

```bash
npm uninstall -g @anthropic-ai/claude-agent-sdk
# 从 .zshrc 中删除 ANTHROPIC_API_KEY 行
```

---

## 四、使用建议

1. **Zed 做轻量活**：临时脚本、配置文件 tweak、Markdown 写作
2. **VS Code 做重活**：多文件重构、调试、测试、Git 复杂操作
3. **Claude CLI**：当你不想切到浏览器时，终端里直接问 Claude 写命令
4. **别同时开两个 AI agent**——Cline 在 VS Code 干活时，Zed 的 Claude 面板关掉，避免 token 浪费

---

## 五、RSS 智能订阅技术方案（Go + LLM）

这是你提到的一个很好的自动化方向。方案概要：

```
RSS 源 → Go 爬虫 → 内容提取 → Claude API 打分 → 达到阈值 → 自动订阅
```

### 核心逻辑

```go
// 伪架构
type Article struct {
    Title   string
    Content string
    Source  string
}

func EvaluateArticle(a Article) (score float64, subscribe bool) {
    prompt := fmt.Sprintf(`
评估以下文章对独立开发者的价值（0-100分）：
标题: %s
来源: %s
内容概要: %s

评分标准:
- 技术深度 (40分): 是否有独特见解或深层分析
- 可操作性 (30分): 能否直接应用到工作中
- 信息密度 (30分): 是否废话少、干货多

低于60分不推荐订阅。`, a.Title, a.Source, truncate(a.Content, 2000))

    result := claudeAPI.Evaluate(prompt)
    score = result.Score
    subscribe = score >= 60
    return
}
```

这个可以后续作为独立小项目来做。先记下思路，放在自动化拓展清单里。
