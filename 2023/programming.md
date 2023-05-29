---
title: 码农碎碎念~
description: 分行接绮树, 倒影入清漪. 不学御沟上, 春风伤别离.
date: 2023-01-08
---

- Rust 加持下的 Python 新生态

- [Ruff](https://github.com/charliermarsh/ruff)
  - An extremely fast Python linter, written in Rust.
- [Rye](https://github.com/mitsuhiko/rye)
  - 确实好用!
- [PyO3](https://github.com/PyO3/pyo3)
  - [Maturin](https://github.com/PyO3/maturin)

---

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
    [InfluxDB IOx](https://github.com/influxdata/influxdb_iox)
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
