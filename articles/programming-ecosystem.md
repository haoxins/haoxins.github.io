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

## GUI

* [Slint](https://github.com/slint-ui/slint)
  - 替代 `Qt`

------------------

## 2022

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
