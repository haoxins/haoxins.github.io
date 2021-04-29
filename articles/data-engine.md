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

### Argo

* [Argo Project](https://github.com/argoproj)
  - [Argo Workflows](https://github.com/argoproj/argo-workflows)
  - 有点意思, 期待成为主流

### Arrow

* [arrow-rs: Native Rust implementation of Apache Arrow](https://github.com/apache/arrow-rs)

* [Ballista: A Distributed Scheduler for Apache Arrow (2021-04-12)](https://arrow.apache.org/blog/2021/04/12/ballista-donation/)
  - [Ballista (2021-04-10)](https://github.com/ballista-compute/ballista) has been donated to the Apache Arrow project

### Flink

* [A Python 3 implementation built on GraalVM](https://github.com/oracle/graalpython)
  - 期待 **PyFlink** 引入

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

* [Apache Kafka Made Simple: A First Glimpse of a Kafka Without ZooKeeper](https://www.confluent.io/blog/kafka-without-zookeeper-a-sneak-peek/)

* **Kafka 2.8.0**
  - Early access of replace ZooKeeper with a self-managed quorum
  - JSON request/response debug logs
  - Topic identifiers

### JDK 17 (LTS)

* [ZGC | What's new in JDK 16](https://malloc.se/blog/zgc-jdk16)

### Others

* [What's New in TiDB 5.0](https://docs.pingcap.com/zh/tidb/stable/release-5.0.0)

```
TiDB 通过 TiFlash 节点引入了 MPP 架构.
这使得大型表连接类查询可以由不同 TiFlash 节点共同分担完成.
经测试, TiDB 5.0 在同等资源下, MPP 引擎的总体性能是 Greenplum 6.15.0 与 Apache Spark 3.1.1
两到三倍之间, 部分查询可达 8 倍性能差异.

引入聚簇索引功能, 提升数据库的性能. 例如, TPC-C tpmC 的性能提升了 39%.
开启异步提交事务功能, 降低写入数据的延迟.
引入 Raft Joint Consensus 算法, 确保 Region 成员变更时系统的可用性.
优化 EXPLAIN 功能, 引入不可见索引等功能帮助提升 DBA 调试及 SQL 语句执行的效率.
提升从 Amazon S3 或者 TiDB/MySQL 导入导出数据的性能.
```

* [Old blog - Random notes on improving the Redis LRU algorithm](http://antirez.com/news/109)
* [Old blog - Redis persistence demystified](http://oldblog.antirez.com/post/redis-persistence-demystified.html)

* [Announcing the Deno Company](https://deno.com/blog/the-deno-company)

```
A Globally Distributed JavaScript VM

Deno Deploy is a distributed system that runs JavaScript, TypeScript, and WebAssembly
at the edge, worldwide. The service deeply integrates the V8 JavaScript runtime
with a high performance asynchronous web server to provide
optimal performance without unnecessary intermediate abstractions.
```

------------------

## 2020

* [A Snowflake deep dive](https://hhhypergrowth.com/a-snowflake-deep-dive/)

```
Extract, Load & Transform (ELT) = Changing the ETL process
to eliminate needing a staging area.
The load ("L") is done before the transform ("T"), meaning
all of the raw data is now directly loaded into the Data Lake,
which can then serve as the staging area to
further refine the data from there, using SQL-based tooling.

In AWS, is using EC2 compute over S3 storage,
acting somewhat akin to (aka competes against) AWS Athena
or the MongoDB Atlas Data Lake service.

In Azure, it utilizes Azure Compute over Azure Blob Storage.
They also recently added support for the new
Azure Data Lake Storage format (ADLS Gen2).

On Google Cloud, it uses Google Compute Engine (GCE)
over Google Cloud Storage (GCS).

Single Copy of Data
One huge benefit of a Data Lakehouse is that
all the raw data can be utilized further,
directly within the database.
An analyst can be saving queries into new refined datasets
for BI tools to take advantage of.
A data broker can be directly isolating datasets
to share or publish or monetize.

"One Copy of Data, Many Workloads".
```

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
