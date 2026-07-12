# Flutter 跨平台技术方案评估

> OPE macOS Workflow · 2026-05-18

## 核心问题

Go + TypeScript 全栈开发者，3-6 个月内有移动端上架需求，要不要转 Flutter？

## 两条路对比

### 路线 A：Flutter + Dart

| 维度 | 评估 |
|------|------|
| 语言门槛 | Dart 是全新语言，但语法接近 TS/Java，有 TS 基础 2-3 周可上手 |
| 移动端产出 | iOS + Android 一套代码，原生性能，App Store/Google Play 直接上架 |
| Web 端 | Flutter Web 可覆盖但不如原生 Web 框架（SEO 差、首屏慢） |
| 与 Go 后端协作 | 标准 REST/GraphQL/gRPC 调用，无特殊耦合 |
| 生态成熟度 | 成熟，pub.dev 包丰富，Firebase/Appwrite 集成完善 |
| 单人维护成本 | 中——一套代码出三端，但要学 Dart 生态 |
| OPE 适配度 | ★★★★ 适合「一个产品多端发布」的场景 |

### 路线 B：React Native + Expo

| 维度 | 评估 |
|------|------|
| 语言门槛 | TypeScript 直接复用，零新语言成本 |
| 移动端产出 | iOS + Android，Expo 生态大幅简化原生配置 |
| Web 端 | 配合 Next.js 已有的 Web 端，但 RN Web 不推荐用于复杂场景 |
| 与 Go 后端协作 | 同 Flutter |
| 生态成熟度 | 成熟，但第三方库质量参差，原生桥接有时需要写 Kotlin/Swift |
| 单人维护成本 | 中高——Web + Mobile 是两套 UI 代码，改设计要改两遍 |
| OPE 适配度 | ★★★ 适合「Web 已有、移动端补位」的场景 |

## 推荐：路线 A — Flutter

理由不是 Flutter 比 RN「更好」，而是在你的约束下更优：

1. **你是从零开始做移动端**，没有历史 RN 包袱，Flutter 的学习成本和 RN 差不多但天花板更高
2. **OPE 单人维护**决定了代码复用率是核心指标——Flutter 一套 UI 代码出两端，RN 要额外维护 Web 端
3. **App Store 上架体验** Flutter 更顺滑，RN 的原生依赖有时让你不得不写 Swift/Kotlin
4. **Dart 不难**——你有 Go 的静态类型经验 + TS 的现代语法经验，学 Dart 是两者的交集

## Web 端怎么处理？

**Flutter 不替代你的 Web 技术栈。** 分工如下：

```
          ┌─────────────────────────┐
          │    Go 后端 API 层        │  ← Go (不变)
          └──────────┬──────────────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
┌────▼─────┐  ┌─────▼──────┐  ┌─────▼──────┐
│ Next.js   │  │ Astro     │  │ Flutter    │
│ Web 应用  │  │ 内容站点  │  │ Mobile App │
└──────────┘  └───────────┘  └────────────┘
   TS/React       TS/Astro       Dart
```

- Web 端继续用 TS 框架（Next.js/Astro/Hono，见框架选型文档）
- 移动端用 Flutter
- 共享 Go 后端 API

## 学习路径（3-6 个月计划）

### 第 1-2 周：Dart 基础
- Dart 语言 tour（官方文档）
- 重点理解：async/await、Stream、null safety、isolates
- 写几个纯 Dart 命令行小工具练手

### 第 3-6 周：Flutter 核心
- Widget 树思维（和 React 组件树类似但细节不同）
- 状态管理：从 Provider 入门，Riverpod 进阶
- 路由、导航、表单

### 第 7-12 周：实战项目
- 选一个你已有的 Web 产品，把它移动端化
- 集成 Go 后端 API
- 处理推送通知、离线存储、App Store 提审流程

### 第 13-24 周：上架打磨
- TestFlight 内测
- App Store 审核准备
- 性能优化、崩溃收集

## 可回撤方式

- Flutter 和 Dart SDK 通过 `flutter doctor` 管理，卸载只需 `rm -rf ~/development/flutter`
- 现有 Go + TS 项目完全不受影响，Flutter 是纯增量
- 如果 2 个月内觉得 Dart/Flutter 不对，切回 RN 的成本是沉没的学习时间，没有代码债务
