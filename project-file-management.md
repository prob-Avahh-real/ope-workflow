# 项目文件管理规范化方案

> OPE macOS Workflow · 2026-05-18

---

## 一、问题诊断

「本地散落」是开发者常态，但作为 OPE，散落的代价比打工人高——你的项目就是你的资产，散落 = 丢失风险 + 上下文切换成本 + 备份困难。

---

## 二、推荐目录结构

```
~/projects/              ← 所有项目的根（一个目录管所有）
├── active/              ← 正在活跃开发的
│   ├── product-alpha/   ← Go + Next.js 项目
│   ├── flutter-app/     ← Flutter 移动端项目
│   └── api-service/     ← Go 纯后端
├── experiments/         ← 试验性项目、side project
│   ├── rss-scorer/      ← RSS 智能评分工具
│   └── hono-playground/ ← Hono 框架尝鲜
├── archive/             ← 已完成的/不再维护的
│   └── old-landing-page/
├── lib/                 ← 跨项目共享的库/工具
│   └── go-utils/        ← 自己写的 Go 工具包
└── templates/           ← 项目脚手架模板
    ├── go-api-template/
    └── next-app-template/
```

### 为什么这样分

- **active / experiments / archive** 按活跃度分层，打开 `~/projects/` 不会眼花缭乱
- **lib** 避免跨项目复制粘贴代码——同一个工具函数改一处就行
- **templates** 减少新建项目的摩擦——`cp -r templates/next-app-template ~/projects/active/new-project`

---

## 三、迁移步骤（零风险，渐进式）

### 第 1 步：创建目录结构（1 分钟）

```bash
mkdir -p ~/projects/{active,experiments,archive,lib,templates}
```

### 第 2 步：盘点现有项目（10 分钟）

打开终端，找出你所有散落的项目目录：

```bash
# 查找所有含 .git 的目录（大概率是你的项目）
find ~ -maxdepth 5 -name ".git" -not -path "*/node_modules/*" -not -path "*/Library/*" 2>/dev/null | sed 's/\/.git//' | sort
```

把输出过一遍，决定每个项目放进 active / experiments / archive 哪个分类。

### 第 3 步：逐个迁移（不要一起搬）

对每个项目：

```bash
# 移动（而非复制，避免两份代码不同步）
mv ~/Documents/old-project ~/projects/active/product-alpha

# 如果原位置有其他工具依赖该路径，创建软链接
ln -s ~/projects/active/product-alpha ~/Documents/old-project
```

### 第 4 步：配置快捷访问

**Raycast Quicklink**:
- `;proj` → 在 Finder 中打开 `~/projects/active/`

**终端别名**（加到 `~/.zshrc`）:

```bash
alias pj="cd ~/projects"
alias pja="cd ~/projects/active"
alias pjx="cd ~/projects/experiments"
```

**VS Code 工作区文件**:
在每个 active 项目的根目录下已有 `.vscode/` 配置时，直接在 Raycast 中输入项目名即可定位。

---

## 四、Git 管理规范

每个项目独立的 git 仓库，不做 monorepo（单人维护 monorepo 是过度工程）。

但加一个：**`~/projects/.github/` 存放跨项目的 GitHub 配置**（Issue 模板、PR 模板），需要时复制过去。

```bash
mkdir -p ~/projects/.github
```

---

## 五、备份策略

既然是 OPE，你的代码是你最重要的资产之一。最小化但可靠的备份方案：

```
~/projects/  →  GitHub (每个项目一个 repo)
             →  定期 rsync 到外置硬盘或 NAS（如果有的（如果有）
```

**最简单方案**：所有项目推 GitHub，`~/notes/` 和 `~/projects/templates/` 也建 repo 推上去。GitHub 本身就是异地备份。

**可选增强**：Arq 或 Backblaze 做全盘备份（包括 `~/projects/`、`~/.config/`、`~/notes/`）。

---

## 六、可回撤

整个方案只涉及 `mv` 和 `ln -s`，没有写过任何不可逆的文件操作。回撤：

```bash
# 把项目移回去
mv ~/projects/active/product-alpha ~/Documents/old-project

# 删除目录结构（确保里面没东西再删）
rmdir ~/projects/active ~/projects/experiments ~/projects/archive ~/projects/lib ~/projects/templates ~/projects

# 从 .zshrc 中删除别名
```
