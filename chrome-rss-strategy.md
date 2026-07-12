# Chrome Tab 管理 + RSS 智能订阅方案

> OPE macOS Workflow · 2026-05-18

---

## 一、Chrome Tab 治乱方案

### 问题诊断

你描述的症状是「开太多找不到」+「分组混乱」。这不是工具问题，是**流程问题**——tab 是你的短期工作记忆，缺乏「归档」机制。

### 三层方案

#### 第 1 层：原生 Chrome Tab Groups（零成本，立即生效）

Chrome 自带的标签页分组功能其实够用，关键是**固定一套分组规则**：

```
分组命名规范: [项目/场景] → 颜色 ← 状态

示例:
📁 vibe-coding    🟢 活跃
📁 竞品调研       🔵 参考
📁 学习中         🟡 待消化
📁 临时           ⚪ 用完即关
```

**操作**:
- 右键 tab →「向新群组中添加标签页」
- 群组折叠后只占一个 tab 位，点开才展开
- 每天结束时：「临时」组全关；「学习中」组归档到书签

#### 第 2 层：Workona 会话管理（推荐安装）

Workona 是 Chrome 扩展，核心理念是**工作空间切换**——把一组 tab 保存为一个 Workspace，一键切换。

```
OPE Workspaces 示例:

🚀 开发环境    → VS Code Web、GitHub、API 文档、localhost
✍️ 写作        → 博客后台、Grammarly、参考文章
🎨 设计        → Figma、Dribbble、设计系统文档
📊 竞品        → 竞品站点、Similarweb、行业报告
📖 待读        → 存起来稍后读的文章
```

**安装**: Chrome Web Store 搜 "Workona"，免费版够用。

**与 Tab Groups 的关系**: Workona 管「跨会话」的 tab 存档，Tab Groups 管「当前会话」的 tab 临时分组。两者互补。

#### 第 3 层：习惯规则

工具再好，不养成习惯会打回原形：

- **「2 分钟规则」**：打开的 tab 2 分钟内没用到 → 关掉或归档到 Workona
- **「每日清空」**：每天收工时检查 tab 栏，超过 10 个就清到 Workona
- **「一书签一用途」**：书签栏不放临时东西，只放高频固定入口（GitHub、CI Dashboard、产品后台）

### 可回撤

- Tab Groups: Chrome 原生功能，不涉及任何安装/卸载
- Workona: Chrome 扩展，随时在 `chrome://extensions` 中禁用或移除
- 所有数据在 Chrome 同步中，删扩展不丢数据

---

## 二、RSS 订阅策略

### RSS 没过时，但用法变了

RSS 本身是协议，谈不上过时。变的是消费方式——过去是「订阅所有感兴趣的源然后被淹死」，现在是「筛选高信号源，AI 辅助过滤」。

### 推荐工具：Inoreader

| 维度 | Inoreader | Feedly | NetNewsWire |
|------|-----------|--------|-------------|
| 免费额度 | 150 源 | 100 源 | 无限（本地） |
| 自动化规则 | ✅ 付费版 | ✅ 付费版 | ❌ |
| AI 摘要 | ✅ | ✅ | ❌ |
| 与 LLM 集成 | Webhook → 可接 Claude API | 有限 | ❌ |
| 平台 | Web + iOS + Android | Web + iOS + Android | macOS + iOS |

推荐 Inoreader 免费版起步。

### 手动筛选 RSS 源的方法

在「AI 自动判断含金量订阅」实现之前，先用人工方法建立高质量源列表：

1. **从你常刷的站点中**，找出真正每次更新都值得看的，不超过 20 个
2. **关注独立博客而非媒体站**——独立开发者博客的信号密度远高于 TechCrunch 之流
3. **用 Inoreader 的「过滤规则」**：标题含特定关键词的自动标星，其余快速扫过

### AI 自动订阅：技术实现路径（后续项目）

这个可以做为一个独立小项目。完整思路参见 `zed-claude-cli-setup.md` 第五部分的方案。核心流程：

```
发现新源 → Go 爬虫取最近 5 篇文章 → 
拼成 prompt 发给 Claude API 打分 → 
得分 > 60 → 自动添加到 Inoreader
```

用你现有的 Go 技术栈 + Claude API，预估开发时间 3-5 天。可以作为学习 Flutter 前的热身项目。
