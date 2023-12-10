---
title: 码农碎碎念~
description: 分行接绮树, 倒影入清漪. 不学御沟上, 春风伤别离.
date: 2023-01-08
---

- Kafka Protocol Buffers (zstd) to JSON (zstd)
  - Messages `236 M`, Disk `112.7 Gb`
  - to
  - Messages `214 M`, Disk `138.0 Gb`
  - `+ 35%`

---

- 吐槽一下 [maturin](https://github.com/PyO3/maturin), publish 的时候提示
  - `Please enter your username`
  - 然后统一输入
  - `__token__`
  - 多此一举~

---

- [NebulaGraph](https://docs.nebula-graph.com.cn)

```
在一个图空间中, 一个点由点的 ID 唯一标识, 即 VID 或 Vertex ID.
```

> `vid`: Space 全局唯一!

```
下列操作是异步实现的, 要在下一个心跳周期之后才能生效, 否则访问会报错.
为确保数据同步, 后续操作能顺利进行, 请等待 2 个心跳周期 (20 秒).

CREATE SPACE
CREATE TAG
CREATE EDGE
ALTER TAG
ALTER EDGE
CREATE TAG INDEX
CREATE EDGE INDEX
```

```
DELETE VERTEX <vid> WITH EDGE;
```

```
$^  起始点
$$  目的点
```

- GO 复合语句中如需引用子查询的结果, 需要为该结果设置别名,
  并使用管道符 `|` 传递给下一个子查询,
  同时在下一个子查询中使用 `$-` 引用该结果的别名.

---

- 2023年9月, 用来测试`文心一言`的问题
  - 详细描述`20`世纪的数学成果
  - 详细描述`20`世纪的物理成果

```
2023-09-04 不满意
```


- [Go Style Decisions](https://google.github.io/styleguide/go/decisions)
  - 强迫症患者必看

- [Deconstructing Type Parameters](https://go.dev/blog/deconstructing-type-parameters)

```
To repeat, writing type parameters and constraints [S []E, E any]
means that the type argument for S can be any unnamed slice type,
but it can't be a named type defined as a slice literal.
Writing [S ~[]E, E any], with a ~, means that the type argument
for S can be any type whose underlying type is a slice type.
```

```go
// We can constrain the component types any way we like.
func WithStrings[S ~[]E, E interface { String() string }](s S) (S, []string)
// This says that the argument of WithStrings must be a
// slice type for which the element type has a String method.
```

- [New UUID Formats](https://uuid6.github.io/uuid6-ietf-draft/)

```
UUID Version 6

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           time_high                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           time_mid            |      time_low_and_version     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|clk_seq_hi_res |  clk_seq_low  |         node (0-1)            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                         node (2-5)                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

UUID Version 7

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           unix_ts_ms                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          unix_ts_ms           |  ver  |       rand_a          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|var|                        rand_b                             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            rand_b                             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

UUID Version 8

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           custom_a                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          custom_a             |  ver  |       custom_b        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|var|                       custom_c                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           custom_c                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Max UUID

FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
```

---

- [InfluxDB Edge](https://github.com/influxdata/influxdb)
  - Apache DataFusion 生态终于崭露头角~
  - 期待 Arroyo

```
InfluxDB is an open source time series database written in Rust, using
Apache Arrow, Apache Parquet, and Apache DataFusion as its foundational
building blocks. This latest version (3.x) of InfluxDB focuses on
providing a real-time buffer for observational data of all kinds
(metrics, events, logs, traces, etc.) that is queryable via SQL or InfluxQL,
and persisted in bulk to object storage as Parquet files,
which other third-party systems can then use.
```

- [Arroyo 0.6](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.6.0)
  - [Announcing Arroyo 0.6.0](https://www.arroyo.dev/blog/arroyo-0-6-0)
  - [Example GKE configuration](https://doc.arroyo.dev/deployment/kubernetes#example-gke-configuration)

```
We've finished our migration from gRPC
to REST for the public-facing Arroyo API.
```

> 版本发布越发频繁了.

- [Apache Flink Kubernetes Operator 1.6.0](https://flink.apache.org/2023/08/15/apache-flink-kubernetes-operator-1.6.0-release-announcement/)
  - 主要期待: `General Autoscaler Improvements`

- [Arroyo 0.5](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.5.0)
  - The biggest of these is the new FileSystem connector,
    which is a high-performance, transactional sink for
    writing data to filesystems and object stores like S3.
  - This allows Arroyo to write into
    data lakes and data warehouses.

- [Aptos](https://github.com/aptos-labs/aptos-core)

```
Aptos Labs & Microsoft Partnership: Making Web3 Accessible on Aptos
August 09, 2023
```

---

- 从 [Gin](https://github.com/gin-gonic/gin) 切换到 [Hertz](https://github.com/cloudwego/hertz)
  - 项目对 Web 框架依赖很少, 切换成本较低~
  - OpenTelemetry 的支持是一个亮点

- [PEP 703 - Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/)
  - 还是值得期待的~

- [Changes in MySQL 8.1.0](https://dev.mysql.com/doc/relnotes/mysql/8.1/en/news-8-1-0.html)
  - 最大的 Change, 让你知道 MySQL 还活着~ 哈哈哈!

- 2023-07-18, 你妹的 [PyYAML](https://github.com/yaml/pyyaml/issues/724)
  - [kfp](https://github.com/kubeflow/pipelines/issues/9745)
  - 折腾了一个下午!
  - 教训总结: Python 需要 Rust inside!

- 2023-07, Spring Boot `2` to Spring Boot `3`
  - 手上正好有一个小项目, 可以用来看看跑起来的差异~
  - Java `11` to Java `17`
  - Spring Web to Spring WebFlux
  - 内存占用降低约 `40%`

- [Govulncheck v1.0.0 is released!](https://go.dev/blog/govulncheck)

> 找个项目试一下, 然后

```
Scanning your code and ... packages across ... dependent modules
for known vulnerabilities...

panic: ...
```

> 换个项目

```
Scanning your code and ... packages across ... dependent modules
for known vulnerabilities...

No vulnerabilities found.
```

- [Kvrocks](https://github.com/apache/kvrocks)
  - Redis 太贵了~

- [Go 1.21 Release Notes](https://tip.golang.org/doc/go1.21)
  - New built-in functions: `min`, `max` and `clear`.
  - New `log/slog` package for structured logging.
  - New `slices` package for common operations
    on slices of any element type.
  - This includes sorting functions that are
    generally faster and more ergonomic
    than the `sort` package.
  - New `maps` package for common operations on
    maps of any key or element type.
  - New `cmp` package with new utilities
    for comparing ordered values.
- 2023-07: `slog` 已经用上了, 还不错~

> 可以逐渐放弃 [lo](https://github.com/samber/lo) 了~
> 更正 (2023-08): 放弃 `lo` 不可能!

```go
var prints []func()
for i := 1; i <= 3; i++ {
  prints = append(prints, func() { fmt.Print(i) })
}
for _, print := range prints {
  print()
}
// print 444
// with `GOEXPERIMENT=loopvar`
// print 123
```

```go
s := []int{1, 2, 3}
for _, i := range s {
  go func() {
    fmt.Print(i)
  }()
}
// print 333
// with `GOEXPERIMENT=loopvar`
// print 321 or 213 or 312 or others (random)
```

- [Arroyo 0.3](https://github.com/ArroyoSystems/arroyo/releases/tag/v0.3.0)
  - With this release we are shipping initial support for writing
    user-defined functions (UDFs) in Rust, allowing users to
    extend SQL with custom business logic.
  - 嗯, 开始像点样子了~

---

- Rust 加持下的 Python 新生态

- [Ruff](https://github.com/charliermarsh/ruff)
  - An extremely fast Python linter, written in Rust.
  - Bye! Black & isort
  - 优势: lint & format (Black & isort) 一体
- [Rye](https://github.com/mitsuhiko/rye)
  - 确实好用!
- [PyO3](https://github.com/PyO3/pyo3)
  - [Maturin](https://github.com/PyO3/maturin)

---

- [SQL: 2023 is finished: Here is what's new](http://peter.eisentraut.org/blog/2023/04/04/sql-2023-is-finished-here-is-whats-new)

```
Property Graph Queries

A whole new part 16 was added to the SQL standard,
titled "Property Graph Queries (SQL/PGQ)".
(Including this new part,
there are now 11 active parts of SQL (ISO/IEC 9075).
The part that most people know as the core language is part 2.)
This allows data in tables to be queried as if it were a graph database.
```

- [JEP 444: Virtual Threads](https://openjdk.org/jeps/444)
  - 终于来了, 但也就仅此而已

---

- [酷壳 - CoolShell](https://coolshell.cn)
  - 享受编程和技术所带来的快乐
  - 2023-05-15 网络消息传播开来
  - 陈皓, 网名: 左耳朵耗子, 2023年5月13日, 心梗逝世, 享年 47 岁

---

- [sea-streamer](https://github.com/SeaQL/sea-streamer)
  - [rdkafka](https://github.com/fede1024/rust-rdkafka)

- [Announcing the Release of Apache Flink 1.17](https://flink.apache.org/2023/03/23/announcing-the-release-of-apache-flink-1.17/)
  - 有不少东西值得测试~

```
Generic Incremental Checkpoint (GIC)
  有望缓解 Big window/state 的性能波动
Watermark Alignment Support
  有望缓解 Multi partitions 的性能波动
```

```
Oracle intends to make future LTS releases every
two years meaning the next planned LTS release
is Java 21 in September 2023.
```

> 今天 (2023-03-28) 才知道, 期待 Java 21

---

- [Arroyo](https://github.com/ArroyoSystems/arroyo)
  - 2023-04 突然冒出来的
  - 只有十几个 commits, 但是貌似完成度蛮高
  - deps: arrow, axum, datafusion, parquet,
    prost, serde, tokio, tonic
  - The query is parsed and planned via
    [Datafusion](https://github.com/apache/arrow-datafusion)
  - Arroyo can also be configured to schedule workers on a
    [Nomad](https://github.com/hashicorp/nomad)
    cluster.
  - Support for scheduling workers on a
    __Kubernetes__ cluster is __coming soon__.
  - 对 Nomad 没兴趣, 静候 K8s ready.
  - [Lightweight Asynchronous Snapshots for Distributed Dataflows](https://arxiv.org/pdf/1506.08603.pdf)
  - Arroyo uses __Postgres__ to store configuration
    (sources, connections, sinks, pipelines, etc)
    and the status of the system.
  - Arroyo uses
    [Refinery](https://github.com/rust-db/refinery)
    to manage migrations.
  - 我个人还是更喜欢
    [Atlas](https://github.com/ariga/atlas),
    哈哈哈. Refinery 只是 Flyway 的模仿者~
  - Arroyo uses __Prometheus__ for metrics collection.
  - Checkpoints are stored on __S3__ for recovery.
  - 2023-04-10: 活跃度先超越
    [Fluvio](https://github.com/infinyon/fluvio)
    再说吧!
  - 2023-04-10: `Hello, world!` 初体验, 并不顺畅!
  - 透过 Arroyo 去看一下 Rust 的生态
  - [petgraph](https://github.com/petgraph/petgraph)
  - Graph data structure library.
    Provides graph types and graph algorithms.
  - [tracing](https://github.com/tokio-rs/tracing)
  - `tracing` is a framework for instrumenting
    Rust programs to collect structured,
    event-based diagnostic information.
    `tracing` is maintained by the Tokio project,
    but does not require the tokio runtime to be used.
  - BTW,
    [InfluxDB Edge](https://github.com/influxdata/influxdb)
    同样.
    It is built using Apache Arrow and DataFusion among other things.

- [DataFusion: Streaming execution support roadmap](https://github.com/apache/arrow-datafusion/issues/4285)
  - 暂时 (2023) 不抱太大期望~

- [Lance](https://github.com/lancedb/lance)
  - Alternative to Parquet
- [LanceDB](https://github.com/lancedb/lancedb)
  - An open-source database for vector-search
    built with persistent storage,
    which greatly simplifies retrevial,
    filtering and management of embeddings.

---

- https://github.com/apache/incubator-opendal
  - From [Databend](https://github.com/datafuselabs)
  - 赞!

- https://blyss.dev
  - Access data privately using homomorphic encryption.
  - Privately scan for breached credentials,
    block malicious URLs, access blockchain data, and more.
  - 先看看能活多久~

---

- [Introducing Rust-Based Ztunnel for Istio Ambient Service Mesh](https://istio.io/latest/blog/2023/rust-based-ztunnel/)
  - https://github.com/istio/ztunnel

```
This purpose-built ztunnel involved two key areas:

1. The configuration protocol between ztunnel and its Istiod
2. The runtime implementation of ztunnel

We chose to build on top of the Tokio and Hyper libraries,
two of the de-facto standards in the ecosystem that
are extensively battle-tested and easy to write
highly performant asynchronous code with.
```

> 所以, [Linkerd 2](https://github.com/linkerd/linkerd2)
  和 [Linkerd 2 Proxy](https://github.com/linkerd/linkerd2-proxy)
  彻底没戏了.
> 当然, [Istio](https://github.com/istio/istio)
  和 [Envoy](https://github.com/envoyproxy/envoy)
  也逐渐分道扬镳了~

---

- [Service Weaver](https://serviceweaver.dev)
  - Service Weaver is a programming framework for
    writing and deploying cloud applications.
  - https://github.com/ServiceWeaver/weaver
  - 感觉现在才出, 有点晚了~
  - 看看会不会有一个活跃的社区

- ChatGPT 最近是热点话题, 与其无聊的讨论什么职位会被替代,
  我更期待何时 AI 能帮助完成那些必定无法仅靠人力解决的事情.
  - 比如: 编纂`数学史`;
  - 再比如: 评审`数学证明`;
  - 再比如: 全人类知识图谱.

- [Cog](https://github.com/replicate/cog)
  - Containers for machine learning
- [Oxen](https://github.com/Oxen-AI/Oxen)
  - Library, tools, and server to manage local
    and remote Oxen repositories.
  - Includes:
  - `oxen` (command line interface)
  - `oxen-server` (remote server to sync data to)
  - `liboxen` (shared lib between cli and server)

---

- [Eclipse Zenoh](https://github.com/eclipse-zenoh/zenoh)

```
Zenoh (pronounce /zeno/) unifies data in motion,
data at rest and computations. It carefully blends
traditional pub/sub with geo-distributed storages,
queries and computations, while retaining a level of
time and space efficiency that is well beyond
any of the mainstream stacks.
```

---

- Go `1.20` is released!
  - `1 Feb 2023`

```go
package errors

// Join returns an error that wraps the given errors.
// Any nil error values are discarded.
// Join returns nil if errs contains no non-nil values.
// The error formats as the concatenation of the strings obtained
// by calling the Error method of each element of errs, with a newline
// between each string.
func Join(errs ...error) error {
  // ...
}
```

- The `math/rand` package now automatically seeds
  the global random number generator
  (used by top-level functions like `Float64` and `Int`)
  with a random value, and the top-level
  `Seed` function has been __deprecated__.

- The top-level `Read` function has been __deprecated__.
  - In almost all cases, `crypto/rand.Read` is more appropriate.

> 前进一小步, 真的是一小步, 无聊~

---

- `2023-01`, 列几个值得关注的`早期项目`
  - [Polars](https://github.com/pola-rs/polars)
  - Blazingly fast DataFrames in Rust, Python
  - [DataFusion](https://github.com/apache/arrow-datafusion)
  - DataFusion is an extensible query planning, optimization,
    and execution framework, written in Rust, that uses
    Apache Arrow as its in-memory format.
  - [BlindAI](https://github.com/mithril-security/blindai)
  - BlindAI is a confidential AI inference server.
  - 关注原因: 早期探索者
  - [BastionLab](https://github.com/mithril-security/bastionlab)
  - BastionLab is a simple privacy framework for
    data science collaboration,
    covering data exploration and AI traning.
  - 关注原因: 早期探索者
