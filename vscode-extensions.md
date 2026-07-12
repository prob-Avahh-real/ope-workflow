# OPE VS Code 扩展清单

> 安装方式: 在 VS Code 中逐个搜索安装，或运行下方批量安装命令
> 可回撤: `code --list-extensions` 查看已装，`code --uninstall-extension <id>` 逐个卸载

## 批量安装命令

```bash
code --install-extension golang.go
code --install-extension ms-vscode.vscode-typescript-next
code --install-extension dart-code.flutter
code --install-extension dart-code.dart-code
code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
code --install-extension bradlc.vscode-tailwindcss
code --install-extension eamodio.gitlens
code --install-extension github.copilot
code --install-extension github.copilot-chat
code --install-extension saoudrizwan.claude-dev
code --install-extension pkief.material-icon-theme
code --install-extension zhuangtongfa.material-theme
code --install-extension formulahendry.code-runner
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension gruntfuggly.todo-tree
code --install-extension ms-azuretools.vscode-docker
code --install-extension yzhang.markdown-all-in-one
code --install-extension bierner.markdown-mermaid
code --install-extension tamasfe.even-better-toml
code --install-extension grapecity.gc-excelviewer
code --install-extension unifiedjs.vscode-mdx
```

## 扩展用途速查

### 语言核心
| 扩展 | 用途 |
|------|------|
| `golang.go` | Go 语言支持（LSP、调试、测试） |
| `ms-vscode.vscode-typescript-next` | TypeScript 夜间版（更快） |
| `dart-code.flutter` | Flutter 开发（Widget 预览、热重载） |
| `dart-code.dart-code` | Dart 语言基础支持 |

### 代码质量
| 扩展 | 用途 |
|------|------|
| `esbenp.prettier-vscode` | 代码格式化 |
| `dbaeumer.vscode-eslint` | JS/TS 静态检查 |
| `bradlc.vscode-tailwindcss` | Tailwind CSS 智能提示 |
| `streetsidesoftware.code-spell-checker` | 拼写检查（驼峰命名也生效） |

### AI 辅助（三选二，别全开）
| 扩展 | 用途 | 费用 |
|------|------|------|
| `github.copilot` + `copilot-chat` | GitHub Copilot 补全+聊天 | $10/月 |
| `saoudrizwan.claude-dev` | Cline（Claude 驱动编码助手） | 按 API 用量 |

> **建议**: Copilot 做补全（延迟低），Cline 做复杂重构和多文件编辑。别同时开两个 agent 模式，会互相抢焦点。

### Git & 项目
| 扩展 | 用途 |
|------|------|
| `eamodio.gitlens` | Git 增强（行历史、blame、对比） |
| `gruntfuggly.todo-tree` | 代码中 TODO/FIXME 聚合面板 |
| `ms-azuretools.vscode-docker` | Docker 管理 |

### 外观 & 文档
| 扩展 | 用途 |
|------|------|
| `pkief.material-icon-theme` | 文件图标美化 |
| `zhuangtongfa.material-theme` | One Dark Pro 主题 |
| `yzhang.markdown-all-in-one` | Markdown 写作增强 |
| `bierner.markdown-mermaid` | Mermaid 图表预览 |
| `tamasfe.even-better-toml` | TOML 语法支持 |
| `unifiedjs.vscode-mdx` | MDX 支持 |

### 实用工具
| 扩展 | 用途 |
|------|------|
| `formulahendry.code-runner` | 右键快速运行代码片段 |
| `grapecity.gc-excelviewer` | CSV/Excel 预览 |
