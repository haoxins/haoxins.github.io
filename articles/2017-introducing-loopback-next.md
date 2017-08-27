---
layout: page
title: loopback-next, 现代化的 node.js web 框架
description: null
date: 2017-08-27
---

## loopback: 现代化的 node.js web 框架

* 注: 由于 `loopback-next (v4)` 尚在快速迭代, 文中涉及的技术细节可能会与当前实现不匹配.

### 概述

[loopback-next, 即 loopback v4](https://github.com/strongloop/loopback-next) 是 [strongloop](https://github.com/strongloop) 团队打造的新一代 node.js APIs 框架.
原本的 `loopback (v3)` 基于 [express](https://github.com/expressjs/express), 而在 `v4` 当中则不再依赖.

相较于 `rails`, `django`, `meteor` 等框架, `loopback` 最大的差异在于: 仅提供 `API service`.
后面会有一篇文章再论述 [loopback的前端快速整合方案](articles/2017-loopback-and-angular-admin.md).

* 特点
  - 快速开发, 高效实现业务逻辑
  - 高度可配置, 可扩展
  - 强大的命令行工具, 简单的命令便可产出完整的 `API service`, 定义 `model` 等
  - 便于测试
  - 完善的周边生态, 丰富的组件库
  - 现代化的 JS(TS) 语法, 灵活使用语言特性
  - 符合 [OpenAPI](https://www.openapis.org) 规范

* 核心功能
  - `代码即文档`: 不是说好的代码就是文档, 而是直接根据代码定义输出完备的 APIs 文档
  - `角色, 权限`: 自带强大的, 灵活的 `role`, `permission` 功能
  - `model, data`: 支持各种主流的和非主流的数据库, 可靠的 `类ORM` 实现
  - `client SDK`: 可以直接生成各平台SDK, `web`, `ios`, `android` 等

### 基本概念

### Thinking in LoopBack

### License
MIT
