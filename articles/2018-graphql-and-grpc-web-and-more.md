---
title: Why GraphQL
description: The future is always awesome
date: 2018-12-02
---

### 基本共识

* 避免重复代码: `app`, `web`, `service`, `serverless function`, `CDN function`
* 避免多次开发: `增|减|改 字段`, `后端数据结构变更`, `service 拆分`, `迁一发, 全身动`
* 降低开发沟通成本: `code` -> `docs`, 共享 `schema` (跨语言)
* 易于测试, 完善的工具集

### 特殊场景

* 复杂查询: `Elasticsearch`, `Open API` (Github API, ...)

### Why API layer ?

* service APIs 不够 `restful`
* APIs 合并, 一个数据, 需要 a, b, c 三个APIs, 然后组装合并
* 接口返回的数据格式各种嵌套不合理
* 接口返回的数据字段命名随意或者风格不统一
* 后端返回的 数据格式/字段名 一旦变了, C端视图绑定部分的代码需要修改

### Why GraphQL ?

### How GraphQL ?

* `Client only` vs `Client & Server`

### GraphQL good for ?

### gRPC-web good for ?

### simple Http/Rest good for ?

### Performance

* How `gRPC` uses `HTTP/2` ?

### Tools

https://github.com/dotansimha/graphql-code-generator

### See also

* [Envoy and gRPC-Web: a fresh new alternative to REST](https://blog.envoyproxy.io/envoy-and-grpc-web-a-fresh-new-alternative-to-rest-6504ce7eb880)
