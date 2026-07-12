# Figma UI 设计工作流配置

> OPE macOS Workflow · 2026-05-18

---

## 一、安装与基础设置

```bash
brew install --cask figma
```

或从 [figma.com/downloads](https://figma.com/downloads) 下载桌面端（桌面端比 Web 版性能好）。

### 初始设置

1. 登录 Figma 账号
2. 安装 Figma 字体服务（首次打开桌面端会提示）
3. 建议新建一个 OPE 专属 Team（免费版支持 1 Team + 3 Figma files per project）

---

## 二、OPE 设计工作流 SOP

### 阶段 1：快速原型（别从零画）

作为全栈开发者，你不是专业设计师。所以：

- **先用参考，不造轮子**：Dribbble、Mobbin、Screenlane 找同类产品的设计参考
- **Figma Community** 有大量免费 UI Kit 和组件库，拿来做底板改
- **v0.dev**（Vercel）可以文字描述生成 UI，导出到 Figma 继续改

```
思路 → v0.dev 生成初版 → Figma 精调 → Dev Mode 出代码
```

### 阶段 2：设计系统（最小化）

不要建大而全的设计系统。OPE 只需要：

- **颜色系统**: Primary / Secondary / Neutral / Error 各 3-5 个色阶
- **排版**: 标题 / 正文 / Caption 三档字号（移动端和 Web 分别定义）
- **间距**: 4px 基准的 spacing scale（4, 8, 12, 16, 24, 32, 48）

用 Figma 的 Styles 和 Variables 功能定义这些，改一个地方全局更新。

### 阶段 3：Dev Mode

这是 Figma 对开发者最有价值的功能：

- 选中任意元素 → 切到 Dev Mode（`Shift+D`）
- 直接看 CSS/Tailwind/SwiftUI 代码
- 测量间距、查看颜色变量、导出资源

**与 VS Code 的衔接**：
1. Figma 中设计定稿
2. Dev Mode 复制 CSS/属性
3. VS Code 中用 Tailwind 或原生 CSS 实现对应的设计

---

## 三、Figma 文件组织

```
📁 OPE Design
├── 🎨 Design System        ← 颜色、字体、组件库
├── 📱 Mobile App (Flutter) ← 移动端所有页面
├── 🌐 Web App              ← Web 端所有页面
├── 📄 Landing Page         ← 独立落地页
└── 🧪 Experiments          ← 探索性设计
```

一个 Figma 文件放一个产品线，别把所有东西塞一个文件里（加载慢）。

---

## 四、设计效率提升

### 必装插件

| 插件 | 用途 |
|------|------|
| **Iconify** | 搜索图标直接拖入（Material、Feather、Lucide 全有） |
| **Unsplash** | 占位图片（设计阶段用，生产环境换真实图片） |
| **Content Reel** | 生成逼真的假数据（人名、地址、文本段落） |
| **Autoflow** | 快速画流程图和用户流程线 |
| **Stark** | 无障碍检查（对比度、色盲模拟） |

### AI 辅助

- **Figma AI**（内置）：自动生成图层名、一键替换文本
- **v0.dev → Figma 插件**：把 v0 生成的 UI 直接导入 Figma 继续编辑
- **Claude**（你已在用）：描述设计需求，Claude 可以帮你生成 Figma 插件脚本或 Dev Mode 中的代码实现

---

## 五、Flutter 设计对接

Flutter 使用 Material Design 3 作为默认设计语言。在 Figma 中设计 Flutter 界面时：

- 用 [Material 3 Design Kit](https://www.figma.com/community/file/1035203688168086460)（Figma Community 免费下载）
- 直接用 M3 组件搭页面，Flutter 端几乎 1:1 还原
- Color Scheme 在 Figma 中定义好后，用 [Material Theme Builder](https://m3.material.io/theme-builder) 导出 Dart 代码

---

## 六、可回撤

```bash
brew uninstall --cask figma
# Figma 云端数据保留在 figma.com 账号中
# 桌面端卸载不影响云端文件
```
