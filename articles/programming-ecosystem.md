---
title: Programming ecosystem
description: 风不定, 人初静, 明日落红应满径.
date: 2022-01-17
---

## ML Engineering

> 此处特指: Engineering

* [Arrow](https://github.com/apache/arrow)
  - [Polars](https://github.com/pola-rs/polars)

* [Ray](https://github.com/ray-project/ray)

## ML

* JupyterLab `v4`

## WASM & WASI

* [WASI](https://wasi.dev)
  - https://github.com/WebAssembly/WASI
  - https://github.com/bytecodealliance/wasi

* [Krustlet](https://github.com/krustlet/krustlet)
  - Kubernetes Kubelet in Rust for running WASM

## Cloud native

* 我的定义:
  - `2021`: Cloud native = K8s native + Object storage

------------------

## 2022

* [Spin](https://github.com/fermyon/spin)
  - Spin is a framework for building, deploying, and running fast,
    secure, and composable cloud microservices with WebAssembly.
  - [WAGI: WebAssembly Gateway Interface](https://github.com/deislabs/wagi)

* [Google Cloud](https://cloud.google.com) 是真不行!
  - 哎~

* `2022-03`
  - 过去 `2` 个月, 一直在 `设计 & 实现` 基于 `Flink operator`
    的一个团队内部平台的 `K8s operator`,
    团队内部称为 `Metric platform operator`
  - 基于 `Operator` 模式, 配合 `K8s CRD` 的 `GitOps`,
    实现 `Metric platform` 的一些 `Flink job` 调度和处理
  - 一开始, `Flink operator` 选择
    [spotify/flink-on-k8s-operator](https://github.com/spotify/flink-on-k8s-operator)
  - 因为
    [GCP/flink-on-k8s-operator](https://github.com/GoogleCloudPlatform/flink-on-k8s-operator)
    几乎不维护了
  - 当然, 前者 `Fork` 自后者
  - 开发进行中的时候, `Flink` 官方团队也推出了
    [apache/flink-kubernetes-operator](https://github.com/apache/flink-kubernetes-operator)
  - 虽然打乱了原本的计划, 需要重新取舍, 但是整体而言却是**重大利好**, 理由如下:
  - (1) 对于 `Flink on K8s` 的趋势是一大推进, `2022` 年,
    可能 `K8s` 会是 `Flink` 社区第一推荐部署方式.
    这也得感谢*阿里云*的推动.
  - (2) 我一直认为, 结合 `K8s`, `Flink` 未来应该通过 `Operator` 彻底废除
    `Job Manager`. 这一想法比较激进, 因为意味着 `Flink` 将来只能部署在 `K8s` 上.
    但这个选择会简化 `Flink`, 使其专注于自己的专长.
  - 总体而言, 先干掉 `Job Manager`, 再干掉 `Flink`, 会是我的 `2022` 的一个重点方向.
  - 为什么要干掉 `Flink`? 理由后续说明.

* `2022-03`
  - 有同事问我脑海中的技术的 `blueprint` 是啥样子的?
  - **中心化**: `Kubernetes` 上面的 `functions/pipelines`
  - 比如:
    `Argo workflows`,
    `Dapr functions`,
    `Istio plugins`,
    `Kubernetes operators`,
    `Kubeflow pipelines`
  - **去中心化**: 某几个公链的 `Smart contracts`
  - 我不认为: `私有链`, `联盟链`有价值!

* `2022-02-28`, 公司隔壁团队终于得到结论:
  - [YugabyteDB](https://github.com/yugabyte/yugabyte-db) 不可用
  - 我先前看了看 Issues, Code, Docs 就早早得出了这个结论.
  - 1) 直接 include PostgreSQL 代码, 且近`2`年未同步.
    所谓的 PostgreSQL 兼容, 过度承诺.
  - 2) 架构不合理, 本质上他们做的不是 DB, 只是围绕 DB 的 Services.
    和 [TiDB](https://github.com/pingcap/tidb) 根本不具备可比性.
  - 3) 过度宣传, 文档的描述不务实. 对比列表, 完胜所有对手, 很假.
  - 4) 根据 GitHub Issues, 不像有较多人在用.

* 关于 `Flink` 的替代
  - 首先, `Flink` 的 *Scope* 其实和 `K8s` 是有重叠的;
  - 同时, `Flink` 的各种历史包袱也很多.
  - 此时, `Flink` 还没有真正的可替代品;
  - 但大概率会基于
    [DataFusion](https://github.com/apache/arrow-datafusion)
  - [Fluvio](https://github.com/infinyon/fluvio)
    的开发力量稍显薄弱

* Spring Boot `3.0.0`
  - Spring Boot `3.0` requires Java `17` as a minimum
    version and Spring Framework `6`.
  - Applications built with Gradle require
    Gradle `7.3` or later.
  - `2022` 年开始, 我基本脱离 `JVM/Java/Kotlin` 了
  - 除了 `Flink` 相关, 至少远离 `Spring` 了
  - 所以, Spring Boot `3`, 与我无关
  - 哈哈哈, 开心

* [Kubeflow pipelines v1.8.0](https://github.com/kubeflow/pipelines/blob/1.8.0/CHANGELOG.md)
  - **BREAKING CHANGES**
  - Use Argo Emissary Executor instead of Docker by default.
  - `sdk.v2`: Block task dependency referencing tasks
    inside a sibling condition or loop group.
  - `sdk`: Deprecate `V2 compatible mode` in v1 compiler.
  - `sdk.v2`: Merge v2 experimental change back to v2 namespace.
  - 可以 `non-prod` 环境先试试水了

* **Kubeflow** 的社区问题!
  - `2021` 年, 我个人对 [Kubeflow](https://github.com/kubeflow/kubeflow) 社区的评价较差
  - 几乎处于**无人维护**的状态
  - [Training operator](https://github.com/kubeflow/training-operator)
  - [Kubeflow pipelines](https://github.com/kubeflow/pipelines)
  - 等子项目还稍微好些
  - 或许该思考下如何重新组装 `Kubeflow` 了
  - [MLflow](https://github.com/mlflow)
  - [Ray](https://github.com/ray-project)
  - 是不错的候选, 尤其是 **Ray**
