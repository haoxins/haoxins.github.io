---
title: Data engine
description: 回首向来萧瑟处, 归去, 也无风雨也无晴
date: 2020-11-03
---

## Serialization

* [Cap'n Proto](https://github.com/capnproto/capnproto)
  - :)
* [FlatBuffers](https://github.com/google/flatbuffers)
  - Zero copy, IPC
* [Protobuf](https://github.com/protocolbuffers/protobuf)
  - 节省内存, RPC

* [Parquet](https://github.com/apache/parquet-format)
  - 磁盘存储, 列
* [Avro](https://github.com/apache/avro)
  - 磁盘存储, 行

## KV 存储

* RocksDB
  - LSM 树
  - 基本的 KV 查询能力
  - 很高的 文件数据 写入速度

* [TiKV](https://github.com/tikv/tikv)
  - LSM 树
  - TiFlash (B+ 树)

------------------

# Timeline

------------------

## 2021

### Flink

* Window

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

* Checkpoint

```
When working with state kept in a heap-based state backend,
accesses and updates involve reading and writing objects on the heap.
But for objects kept in the RocksDBStateBackend,
accesses and updates involve serialization and deserialization,
and so are much more expensive.
But the amount of state you can have with RocksDB is limited
only by the size of the local disk.
Note also that only the RocksDBStateBackend is able to do incremental snapshotting, which is a significant benefit for applications
with large amounts of slowly changing state.
```

* [How to natively deploy Flink on Kubernetes with High-Availability (HA)](https://flink.apache.org/2021/02/10/native-k8s-with-ha.html)

------------------

## 2020

### Flink

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

* [Stateful Functions Internals: Behind the scenes of Stateful Serverless](https://flink.apache.org/news/2020/10/13/stateful-serverless-internals.html)
