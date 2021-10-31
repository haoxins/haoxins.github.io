---
title: KServe and Dapr (Serverless)
description: 明月出天山, 苍茫云海间. 长风几万里, 吹度玉门关.
date: 2021-08-24
---

## KServe

* [KServe](https://github.com/kserve/kserve)

------------------

## Dapr

### Dapr Concepts

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

## Knative

* [Knative Operator](https://github.com/knative/operator)

### Knative Serving

* 原本 `KFServing` 基于 *Knative*
* 后来 `KFServing` 改名 **KServe**,
  且 *Knative* 变为*可选依赖*

### Knative Eventing

* *Eventing* 的存在, 没有意义, 忽略~
