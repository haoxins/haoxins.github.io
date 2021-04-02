---
title: Data engine
description: 回首向来萧瑟处, 归去, 也无风雨也无晴
date: 2020-11-03
---

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

* [How to natively deploy Flink on Kubernetes with High-Availability (HA)](https://flink.apache.org/2021/02/10/native-k8s-with-ha.html)

* Window, Watermark

```
Window (If 5min)
  TUMBLE [0, 5) [5, 10) [10, 15)
  HOP - Sliding Window
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE)
    update every 30s, window size 1min
  SESSION

Over
  Row Over (ROWS BETWEEN)
  1 Row -> 1 Window, the row is the last row in the window
  Range Over (RANGE BETWEEN)
```

```
Once a watermark reaches an operator,
the operator can advance its internal event time
clock to the value of the watermark.

Each parallel subtask of a source function
usually generates its watermarks independently.

Some operators consume multiple input streams; a union, for example,
or operators following a keyBy() or partition() function.
Such an operator's current event time is the
minimum of its input streams' event times.

Sliding window assigners can create lots of window objects,
and will copy each event into every relevant window.
For example, if you have sliding windows
every 15 minutes that are 24-hours in length,
each event will be copied into 4 * 24 = 96 windows.

Windows are only created when events are assigned to them.
So if there are no events in a given time frame,
no results will be reported.

1. Specify whether your stream is keyed or not
2. Define a window assigner
  - tumbling windows
  - sliding windows
  - session windows
  - global windows
  - custom window (WindowAssigner)
3. Specify the computation that we want to perform on each of these windows
  - ReduceFunction
  - AggregateFunction
  - ProcessWindowFunction

Time-based windows have a start timestamp (inclusive)
and an end timestamp (exclusive) that together
describe the size of the window.

When watermarks arrive at the window operator this triggers two things:
1. the watermark triggers computation of all windows
  where the maximum timestamp (which is end-timestamp - 1)
  is smaller than the new watermark
2. the watermark is forwarded to downstream operations

A Trigger determines when a window (as formed by the window assigner)
is ready to be processed by the window function.

Flink allows to specify a maximum allowed lateness for window operators.
(default value is 0)

Elements that arrive after the watermark has passed the end of the window
but before it passes the end of the window plus the allowed lateness,
are still added to the window. Depending on the trigger used,
a late but not dropped element may cause the window to fire again.

In order to make this work, Flink keeps the state of windows
until their allowed lateness expires.
```

```
Window
  * Watermark
  * Trigger
    - TriggerResult(boolean fire, boolean purge)
    - CONTINUE: do nothing
    - FIRE: trigger the computation
    - PURGE: clear the elements
    - FIRE_AND_PURGE: trigger the computation and clear the elements
  * Evictor
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
Note also that only the RocksDBStateBackend is able to do incremental snapshotting,
which is a significant benefit for applications
with large amounts of slowly changing state.
```

### Kafka

* KIP-500: Replace ZooKeeper with a Self-Managed Metadata Quorum

```
Raft
```

### JDK 17 (LTS)

* [ZGC | What's new in JDK 16](https://malloc.se/blog/zgc-jdk16)

### Others

* [Old blog - Random notes on improving the Redis LRU algorithm](http://antirez.com/news/109)
* [Old blog - Redis persistence demystified](http://oldblog.antirez.com/post/redis-persistence-demystified.html)

* [Announcing the Deno Company](https://deno.com/blog/the-deno-company)

```
A Globally Distributed JavaScript VM

Deno Deploy is a distributed system that runs JavaScript, TypeScript, and WebAssembly
at the edge, worldwide. The service deeply integrates the V8 JavaScript runtime
with a high performance asynchronous web server to provide
optimal performance without unnecessary intermediate abstractions.

不看好
```

* [Argo Workflows](https://github.com/argoproj/argo-workflows)
  - [Argo Workflows](https://argoproj.github.io/argo-workflows)
  - 有点意思, 期待成为主流

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

### Serialization

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
