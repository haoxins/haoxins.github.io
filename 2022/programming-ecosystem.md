---
title: Programming ecosystem
description: 风不定, 人初静, 明日落红应满径.
date: 2022-01-17
---

## Data & ML Engineering

- [DataFusion](https://github.com/apache/datafusion)
  - [Ballista](https://github.com/apache/datafusion-ballista)
  - 期待 2023 能带来全新的 Streaming computing 生态
  - `Streaming` vs `Mini batch` vs `Batch`

- [Polars](https://github.com/pola-rs/polars)
  - __Polars__ has transitioned to __Arrow2__.

## Cloud native

- 我的定义:
  - `2022`:
  - `2021`: Cloud native = K8s native + Object storage

------------------

## 2023

- Streaming computing
  - [Fluvio](https://github.com/infinyon/fluvio)
  - [RisingWave](https://github.com/risingwavelabs/risingwave)
  - [Materialize](https://github.com/MaterializeInc/materialize)

---

- Kafka 压缩 gzip vs zstd, 简单的对比:
  - gzip storage: `93` million messages, `41.8` GB
  - zstd storage: `103` million messages, `35.4` GB

## 2022

- [Fluvio](https://github.com/infinyon/fluvio)
  - 基本不会有未来了~

- [K8s: Object Storage Support](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/1979-object-storage-support)

- [Citus 11 for Postgres goes fully open source, with query from any node](https://www.citusdata.com/blog/2022/06/17/citus-11-goes-fully-open-source)
  - https://github.com/citusdata/citus
  - 再次重申看衰 https://github.com/yugabyte/yugabyte-db

- [Ray-2.0.0](https://github.com/ray-project/ray/releases/tag/ray-2.0.0)
  - https://github.com/ray-project/ray/pull/24523
  - `Polars` is significantly faster than the
    current `PyArrow`-based sort.

- `2022-08-20` GitHub 账号升级到了 Pro
  - 每月 `$4`
  - 确实做得不错

- `2022-08-19` Colima
  - container runtimes on macOS (and Linux) with minimal setup
  - [Colima](https://github.com/abiosoft/colima)
  - 用了一段时间, 不喜欢 Rancher Desktop
  - `2023-08-22`, 迁移至 [Podman](https://github.com/containers/podman)

- [HoraeDB](https://github.com/apache/horaedb)
  - 蚂蚁出品, 预料之中, 果然基于 `Arrow`.

- [07-25: Apache Flink Kubernetes Operator 1.1.0 Release](https://flink.apache.org/news/2022/07/25/release-kubernetes-operator-1.1.0.html)
  - [07-06: Apache Flink 1.15.1 Release](https://flink.apache.org/news/2022/07/06/release-1.15.1.html)
  - 准备生产环境部署升级了!
  - 删除 `FlinkDeployment` 之前需要先删除所有相关的 `FlinkSessionJob`

- [Strimzi Kafka Operator](https://github.com/strimzi/strimzi-kafka-operator)
  - 开发环境用起来还蛮方便, 但是远不够 Production Ready!
  - `2022-09`, 同事也搁置了公司内的 Kafka operator 迁移
  - 使用的是 https://github.com/strimzi/strimzi-kafka-operator
  - 对于这个项目的代码实现, 不予置评

- `2022-06-27`, 由于 License 的问题,
  用上了免费的 Rancher Desktop,
  替代 Docker Desktop
  - [Rancher Desktop](https://rancherdesktop.io)
  - [nerdctl](https://github.com/containerd/nerdctl)

- Kafka `3.2.0`, 至少本地开发不需要 __ZooKeeper__ 了

```zsh
./bin/kafka-storage.sh random-uuid
./bin/kafka-storage.sh format -t <uuid> -c ./config/kraft/server.properties
./bin/kafka-server-start.sh ./config/kraft/server.properties
```

- [Ray-1.13.0](https://github.com/ray-project/ray/releases/tag/ray-1.13.0)
  - Python `3.10` support is now in alpha.

- [RFC 9114 - HTTP3](https://www.rfc-editor.org/rfc/rfc9114)

- [RFC: Introducing Ray AI Runtime](https://github.com/ray-project/ray/issues/22488)
  - 2022, 基本可以说 Kubeflow 凉凉了, 偶尔的维护罢了, 毫无社区活力

- [Quickwit](https://github.com/quickwit-oss/quickwit)
  - The new way to manage your logs at any scale
  - Index data persisted on object storage
  - Ingest JSON documents with or without a strict schema
  - Ingest your documents with exactly-once semantics
  - We estimate that Quickwit can be up to
    `10x` cheaper on average than Elastic
  - 真的假的? 等到 2023, 回头再看
  - [Tantivy](https://github.com/quickwit-oss/tantivy)
  - Tantivy is a full-text search engine library written in Rust

- [PyTorch 1.11, TorchData, and functorch are now available](https://github.com/pytorch/pytorch/releases/tag/v1.11.0)
  - 这个 Release Notes 写得真是用心
  - PyTorch 胜, TensorFlow 败

- [xDS API Working Group (xDS-WG)](https://github.com/cncf/xds)
  - 从 2021 年开始, 本人坚定地唱衰 `Nginx`, `Apisix`

- [Rayon](https://github.com/rayon-rs/rayon)
  - Rayon is a data-parallelism library for Rust.
  - It is extremely lightweight and makes it easy to
    convert a sequential computation into a parallel one.
  - It also guarantees data-race freedom.
  - [DataFusion - Morsel-driven Parallelism using rayon](https://github.com/apache/datafusion/pull/2226)

- [Spin](https://github.com/fermyon/spin)
  - Spin is a framework for building, deploying, and running fast,
    secure, and composable cloud microservices with WebAssembly.
  - [WAGI: WebAssembly Gateway Interface](https://github.com/deislabs/wagi)

- `2022-03`
  - 过去 2 个月, 一直在设计, 实现基于 `Flink operator`
    的一个团队内部平台的 `K8s operator`,
    团队内部称为 `Metric platform operator`
  - 基于 `Operator` 模式, 配合 `K8s CRD` 的 `GitOps`,
    实现 `Metric platform` 的一些 `Flink job` 调度和处理
  - 一开始, `Flink operator` 选择
    [spotify/flink-on-k8s-operator](https://github.com/spotify/flink-on-k8s-operator)
  - 因为
    [GCP/flink-on-k8s-operator](https://github.com/GoogleCloudPlatform/flink-on-k8s-operator)
    几乎不维护了
  - 当然, 前者 Fork 自后者
  - 开发进行中的时候, Flink 官方团队也推出了
    [apache/flink-kubernetes-operator](https://github.com/apache/flink-kubernetes-operator)
  - 虽然打乱了原本的计划, 需要重新取舍, 但是整体而言却是重大利好, 理由如下:
  - (1) 对于 Flink on K8s 的趋势是一大推进, 2022 年,
    可能 K8s 会是 Flink 社区第一推荐部署方式.
    这也得感谢阿里云的推动.
  - (2) 我一直认为, 结合 K8s, Flink 未来应该通过 Operator 彻底废除
    Job Manager. 这一想法比较激进, 因为意味着 Flink 将来只能部署在 K8s 上.
    但这个选择会简化 Flink, 使其专注于自己的专长.
  - 总体而言, 先干掉 Job Manager, 再干掉 Flink, 会是我的 2022 的一个重点方向.
  - 为什么要干掉 Flink? 理由后续说明.

- `2022-03`
  - 有同事问我脑海中的技术的 blueprint 是啥样子的?
  - __中心化__: Kubernetes 上面的 `functions/pipelines`
  - 比如:
    Argo workflows,
    Dapr functions,
    Istio plugins,
    Kubernetes operators,
    Kubeflow pipelines
  - __区块链__: 某几个公链的 Smart contracts
  - 我不认为: 私有链, 联盟链有价值!

- `2022-02-28`, 公司隔壁团队终于得到结论:
  - [YugabyteDB](https://github.com/yugabyte/yugabyte-db) 不可用
  - 我先前看了看 Issues, Code, Docs 就早早得出了这个结论.
  - (1) 直接 include PostgreSQL 代码, 且近`2`年未同步.
    所谓的 PostgreSQL 兼容, 过度承诺.
  - (2) 架构不合理, 本质上他们做的不是 DB, 只是围绕 DB 的 Services.
    和 [TiDB](https://github.com/pingcap/tidb) 根本不具备可比性.
  - (3) 过度宣传, 文档的描述不务实. 对比列表, 完胜所有对手, 很假.
  - (4) 根据 GitHub Issues, 不像有较多人在用.

- [Switch DataFusion to using arrow2](https://github.com/apache/datafusion/issues/1532)
  - https://github.com/jorgecarleitao/arrow2
  - https://github.com/jorgecarleitao/parquet2

- 关于 Flink 的替代
  - 首先, Flink 的 Scope 其实和 K8s 是有重叠的;
  - 同时, Flink 的各种历史包袱也很多.
  - 此时, Flink 还没有真正的可替代品;
  - 但大概率会基于
    [DataFusion](https://github.com/apache/datafusion)
  - [Fluvio](https://github.com/infinyon/fluvio)
    的开发力量稍显薄弱
  - [Ballista Future Direction](https://github.com/apache/datafusion-ballista/issues/30)
  - `2022-08`: 放弃!
    Fluvio 进展缓慢, 无望;
    DataFusion, Ballista 发展路线暂不包含 Streaming
  - 准确的说, Flink 的替代者将会是一个生态, 而不是另一个
    `Stateful Computations over Data Streams`
  - [Substrait](https://substrait.io)
  - [Substrait](https://github.com/substrait-io/substrait)
  - Cross-Language Serialization for Relational Algebra

- Spring Boot `3.0.0`
  - Spring Boot `3.0` requires Java 17 as a minimum
    version and Spring Framework 6.
  - Applications built with Gradle require
    Gradle `7.3` or later.
  - 2022 年开始, 我基本脱离 `JVM/Java/Kotlin` 了
  - 除了 Flink 相关, 至少远离 Spring 了
  - 所以, Spring Boot 3, 与我无关
  - 哈哈哈, 开心

- [Kubeflow pipelines v1.8.0](https://github.com/kubeflow/pipelines/blob/1.8.0/CHANGELOG.md)
  - __BREAKING CHANGES__
  - Use Argo Emissary Executor instead of Docker by default.
  - `sdk.v2`: Block task dependency referencing tasks
    inside a sibling condition or loop group.
  - `sdk`: Deprecate `V2 compatible mode` in v1 compiler.
  - `sdk.v2`: Merge v2 experimental change back to v2 namespace.
  - 可以 `non-prod` 环境先试试水了
