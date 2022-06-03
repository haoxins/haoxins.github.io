---
title: KServe and Dapr (Serverless)
description: 明月出天山, 苍茫云海间. 长风几万里, 吹度玉门关.
date: 2021-08-24
---

## Dapr

### Dapr Components

* State store component
  - Azure CosmosDB
  - Redis
  - GCP Firestore

* Pub/Sub brokers component
  - Apache Kafka
  - NATS Streaming
  - Redis Streams

* Secret store component
  - Kubernetes secrets

* Name resolution provider component
  - Kubernetes
  - HashiCorp Consul

------------------

## KServe

* [KServe](https://github.com/kserve/kserve)

* `2021-11`, 基于 **Dapr** 打造自己的
  *Model serving*, 还是基于 **KServe**?
  - **KServe**: 专为 *Model serving* 而生, 但项目*半死不活*
  - **Dapr**: 足够活跃, 需要自己做一些 *Model serving* 的 *逻辑 & 调度*
  - 个人倾向于 **Dapr**

------------------

## Knative

* [Knative Operator](https://github.com/knative/operator)

### Knative Serving

* 原本 KFServing 基于 Knative
* 后来 KFServing 改名 **KServe**,
  且 Knative 变为可选依赖

* 相较于 K8s, Knative 的抽象层次并没有显著提高
  - Dapr 是抽象层次提高的典型
* 除非与特定类型的 VMs (K8s node pool) 结合,
  否则, 在常规场景下, 资源利用率不会有显著提高.
  - 管理服务的人力投入, 也是资源, 不仅仅是算力
* 综上, `Knative Serving` 对于绝大多数公司, 场景, 意义有限.
  - K8s 甚至可以内置一些 Serverless 的抽象

### Knative Eventing

* Eventing 的存在, **没有意义**, 忽略~

------------------

## Events

### 2021

* [KServe: The next generation of KFServing](https://blog.kubeflow.org/release/official/2021/09/27/kfserving-transition.html)
  - KFServing is now KServe
  - The project has been rebranded from
    KFServing to KServe, and we are planning
    to graduate the project from
    Kubeflow Project later this year.
