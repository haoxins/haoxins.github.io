---
title: Serverless for everything
description: 携取旧书归万隐, 野花啼鸟一般春
date: 2020-07-22
---

## ML pipeline

* [Kubeflow](https://github.com/kubeflow)

------------------

## Data flow/computing

* Query
  - SQL              (MySQL)
  - Streaming/Window (Flink SQL)
  - [DataFusion](https://github.com/apache/arrow-datafusion)
  - Graph
  - [GraphScope](https://github.com/alibaba/GraphScope)

* [Databend](https://github.com/datafuselabs/databend)

### Streaming

* Checkpoints + Serverless jobs

### Batch

* Already

------------------

## Application service

* [Dapr](https://github.com/dapr/dapr)

------------------

## QUIC

* [s2n-quic](https://github.com/aws/s2n-quic)

------------------

## Papers

### Boki: Stateful Serverless Computing with Shared Logs

* [Boki: Stateful Serverless Computing with Shared Logs](https://dl.acm.org/doi/pdf/10.1145/3477132.3483541)

```
State management has become a major challenge
in serverless computing. Boki is the first system
that allows stateful serverless functions to
manage state using distributed shared logs.

Boki's shared log abstraction (i.e., LogBooks) can
support diverse serverless use cases, including
fault-tolerant workflows, durable object storage,
and message queues. Boki's shared logs
achieve elasticity, data locality, and resource efficiency,
enabled by a novel metalog design. The metalog is a
unified solution to the problems of log ordering,
consistency, and fault tolerance in Boki.

Evaluations of Boki and its support libraries
demonstrate the performance advantages (up to 4.7×)
of the shared-log-based approach for
serverless state management.
```

> 期待真实的实现

------------------

* **2021** 注定是一个节点, 但未必称得上是*转折点*
  - 一方面: 商业上的红利期已过, *低垂的果实*基本不再, 行业开始反垄断等整治;
  - 另一方面: 技术上, 国内有大量的*优质开发人员*, 且已经积累了*足够的应用场景*.
  - *精耕细作*的技术时代已经到来!

* **2021**, 我写下我认为属于 **基础设施** 的 *Components*
  - 看看 *5年后*, *10年后*, 会是什么光景
  - *Components* 包括: *标准*, *开源项目*
  - [Kubernetes (K8s)](https://github.com/kubernetes/kubernetes)
  - [RFC9000: QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
  - [Istio](https://github.com/istio/istio)
  - [Go](https://github.com/golang/go)
  - [WebAssembly](https://webassembly.org)
  - [Rust](https://github.com/rust-lang/rust)
  - [Dapr](https://github.com/dapr/dapr)
  - [Cilium](https://github.com/cilium/cilium)

* 关于 `Kubernetes`, `2021` 年之前基本完成的是:
  - 所有的东西都跑在了 `K8s` 上
* 那么 `2022` 年开始:
  - 所有的基础组件 (`Components`), 都会深度基于 `K8s` 去开发
* 之前, `K8s` 服务了 `Components` 的使用者
* 接下来, `K8s` 会服务 `Components` 的开发者
* 一个 `Component` 能在非 `K8s` 环境上运行会是一个神奇的事情!
  - `Kafka`, `Flink`, `Airflow` 之流会被淘汰!

------------------

* Result: State
* Input: Event | Log
* Region
  - Storage
  - Compute
* Storage is very very cheap
* Compute is cheap

* Storage & Compute & Network
  - Storage 越来越是 Cloud native (Cloud service)
  - Conpute 目前是 Open source
  - Network

* Compute & Data
  - OLTP vs OLAP
  - Streaming
  - Computing
  - 个人的开发经验基本都是 以 Data 为核心?
  - 什么场景是 Computing 为核心? 游戏渲染? 计算机模拟? (个人对此一无所知)

* 什么算 计算?
  - Input + State (v1) -> compute -> Output + State (v2)
  - State: Local vs Remote
  - State: Centric vs Dsitributed

### Serverless DB ?

* **Database -> Table**, **落伍了**
  - Micro services & Serverless
* Database instance, **落伍了**

* Programing platform
  - [Dapr](https://github.com/dapr/dapr)
  - [Ray](https://github.com/ray-project/ray)

### 云存储

* 云计算的 **Top 1** 产品, **没有之一**
  - 对象存储 `Object storage`, 将会占据 `80%` 以上的存储`场景/市场`

* [Network-attached storage](https://en.wikipedia.org/wiki/Network-attached_storage)
  - [Network File System](https://en.wikipedia.org/wiki/Network_File_System)
  - [NFS version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc3010)
  - [Network File System (NFS) Version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc7530)

* Aliyun
  - NAS
  - OSS
  - EBS

* *Kubernetes* 将会是各大*云厂商*和*开源社区*的`边界`
  - 云厂商: *存储*, *网络*, *弹性 VMs*, *API Services*
  - *Kubernetes* 天生就是跑在 *Cloud* 上的
