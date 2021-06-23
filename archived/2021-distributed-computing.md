---
title: (2021) Distributed computing
description: 浩浩乎如冯虚御风, 而不知其所止; 飘飘乎如遗世独立, 羽化而登仙.
date: 2021-02-21
---

* 在一个完全异步的分布式系统里, 如果至少有一台机器可能会出故障, 则不存在非随机的共识算法.

```
1. 机器故障
2. 完全异步

分布式系统

1. 分布式系统 至少由 3 台机器组成
2. 每台机器都有 初始状态 (State)
3. 分布式系统是一个封闭系统, 没有外界输入

共识

1. 终止性 termination
2. 一致性 agreement
3. 有效性 validity

消息

1. 消息的发送是异步的, 即: 发送了一条消息后, 不一定能收到 Ack
2. 收到消息的时间间隔没有任何假设
3. 消息系统本身的运行是完美的
4. 所有消息只会被处理一次
5. 消息的接收是异步的, 即: 消息的接收顺序是完全随机的
```

|            | 拜占庭容错 | 一致性 |  性能  | 可用性 |
| ---------- |:--------:|:-----:|:------:|:-----:|
|     2PC    |    N     |  强   |        |       |
|     TCC    |    N     |  最终 |        |       |
|     Raft   |    N     |  强   |        |       |
|    Gossip  |    N     |  最终 |    H   |   H   |
| Quorum NWR |    N     |  强   |        |       |
|     PBFT   |    Y     |       |        |       |
|     PoW    |    Y     |       |        |       |

* [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)
  - C -> ACID
  - A -> Base

```
CAP 由三个性质组成

一致性 Consistency
可用性 Availability
分区容错性 Partition tolerance

分区容错性: 网络出现了问题, 把原本通过网络连接在一起的机器分成了几个独立的部分, 即: 脑裂

CAP 的假设是: 当出现了脑裂后, 你只能在一致性和可用性当中选择一个, 即: 只能选择 CP 或者 AP

CAP 的一致性指的是 可线性化 (Linearizability)

线性一致性 (Linearizability)

可串行化 (Serializability)
两个事务里所有操作的执行结果等价于这两个事务的某一个顺序执行结果

严格可串行化 (Strict Serializability)
两个事务的运行结果等价于唯一一个顺序执行结果
正确性极强
运行效率极低

一致性
1. 单调写一致
2. 单调读一致
3. 自读自写
4. 先读后写
```

