---
title: Distributed computing
description: 浩浩乎如冯虚御风, 而不知其所止; 飘飘乎如遗世独立, 羽化而登仙.
date: 2021-02-21
---

* [Peter Bailis, Highly Available, Seldom Consistent](http://www.bailis.org/blog/)
  - Data management, distributed systems, and beyond
  - [Linearizability versus Serializability](http://www.bailis.org/blog/linearizability-versus-serializability/)
  - [Non-blocking Transactional Atomicity](http://www.bailis.org/blog/non-blocking-transactional-atomicity/)
  - [HAT, not CAP: Introducing Highly Available Transactions](http://www.bailis.org/blog/hat-not-cap-introducing-highly-available-transactions/)

------------------

* 在一个完全异步的分布式系统里,
  如果至少有一台机器可能会出故障,
  则不存在非随机的共识算法.

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
is that it is decentralized - any process (or multiple processes at once!)
can begin taking a snapshot without coordinating with other processes.
```

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

## 2022

- 在研究机构 `Gartner` 最新出炉的 `2021` 全球云计算 `IaaS` 市场份额的数据中,
  阿里云排在全球第三, 仅次于美国云计算巨头亚马逊和微软, 谷歌则排在第四位.
  - `Gartner` 数据还显示, 阿里云长期居于亚太市场份额第一.
  - 个人观点: __谷歌云, 不行!__

## 2021

### Events

* [gRPC Proxyless Service Mesh](https://istio.io/latest/blog/2021/proxyless-grpc/)
  - Introduction to Istio support for gRPC's
    proxyless service mesh features.
  - Istio 1.11 adds experimental support for
    adding gRPC services directly to the mesh.

* [X.1011: Guidelines for continuous protection of the service access process](https://www.itu.int/rec/T-REC-X.1011-202110-I)
  - **Authentication**: Formalized process of verification that,
    if successful, results in an authenticated
    identity for an entity.
  - Use of the term *authentication* in an
    identity management (**IdM**) context is
    taken to mean *entity authentication*.
  - **Authorization**: The granting of rights and,
    based on these rights, the granting of access.

* 市场研究机构 Canalys 公布的数据显示, 截止 2020 年 Q4,
  在全球云服务市场, 排名前四的是*亚马逊云服务* (AWS),
  *微软* Azure, *谷歌云* (Google Cloud) 和*阿里云*.
* 根据 Canalys 的数据报告, 2020 年四季度, 中国云计算市场
  *阿里巴巴*以 `40.3%` 的市场份额高居第一;
  *华为*以 `17.4%` 的市场份额夺得第二;
  *腾讯*位列第三, 市场份额为 `14.9%`;
  *百度*排名第四, 市场份额为 `8.4%`.

* [Kitex](https://github.com/cloudwego/kitex)
  - Kitex 字节跳动内部的 Golang 微服务 RPC 框架
* [rpcx](https://github.com/smallnest/rpcx)
  - Best microservices framework in Go, like alibaba Dubbo,
    but with more features, Scale easily.

```
没人怀疑 gRPC 在 CNCF 的统治地位,
但是 gRPC 不太适合业务层的开发.
```

* [Fluid](https://github.com/fluid-cloudnative/fluid)
  - Fluid, elastic data abstraction and acceleration for
    BigData/AI applications in cloud.
  - 有点意思, 明年看看

```
2021 年 4 月 27 日, 云原生计算基金会 (CNCF) 宣布通过全球 TOC 投票
接纳 Fluid 成为 CNCF 官方沙箱项目.
Fluid 是一个由南京大学, 阿里云以及 Alluxio 开源社区联合发起并开源的
云原生数据编排和加速系统.
```

* [Volcano](https://github.com/volcano-sh/volcano)
  - Volcano is a batch system built on Kubernetes.
  - It provides a suite of mechanisms that are commonly required
    by many classes of batch & elastic workload including:
  - machine learning/deep learning/big data applications.
  - 在 Kubeflow 里面看到的, 期待未来

* [New GKE Dataplane V2 increases security and visibility for containers](https://cloud.google.com/blog/products/containers-kubernetes/bringing-ebpf-and-cilium-to-google-kubernetes-engine)
  - Using *eBPF* to build Kubernetes Network Policy Logging
  - [Cilium](https://github.com/cilium)

```
Today, we're introducing GKE Dataplane V2,
an opinionated dataplane that harnesses the power of eBPF and Cilium,
an open source project that makes the Linux kernel
Kubernetes-aware using eBPF.
Now in beta, we're also using Dataplane V2 to bring
Kubernetes Network Policy logging to Google Kubernetes Engine (GKE).
```

* [OpenFunction/OpenFunction](https://github.com/OpenFunction/OpenFunction)
  - 由 **青云** 开源, [QingCloud](https://www.qingcloud.com)
  - 基于 [dapr/dapr](https://github.com/dapr/dapr)

* 2021年8月, 开源 Data Cloud 服务商 Datafuse Labs 完成数百万美元种子轮与天使轮融资.

* [APISIX](https://github.com/apache/apisix)
  - 公司一直在用的, 国产优秀开源软件
  - 加油!

* [Announcing Linkerd's Graduation](https://linkerd.io/2021/07/28/announcing-cncf-graduation/)
  - Above all else, we promise to be relentless and unwavering in our mission
    to keep Linkerd simple, lightweight, and fast;
    to minimize human cost of service mesh operation wherever possible;
    and to continue making Linkerd the best service mesh on the planet.
  - [Why Linkerd doesn't use Envoy](https://linkerd.io/2020/12/03/why-linkerd-doesnt-use-envoy/)
  - 个人还是非常喜欢 **Linkerd** 的, 虽然 **Istio** 更可能赢得这场比赛

* 2021-06-30: **Quarkus** 2.0.0.Final released
  - Vert.x 4
  - MicroProfile 4
  - Continuous Testing
  - and much more
  - 我还是比较期待 **Spring native**

* 3月16日, `混合云第一股` **青云科技** 正式在科创板上市, 股票代码: `688316`

### Dapr

* [Dapr (Distributed Application Runtime) joins CNCF Incubator](https://www.cncf.io/blog/2021/11/03/dapr-distributed-application-runtime-joins-cncf-incubator/)

```
"Distributed applications and microservices form the basis
for containers and cloud native, but writing distributed
applications that are scalable and reliable can be
incredibly difficult," said Chris Aniszczyk, CTO of CNCF.

"Dapr integrates well with other CNCF projects and provides
best practices that developers can build on top of using
any language or framework. We're excited to welcome Dapr to
the CNCF and work to cultivate their community."

The Dapr project roadmap includes the addition of a new
Configuration API that makes it easier for developers to
manage configuration for their applications and get notified
whenever configurations change, as well as a Query API that
makes it easier for developers to query and filter data in
Dapr state stores.

In addition, the project is looking to add support for gRPC
and WASM-based components that'll allow dynamic discoverability
of state stores, pub/sub brokers, bindings, and other
Dapr components. Finally, new Concurrency APIs will unblock
scenarios such as leader election are also being discussed
in the Dapr community.
```

* [Dapr 1.3.0](https://github.com/dapr/dapr/releases/tag/v1.3.0)
  - Setup VS Code development in a containerized environment
    and use this in GitHub Codespaces for
    contributing to dapr project
  - 赞!

* [The Netflix Cosmos Platform](https://netflixtechblog.com/the-netflix-cosmos-platform-35c14d9351ad)

* [How Alibaba is using Dapr](https://blog.dapr.io/posts/2021/03/19/how-alibaba-is-using-dapr)

* [A visual guide to Dapr](https://blog.dapr.io/posts/2021/03/02/a-visual-guide-to-dapr)

* [Announcing Dapr v1.0](https://blog.dapr.io/posts/2021/02/17/announcing-dapr-v1.0)
  - [Dapr 1.0.0](https://github.com/dapr/dapr/releases/tag/v1.0.0)

### Argo

* [Argo Project](https://github.com/argoproj)
  - [Argo Workflows](https://github.com/argoproj/argo-workflows)
  - 有点意思, 期待成为主流
  - [Argo CD](https://github.com/argoproj/argo-cd)
  - [Argo Workflows v3.0](https://blog.argoproj.io/argo-workflows-v3-0-4d0b69f15a6e)
  - [Argo Workflows v3.1 is coming ...](https://blog.argoproj.io/argo-workflows-v3-1-is-coming-1fb1c1091324)

```zsh
Application
# A group of Kubernetes resources as defined by a manifest.
# This is a Custom Resource Definition (CRD).
Application source type
# Which Tool is used to build the application.
Target state
# The desired state of an application, as represented by files in a Git repository.
Live state
# The live state of that application. What pods etc are deployed.
Sync status
# Whether or not the live state matches the target state.
# Is the deployed application the same as Git says it should be?
Sync
# The process of making an application move to its target state.
Sync operation status
# Whether or not a sync succeeded.
Refresh
# Compare the latest code in Git with the live state. Figure out what is different.
Health
# The health of the application, is it running correctly?
```

* [Argo CD - v2.1.0](https://github.com/argoproj/argo-cd/releases/tag/v2.1.0)
  - The synchronization process became *much much faster*
    and requires significantly *less memory*.
  - This dramatically *reduces* the number of Git requests.

### Kustomize

* [Kustomize Feature List](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#kustomize-feature-list)

```
kustomize targets kubernetes;
it understands and can patch kubernetes style API objects.
It's like make, in that what it does is declared in a file,
and it's like sed, in that it emits edited text.
```

```
~/app
  deployment.yaml
  kustomization.yaml
  service.yaml
```

```
~/app
  base
    deployment.yaml
    kustomization.yaml
    service.yaml
  overlays
    development
      cpu_count.yaml
      kustomization.yaml
      replica_count.yaml
    production
      cpu_count.yaml
      kustomization.yaml
      replica_count.yaml
```

```zsh
kustomize build ~/app/overlays/production
```

### Helm

```zsh
Chart.yaml
# A YAML file containing information about the chart
values.yaml
# The default configuration values for this chart
charts/
# A directory containing any charts upon which this chart depends.
templates/
# A directory of templates that, when combined with values,
# will generate valid Kubernetes manifest files.
  deployment.yaml
  service.yaml
  ingress.yaml
```

### Operator pattern

* [operator-framework/operator-sdk](https://github.com/operator-framework/operator-sdk)
  - Operator SDK `Reaches v1.0` (August 18, 2020)

```
Kubernetes' controllers concept lets you extend the cluster's behaviour
without modifying the code of Kubernetes itself.
Operators are clients of the Kubernetes API that
act as controllers for a Custom Resource.

Some of the things that you can use an operator to automate include:

1. deploying an application on demand
2. taking and restoring backups of that application's state
3. handling upgrades of the application code alongside
   related changes such as database schemas or extra configuration settings
5. simulating failure in all or part of your cluster to test its resilience
6. choosing a leader for a distributed application
   without an internal member election process
```

* [CNCF Operator White Paper - Final Version](https://github.com/cncf/tag-app-delivery/blob/main/operator-wg/whitepaper/Operator-WhitePaper_v1-0.md)

```
The Operator Pattern can be used to solve the problem of managing state.

By using the operator pattern, the knowledge on how to
adjust and maintain a resource is captured in code
and often within a single service (also called a controller).

The Operator pattern consists of three components:

1. The application or infrastructure that we want to manage.
2. A domain specific language that enables the user
   to specify the desired state of the application
   in a declarative way.
3. A controller that runs continuously:
   Reads and is aware of the state.
   Runs actions when operations state changes in an automated way.
   Report the state of the application in a declarative way.
```

* [OAM](https://oam.dev)
  - An open model for defining cloud native apps.
  - https://github.com/oam-dev/kubevela

### Knative

* [Announcing: Knative 1.0](https://knative.dev/blog/articles/announcing-knative-1.0/)
  - We are pleased to announce the release of
    **Knative 1.0** on `Nov. 2, 2021`.
  - [Knative 1.0 is out!](https://knative.dev/blog/articles/knative-1.0/)
  - [Knative Serving release v1.0.0](https://github.com/knative/serving/releases/tag/knative-v1.0.0)

* Announcing Knative v0.24 Release
  - In preparation for *GA*
  - Kubernetes *1.19* is now required
  - DomainMapping feature is now BETA

* Knative Version 0.22 release

```
Highlights

Eventing now allows subscribers and triggers from
different namespaces to be used together.

1.18 is now the minimum Kubernetes version required
to use the Apache Kafka broker with Knative Eventing v0.22.

Apache Kafka broker now supports the ability to choose
between ordered and unordered delivery.

The Knative Operator v0.22 release contains bug fixes
and supports version v0.22 of Knative Serving and Eventing.
```

### JDK 17 (LTS)

* [Oracle Releases Java 17](https://www.oracle.com/news/announcement/oracle-releases-java-17-2021-09-14/)
  - *2021-09-14*
  - [JDK 17](https://openjdk.java.net/projects/jdk/17/)
  - [JEP 414: Vector API (Second Incubator)](https://openjdk.java.net/jeps/414)

* [ZGC | What's new in JDK 16](https://malloc.se/blog/zgc-jdk16)
