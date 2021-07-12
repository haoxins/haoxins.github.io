---
title: 关于 Computing 的思考
description: 携取旧书归万隐, 野花啼鸟一般春
date: 2020-07-22
---

```
2021 注定是一个节点, 但未必称得上是 转折点

一方面: 商业上的红利期已过, 低垂的果实基本不再, 行业开始反垄断等整治;
另一方面: 技术上, 国内有大量的优质开发人员, 且已经积累了足够的应用场景.

精耕细作的技术时代已经到来!
```

* **2021**, 我写下我认为属于 **基础设施** 的 Component
  - 看看 5年后, 10年后, 会是什么光景
  - Component 包括: Website, 标准, 开源项目
  - **No 1** [GitHub](https://github.com)
  - **No 2** [Kubernetes (K8s)](https://github.com/kubernetes/kubernetes)
  - [RFC9000: QUIC](https://datatracker.ietf.org/doc/html/rfc9000)

* Result: State
* Input: Event | Log
* Region
  - Storage
  - Compute
* Storage is very very cheap
* Compute is cheap

* Conpute & Storage
  - Storage 越来越是 Cloud native (Cloud service)
  - Conpute 目前是 Open source
  - IO

### Serverless DB ?

* **Database -> Table**, **落伍了**
  - Micro services & Serverless
* Database instance, **落伍了**

* Programing platform
  - Flink
  - Dapr
  - Ethereum

## 我们需要一个什么样的 Platform ?

### 我们不再应该操心的事情

* 存储扩容
* 数据加密
* 数据备份
* 通讯协议
* Runtime 可用性

### 我们需要 Focus 的事情

* 业务逻辑, 这是最浅显的
* 行业(规则)积累
* 专业(工业控制系统, 规划, ...)建树
