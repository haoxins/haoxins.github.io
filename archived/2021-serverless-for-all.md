---
title: Serverless for everything
description: 携取旧书归万隐, 野花啼鸟一般春
date: 2020-07-22
---

## ML pipeline

* [Kubeflow](https://github.com/kubeflow)

------------------

## Data flow

* [Datafuse](https://github.com/datafuselabs/datafuse)

### Streaming

* Checkpoints + Serverless jobs

### Batch

* Already

------------------

## Application service

* [Dapr](https://github.com/dapr/dapr)

------------------

## QUIC

------------------

* **2021** 注定是一个节点, 但未必称得上是*转折点*
  - 一方面: 商业上的红利期已过, *低垂的果实*基本不再, 行业开始反垄断等整治;
  - 另一方面: 技术上, 国内有大量的*优质开发人员*, 且已经积累了*足够的应用场景*.
  - *精耕细作*的技术时代已经到来!

* **2021**, 我写下我认为属于 **基础设施** 的 *Components*
  - 看看 *5年后*, *10年后*, 会是什么光景
  - *Components* 包括: *标准*, *开源项目*
  - [Kubernetes (K8s)](https://github.com/kubernetes/kubernetes)
  - [Go](https://github.com/golang/go)
  - [RFC9000: QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
  - [Rust](https://github.com/rust-lang/rust)
  - [Istio](https://github.com/istio/istio)

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
  - Flink
  - Dapr

### 云存储

* 云计算的 **Top1** 产品, **没有之一**

* [Network-attached storage](https://en.wikipedia.org/wiki/Network-attached_storage)
  - [Network File System](https://en.wikipedia.org/wiki/Network_File_System)
  - [NFS version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc3010)
  - [Network File System (NFS) Version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc7530)

* Aliyun
  - NAS
  - OSS
  - EBS