---
title: 关于技术, 次年度期待清单
description: 钟鼓馔玉何足贵, 但愿长醉不复醒.
date: 2018-12-02
---

## 2023 不再继续

------------------

## 2022 Next Generation (Lockdown in 2021-08-20)

### Overview

* [QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
  - [HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-quic-http-34)

* **Why Golang v2?**
  - Just Go `1.18`, `1.19`, `1.20`, ...
  - **Generics**: *1.18+*
  - **Error handling**: *1.2x*
  - **Error values**: *2.xx* or *1.2x*

* **Spring Framework**
  - [Spring Native](https://github.com/spring-projects-experimental/spring-native)
  - 打败 Spring Framework 的一定不是另一个 **Web Framework**

### Machine learning

* [Kubeflow](https://github.com/kubeflow)
  - [Kubeflow](https://github.com/kubeflow/kubeflow)
  - [KFServing](https://github.com/kubeflow/kfserving)
  - [Pipelines](https://github.com/kubeflow/pipelines)
  - [Katib](https://github.com/kubeflow/katib)

> 社区的治理存在风险

### Data Computing

* [Apache Arrow](https://github.com/apache/arrow)
  - https://github.com/apache/arrow-cookbook
  - https://github.com/apache/arrow-rs

* [Databend](https://github.com/databendlabs/databend)
  - https://www.databend.com
  - [Roadmap 2021](https://github.com/databendlabs/databend/issues/746)

* [Vineyard (v6d)](https://github.com/v6d-io/v6d)

### Graph Computing

* [GraphScope](https://github.com/alibaba/graphscope)
  - https://graphscope.io
  - https://github.com/GraphScope
  - https://github.com/apache/tinkerpop
  - https://github.com/v6d-io/v6d

### JDK

* [JDK 17](https://openjdk.java.net/projects/jdk/17/)
  - 最后的 JVM, [GraalVM](https://github.com/oracle/graal)
  - [JEP 414: Vector API](https://openjdk.java.net/jeps/414)
  - [JEP 409: Sealed Classes](https://openjdk.java.net/jeps/409)
  - [JEP 406: Pattern Matching for switch](https://openjdk.java.net/jeps/406)
  - [JEP 395: Records](https://openjdk.java.net/jeps/395)
  - [JEP 394: Pattern Matching for instanceof](https://openjdk.java.net/jeps/394)
  - [JEP 378: Text Blocks](https://openjdk.java.net/jeps/378)
  - [JEP 361: Switch Expressions](https://openjdk.java.net/jeps/361)

> 最终, *Rust* + *Go* 会干掉 *JDK/GraalVM*

### Next Generation Service Runtime

* [Dapr](https://github.com/dapr/dapr)
  - https://dapr.io
  - Not **JVM**
  - Not [GraalVM](https://github.com/oracle/graal)

### Next Generation SQL Database

* [TiDB](https://github.com/pingcap/tidb)
  - HTAP is ready
  - Supports serverless

------------------

## 2021 Machine learning (lockdown in 2020-12-03)

### Machine learning

* KubeFlow
  - [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow)
  - [kubeflow/kfserving](https://github.com/kubeflow/kfserving)
    * [knative/serving](https://github.com/knative/serving)

* Cloud native ML & Data development
  - https://colab.research.google.com 体验很好
  - https://aihub.cloud.google.com

* [MLIR - Multi-Level IR Compiler Framework](https://mlir.llvm.org)
  - http://llvm.org/devmtg/2019-04/slides/Keynote-ShpeismanLattner-MLIR.pdf

* [GCP Vizier](https://cloud.google.com/ai-platform/optimizer/docs/overview)
* [GCP AutoML tables](https://cloud.google.com/automl-tables)

### Database

* [TiDB - HTAP](https://github.com/pingcap/tidb)
  - TiDB v5
  - 蚕食 **MySQL/PostgreSQL** & **HTAP**

### Service runtime

* [Dapr v1.0](https://github.com/dapr/dapr)
  - 多点行业案例吧
  - 替代 Spring boot & cloud 的不会是另一个 Web framework

### Language

* [Go2 Beta?](https://github.com/golang/go/milestone/175)
  - Proposals 冻结
* [Go - support HTTP/3](https://github.com/golang/go/issues/32204)
* [Go ORM - facebook/ent v1](https://github.com/facebook/ent)

* [WebAssembly/WASI](https://github.com/WebAssembly/WASI)

* Python3 as default (Ubuntu, MacOS)
* Python 3.11 release

### Serverless

* Workflow: https://cloud.google.com/workflows
  - https://help.aliyun.com/product/113549.html
* Database: https://cloud.google.com/firestore
  - Aliyun HBase, MongoDB, Lindorm Serverless 版

### Network

* [HTTP/3 正式发布](https://tools.ietf.org/html/draft-ietf-quic-http-32)

------------------

## 2020 Events

* 个人的 技术思维从 `偏改革` 走向 `偏改良`
* **更加关注** 逐步迭代完善, 而不是 **过分追求** 一开始就设计完美
* [TiDB: A Raft-based HTAP Database](http://www.vldb.org/pvldb/vol13/p3072-huang.pdf)

```
8月31日 - 9月4日, 第46届 VLDB 会议以线上直播的方式举行,
PingCAP 团队的论文 "TiDB: A Raft-based HTAP Database" 入选 VLDB 2020
成为业界第一篇 Real-time HTAP 分布式数据库工业实现的论文
```

## 2020 Serverless & WebAssembly (lockdown in 2019-12-12)

* [WASI: WebAssembly System Interface](https://wasi.dev)
  - Best runtime
  - [wasi.dev](https://wasi.dev)
  - [Github: WebAssembly/WASI](https://github.com/WebAssembly/WASI)
  - [Node.js WASI](https://github.com/nodejs/wasi)
  - `LLVM 8`: the WebAssembly target is now built by default
* [WebAssembly Interface Types Spec](https://github.com/WebAssembly/interface-types)
* [QUIC to HTTP/3](https://quicwg.org)
  - Best network protocol
  - [Github: quicwg/base-drafts](https://github.com/quicwg/base-drafts)
* Cloud Platform: Azure, GCP
  - GCP: PubSub, Functions, BigQuery, DataFlow, AI Platform
* [Prisma](https://www.prisma.io)
  - Replaces traditional ORMs
  - Cross projects domain models
  - Cross languages ORMs
  - GraphQL (PSL: Prisma Schema Language)
  - Serverless

------------------

## 2019 (lockdown in 2018-12-14)

* Keywords: `GraphQL`, `Serverless`, `Webassembly`

### Maybe

* [Kotlin will continue up](https://kotlinlang.org)
* [Elixir ecosystem](https://hexdocs.pm)
  - Elixir: `2.0`
  - Phoenix: `2.0`
* [Go 2 designs](https://golang.org/s/go2designs)
* [Istio: ready for production](https://istio.io/about/feature-stages)

### Go places

* [Spring boot will lead micro services ecosystem](https://spring.io)
* [HTTP/3 - HTTP over QUIC](https://tools.ietf.org/html/draft-ietf-quic-http-16)
* [Envoy supports QUIC](https://github.com/envoyproxy/envoy/projects/2)
* [GraphQL Foundation](https://gql.foundation)
* [Serverless](https://github.com/cncf/wg-serverless)
* [Chromium & Safari to be the only browsers](https://github.com/MicrosoftEdge/MSEdge)
* [CSS - Houdini](https://ishoudinireadyyet.com)
* [Webassembly](https://webassembly.org)
* [TC39 - Protocol](https://github.com/michaelficarra/proposal-first-class-protocols)

### To be completed

* [Kubernetes 1.14](https://github.com/kubernetes/kubernetes/milestone/41)
* [TypeScript 3.3](https://github.com/Microsoft/TypeScript/milestone/79)
* [Envoy 1.9](https://github.com/envoyproxy/envoy/milestone/8)
* [TC39 - Pipeline operator](https://github.com/tc39/proposal-pipeline-operator)
* [TC39 - Pattern matching](https://github.com/tc39/proposal-pattern-matching)
* [TC39 - do expression](https://github.com/tc39/proposal-do-expressions)
* [TC39 - Slice notation](https://github.com/tc39/proposal-slice-notation)
* [TC39 - Optional chaining](https://github.com/tc39/proposal-optional-chaining)
* [TC39 - Partial application](https://github.com/tc39/proposal-partial-application)
