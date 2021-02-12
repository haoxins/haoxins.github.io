---
title: Data infrastructure
description: 回首向来萧瑟处, 归去, 也无风雨也无晴
date: 2020-11-03
---

------------------

## Flink

* Chandy-Lamport
  - https://zhuanlan.zhihu.com/p/44454670
  - http://composition.al/blog/2019/04/26/an-example-run-of-the-chandy-lamport-snapshot-algorithm/

* SQL
  - Rowtime 列在经过窗口操作后, 其 Event Time 属性将丢失
  - https://help.aliyun.com/document_detail/62510.html

```
Window (If 5min)
  TUMBLE [0, 5) [5, 10) [10, 15)
  HOP - Sliding Window
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE)
    update every 30s, win size 1min
  SESSION

Over
  Row Over (ROWS BETWEEN)
  1 Row -> 1 Window, the row is the last row in the window
  Range Over (RANGE BETWEEN)
```

### Architecture

* JobManager -> Master process
  - JobGraph -> ExecutionGraph
* TaskManager -> Worker process
  - Job task slot
* ResourceManager
  - Kubernetes
* Dispatcher
  - Web UI
  - Rest API

------------------

## History

* **Flink v1.13**

* NumPy 1.20.0
  - https://github.com/numpy/numpy/releases/tag/v1.20.0

```
The Python versions supported for this release are 3.7-3.9
Annotations for NumPy functions
Preliminary support for the upcoming Cython 3.0
```

* **Flink v1.12**

```
Before 1.12
  batch (DataSet API) and streaming (DataStream API)

After 1.12
  The DataSet API will be deprecated
```

* 2020-12-10 Flink 1.12
  - https://flink.apache.org/news/2020/12/10/release-1.12.0.html

```
Release Highlights

The community has added support for efficient batch execution in the DataStream API.

The default stream time characteristic has been changed to EventTime.

Kubernetes-based High Availability (HA) was implemented as an alternative to ZooKeeper for highly available production setups.
```
