---
layout: default
title: 初识 loopback
description: 现代化的 node.js API 框架
date: 2017-08-31
---

## 概述

[loopback-next][lb-repo-url] 是 [strongloop][sl-org-url] 团队打造的新一代 node.js APIs 框架.
原本的 `loopback v3` 基于 [express][exp-repo-url], 而在 `next` 当中则不再依赖.

相较于 `rails`, `django`, `meteor` 等框架, `loopback` 最大的差异在于: 仅提供 `API service`.
后面会有一篇文章再论述 [loopback的前端快速整合方案](articles/2017-loopback-and-angular-admin.md).

* 特点
  - 快速开发, 高效实现业务逻辑
  - 高度可配置, 可扩展
  - 强大的命令行工具, 简单的命令便可产出完整的 `API service`, 定义 `model` 等
  - 便于测试
  - 完善的周边生态, 丰富的组件库
  - 充分利用 `TypeScript` 语法特性
  - 符合 [OpenAPI][open-api-url] 规范

* 核心功能
  - `代码即文档`: 不是说好的代码就是文档, 而是直接根据代码定义输出完备的 APIs 文档
  - `角色, 权限`: 自带强大的, 灵活的 `role`, `permission` 功能
  - `model, data`: 支持各种主流的和非主流的数据库, 可靠的 `类ORM` 实现
  - `client SDK`: 可以直接生成各平台SDK, `web`, `ios`, `android` 等

## Thinking in LoopBack

* [官方Wiki地址](https://github.com/strongloop/loopback-next/wiki/Thinking-in-LoopBack)

### 定义 APIs

## 核心概念

## License
MIT

[lb-repo-url]: https://github.com/strongloop/loopback-next
[exp-repo-url]: https://github.com/expressjs/express
[sl-org-url]: https://github.com/strongloop
[open-api-url]: https://www.openapis.org
