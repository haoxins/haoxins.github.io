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

* [Apache Flink 1.14.0 Release Announcement](https://flink.apache.org/news/2021/09/29/release-1.14.0.html)
  - Flink now supports taking *checkpoints* of applications
    that are partially running and partially finished
    (some operators reached the end of the bounded inputs).
    Additionally, bounded streams now take a final checkpoint
    when reaching their end to ensure smooth
    committing of results in sinks.
  - The batch execution mode now supports programs that
    use a mixture of the `DataStream API` and the `SQL/Table API`
    (previously only pure `Table/SQL` or `DataStream` programs).
  - We are removing the *old SQL execution engine* and
    are removing the active integration with *Apache Mesos*.

* **env.pid.dir**
  - default: `/tmp`
  - Defines the directory where the `flink-<host>-<process>.pid` files are saved
  - 遇到的问题: 重启不干净, 导致 Cluster 不健康

```
Caused by:
  org.apache.flink.util.FlinkRuntimeException:
  java.nio.file.NoSuchFileException:
  /tmp/flink-netty-shuffle-*.channel

Diagnostics java.net.BindException:
  Could not start actor system on any port in port range 6123

The stop script relies on the file `flink-<host>-<process>.pid`.
If that file somehow gets cleanup up occasionally,
the stop script can't find the process identifiers
inside that file to kill the processes.
```

* [Apache Flink 1.13.0 Release Announcement](https://flink.apache.org/news/2021/05/03/release-1.13.0.html)

```
The release brings us a big step forward in one of our major efforts:

Making Stream Processing Applications as natural and as simple
to manage as any other application.

The new reactive scaling mode means that scaling streaming
applications in and out now works like in any other application
by just changing the number of parallel processes.

The release also prominently features a series of improvements
that help users better understand the performance of applications.

Load and backpressure visualization to identify bottlenecks,
CPU flame graphs to identify hot code paths in your application,
and State Access Latencies to see how the State Backends are keeping up.

Unaligned Checkpoints - production-ready
```

* [A Python 3 implementation built on GraalVM](https://github.com/oracle/graalpython)
  - 期待 **PyFlink** 引入

* [How to natively deploy Flink on Kubernetes with High-Availability (HA)](https://flink.apache.org/2021/02/10/native-k8s-with-ha.html)

* Window, Trigger, Watermark

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

* Checkpoint, Savepoint

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

* Streaming, Windowing joins

### Kafka

* [What's New in Apache Kafka 3.0.0](https://www.confluent.io/blog/apache-kafka-3-0-major-improvements-and-new-features/)
  - While **`KRaft`** is not yet recommended for production,
    we have made many improvements to
    the **`KRaft`** metadata and APIs.
  - Starting with Apache Kafka 3.0, the producer enables
    the strongest delivery guarantees by default
    (**`acks=all`**, *`enable.idempotence=true`*).
  - This means that users now get ordering
    and durability by default.
  - Support for Java 8 is deprecated across all components
    of the Apache Kafka project in 3.0.

* KIP-500: Replace ZooKeeper with a Self-Managed Metadata Quorum

* [Apache Kafka Made Simple: A First Glimpse of a Kafka Without ZooKeeper](https://www.confluent.io/blog/kafka-without-zookeeper-a-sneak-peek/)

* **Kafka 2.8.0**
  - Early access of replace ZooKeeper with a self-managed quorum
  - JSON request/response debug logs
  - Topic identifiers

### DataFusion and Ballista

* [Data Fusion](https://github.com/apache/arrow-datafusion)

```
DataFusion supports both an SQL and a DataFrame API
for building logical query plans as well as a query optimizer
and execution engine capable of parallel execution against
partitioned data sources (CSV and Parquet) using threads.

DataFusion is used to create modern, fast and efficient data pipelines,
ETL processes, and database systems, which need the performance of
Rust and Apache Arrow and want to provide their users the convenience of
an SQL interface or a DataFrame API.
```

* [Ballista 0.5.0 Release](https://arrow.apache.org/blog/2021/08/18/ballista-0.5.0/)
  - Ballista queries can now be executed by calling `DataFrame.collect()`
  - The shuffle mechanism has been *re-implemented*
  - Distributed hash-partitioned joins are now supported
  - Keda autoscaling is supported

* [DataFusion 5.0.0 Release](https://arrow.apache.org/blog/2021/08/18/datafusion-5.0.0/)
  - There have been numerous **performance improvements** in this release.

* [Apache Arrow Rust 5.0.0 Release](https://arrow.apache.org/blog/2021/07/29/5.0.0-rs-release/)
  - [Apache Arrow 5.0.0 (29 July 2021)](https://arrow.apache.org/release/5.0.0.html)
  - Arrow releases major versions every three months.

```
Feature-wise, this release adds:

A new kernel which lexicographically partitions points.

Expanded support for the FFI/C data interface,
easing integration with the broader Arrow ecosystem.

Usability enhancements for creating and manipulating RecordBatches.

Improved usability for Arrow Flight's API.

Slimmer dependency stack when default features are disabled.
```

* [Ballista: A Distributed Scheduler for Apache Arrow (2021-04-12)](https://arrow.apache.org/blog/2021/04/12/ballista-donation/)
  - [Ballista (2021-04-10)](https://github.com/ballista-compute/ballista) has been donated to the Apache Arrow project

> How does this (Ballista) compare to Apache Spark?

```
The choice of Rust as the main execution language means that
memory usage is deterministic and avoids the overhead of GC pauses.

Ballista is designed from the ground up to use `columnar data`,
enabling a number of efficiencies such as vectorized processing
(SIMD and GPU) and efficient compression.

Although Spark does have some columnar support,
it is still largely `row-based` today.

The combination of Rust and Arrow provides excellent memory efficiency
and memory usage can be 5x - 10x lower than Apache Spark
in some cases, which means that more processing can fit on a single node,
reducing the overhead of distributed compute.
```

### Arrow

* [Arrow Columnar Format](https://arrow.apache.org/docs/format/Columnar.html)

* [arrow-rs: Native Rust implementation of Apache Arrow](https://github.com/apache/arrow-rs)

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

* [Parquet](https://github.com/apache/parquet-format)
  - 磁盘存储, 列
* [Avro](https://github.com/apache/avro)
  - 磁盘存储, 行

* [FlatBuffers](https://github.com/google/flatbuffers)
  - Zero copy, IPC
* [Protobuf](https://github.com/protocolbuffers/protobuf)
  - 节省内存, RPC
* [Cap'n Proto](https://github.com/capnproto/capnproto)
  - will die :)

* **FlatBuffers** vs **Protobuf**

|                              | Protobuf | FlatBuffers |
| ---------------------------- |:--------:|:-----------:|
| Zero-copy                    |    no    |     yes     |
| Random-access reads          |    no    |     yes     |
| Initialization order         |    any   |  bottom-up  |
| Usable as mutable state      |    yes   |     no      |
| Padding takes space on wire? |    no    |     yes     |
| Pointers take space on wire? |    no    |     yes     |
