---
title: Data infrastructure notes
description: Apache Spark, Flink and more
date: 2020-11-03
---

* Chandy-Lamport
  - https://zhuanlan.zhihu.com/p/44454670
  - http://composition.al/blog/2019/04/26/an-example-run-of-the-chandy-lamport-snapshot-algorithm/

### History

* Flink

```
Before 1.12
  batch (DataSet API) and streaming (DataStream API)

The DataSet API will be deprecated

In Flink 1.12, the default execution mode is STREAMING
```

* 2020-12-10 Flink 1.12
  - https://flink.apache.org/news/2020/12/10/release-1.12.0.html

```
Release Highlights

The community has added support for efficient batch execution in the DataStream API.

Kubernetes-based High Availability (HA) was implemented as an alternative to ZooKeeper for highly available production setups.
```