* [The Raft Consensus Algorithm](https://raft.github.io)

```
Raft 的设计目标是 强一致性 (线性一致性)
Raft 可以提供 强一致性, 也可以提供 最终一致性
```

* [Gossip](https://en.wikipedia.org/wiki/Gossip_protocol)

```
1. 直接邮寄 (Direct Mail)
2. 反熵 (Anti-entropy)
3. 谣言传播 (Rumor mongering)

反熵: 集群中的节点, 每隔段时间就随机选择某个其他节点,
然后通过互相交换自己的所有数据来消除两者之间的差异, 实现数据的最终一致性

谣言传播: 当一个节点有了新数据后, 这个节点变成活跃状态,
并周期性地联系其他节点向其发送新数据, 直到所有的节点都存储了该新数据
```

* **BASE** 实现最终一致性的具体方式
  - 读时修复: 在读取数据时, 检测数据的不一致, 进行修复
  - 写时修复: 在写入数据时, 检测数据的不一致, 进行修复
  - 异步修复: 定时对账检测副本数据的一致性, 并修复

* Snapshot
  - [An example run of the Chandy-Lamport snapshot algorithm](http://composition.al/blog/2019/04/26/an-example-run-of-the-chandy-lamport-snapshot-algorithm/)

```
Chandy-Lamport snapshot algorithm

It turns out to be important that the channels have FIFO behavior
for the Chandy-Lamport algorithm to work.

One of the especially cool things about the Chandy-Lamport algorithm
is that it is decentralized — any process (or multiple processes at once!)
can begin taking a snapshot without coordinating with other processes.
```

------------------

## Streaming computing

* [Differential dataflow](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/01/differentialdataflow.pdf)
  - **Incremental computation**
  - [Naiad](https://github.com/MicrosoftResearch/Naiad)
  - Naiad 可惜了 :)
  - **LINQ** 也是 (Language Integrated Query)

* [Naiad: A Timely Dataflow System](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/11/naiad_sosp2013.pdf)

```
A Naiad application that supports real-time queries
on continually updated data.
The dashed rectangle represents iterative processing that
incrementally updates as new data arrive.
```

```
Naiad is a distributed system for executing data parallel,
cyclic dataflow programs.
It offers the high throughput of batch processors,
the low latency of stream processors,
and the ability to perform iterative and incremental computations.
```

```
1. structured loops allowing feedback in the dataflow,
2. stateful dataflow vertices capable of consuming and
   producing records without global coordination, and
3. notifications for vertices once they have received all
   records for a given round of input or loop iteration.
```

```
Timely dataflow is a computational model based on a
directed graph in which stateful vertices send and
receive logically timestamped messages along directed edges.
The dataflow graph may contain nested cycles,
and the timestamps reflect this structure in order to
distinguish data that arise in different input epochs and loop iterations.
```

```
Timely dataflow graphs are directed graphs with the constraint that
the vertices are organized into possibly nested loop contexts,
with three associated system-provided vertices.
Edges entering a loop context must pass through an
ingress vertex and edges leaving a loop context must
pass through an egress vertex. Additionally,
every cycle in the graph must be contained entirely within some loop context,
and include at least one feedback vertex that is not
nested within any inner loop contexts.
```

```
Each Naiad worker is responsible for delivering messages
and notifications to vertices in its
partition of the timely dataflow graph.
```

* [Streaming 101: The world beyond batch](https://www.oreilly.com/radar/the-world-beyond-batch-streaming-101/)
* [Streaming 102: The world beyond batch](https://www.oreilly.com/radar/the-world-beyond-batch-streaming-102/)
  - 看了果断买了书 [Streaming Systems](https://book.douban.com/subject/27080632/)

* [The Dataflow Model](https://research.google.com/pubs/archive/43864.pdf)

```
The Dataflow Model:
A Practical Approach to
Balancing Correctness,
Latency, and
Cost in Massive-Scale,
Unbounded,
Out-of-Order
Data Processing

A windowing model which supports
unaligned event-time windows,
and a simple API for their creation and use

A triggering model that binds the output times of results to runtime characteristics of the pipeline,
with a powerful and flexible declarative API for describing desired triggering semantics

An incremental processing model that
integrates retractions and updates into the windowing and
triggering models described above

Common Windowing Patterns

1. Fixed (tumbling windows)
2. Sliding
3. Sessions

Time Domains

1. Event Time
2. Processing Time

Windowing

Window Assignment
which assigns the element to zero or more windows.
From the model's perspective, window assignment
creates a new copy of the element in each of the windows
to which it has been assigned.

Window Merging
which merges windows at grouping time.
This allows data-driven windows to be constructed over time
as data arrive and are grouped together.

For any given windowing strategy, the two operations are intimately related;
sliding window assignment requires sliding window merging,
sessions window assignment requires sessions window merging, etc.
Note that, to support event-time windowing natively,
instead of passing (key, value) pairs through the system,
we now pass (key, value, event time, window) 4-tuples.
Elements are provided to the system with event-time timestamps,
and are initially assigned to a default global window,
covering all of event time,
providing semantics that match the defaults in the standard batch model.

Windowing determines where in event time
data are grouped together for processing.
Triggering determines when in processing time
the results of groupings are emitted as panes.
```

------------------

# Timeline

------------------

## 2021

* [The Netflix Cosmos Platform](https://netflixtechblog.com/the-netflix-cosmos-platform-35c14d9351ad)

* [Introduction to Lock-Free Data Structures](https://www.baeldung.com/lock-free-programming)

```
1. Obstruction-Free
2. Lock-Free
3. Wait-Free

Lock (Block) vs Starvation
```

* CAS

```
1. CAS (compare-and-swap)

CAS is an atomic operation, which means that
fetch and update together are one single operation.

Furthermore, compare-and-swap does not prevent the A-B-A problem

2. Load-Link/Store-Conditional

AtomicStampedReference

3. Fetch and Add

Again, the important point is that the operation happens atomically,
which means no other thread can interfere.
```

* [How Alibaba is using Dapr](https://blog.dapr.io/posts/2021/03/19/how-alibaba-is-using-dapr)

* 3月16日, `混合云第一股` `青云科技` 正式在科创板上市, 股票代码: `688316`

* [A visual guide to Dapr](https://blog.dapr.io/posts/2021/03/02/a-visual-guide-to-dapr)

* [Announcing Dapr v1.0](https://blog.dapr.io/posts/2021/02/17/announcing-dapr-v1.0)
  - [Dapr 1.0.0](https://github.com/dapr/dapr/releases/tag/v1.0.0)
