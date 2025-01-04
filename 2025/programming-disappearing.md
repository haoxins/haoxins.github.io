---
title: 软件项目消亡史
description: 楼高目断, 天遥云黯, 只堪憔悴. 念兰堂红烛, 心长焰短, 向人垂泪.
date: 2024-07-13
---

```
2024-07-13 凌晨, 突发奇想~
当下 AI 热火朝天, 众人皆言很快就不需要码农了.
哈哈, 顺着这个契机, 就开始记录各个编程语言的消亡吧.

后来决定不仅仅局限于编程语言, 而是 (开源) 软件项目.
且必须是自己"直接/间接"使用过的!
```

- 首先, 给出几个定义
  - 何为消亡?
  - 编程技术的 GitHun repository archived
    或者超过 1 年没有新的 commits
  - 如何排除小众项目或者实验项目?
  - 该项目必须有主流应用, 即该项目必须有其他的基于它的应用,
    且该应用有一定的行业影响.

- No 1. __Hive__
  - [Hive](https://github.com/apache/hive)
  - 传统老兵~

- No 1. __ZooKeeper__
  - 曾几何时, 几乎是分布式系统的标配组件.
  - 最后的一次出现在开源社区视野,
    应该就是
    [Kafka](https://github.com/apache/kafka)
    宣布移除
    [ZooKeeper](https://github.com/apache/zookeeper)
    依赖!

```
What is ZooKeeper?
ZooKeeper is a centralized service for maintaining
configuration information, naming, providing distributed
synchronization, and providing group services.
All of these kinds of services are used in some form or
another by distributed applications. Each time they are
implemented there is a lot of work that goes into fixing
the bugs and race conditions that are inevitable.
Because of the difficulty of implementing these kinds of
services, applications initially usually skimp on them,
which makes them brittle in the presence of change and
difficult to manage. Even when done correctly,
different implementations of these services lead to
management complexity when the applications are deployed.
```

```
KIP-500: Replace ZooKeeper with a Self-Managed Metadata Quorum

Using the Raft algorithm, the controller nodes will elect a leader
from amongst themselves, without relying on any external system.
The leader of the metadata log is called the active controller.
The active controller handles all RPCs made by the brokers.
The follower controllers replicate the data that is written to
the active controller and serve as hot standbys if the active
controller fails.
Because the controllers will now all track the latest state,
controller failover will not require a lengthy reloading period
where we transfer all the states to the new controller.
Just like ZooKeeper, Raft requires a majority of nodes to be
running in order to continue running. Therefore, a three-node
controller cluster can survive one failure. A five-node controller
cluster can survive two failures, and so on.
```

- No 2. __Scala__
  - [Scala 2](https://github.com/scala/scala)
  - [Scala 3](https://github.com/scala/scala3)
  - 个人没写过 Scala, 所以这里是间接使用 Scala,
    嗯, 因为 Spark, 哈哈~
  - Scala 开发的主流应用在 2024 几乎唯一剩下了 Spark,
    且 Spark 没有计划迁移到 Scala 3.

- No 3. __Kubeflow__
  - [Kubeflow](https://github.com/kubeflow/kubeflow)
  - [Kubeflow pipelines](https://github.com/kubeflow/pipelines)
  - 作为自己贡献过的项目, 还是很惋惜的.
  - 理念其实不错, 也在较早的时候给出了一个可用版本.
    然后就是数年的停滞不前~ 错过了最该发力的时间窗口!

- No 4. __Flink__
  - [Flink](https://github.com/apache/flink)
  - [Flink Kubernetes Operator](https://github.com/apache/flink-kubernetes-operator)
  - [Java Operator SDK](https://github.com/operator-framework/java-operator-sdk)

- No 5. __Spark__
  - [Spark](https://github.com/apache/spark)
  - 2024-07, Spark 依旧广泛应用于数据领域,
    各大云计算厂商也有基于 Spark 的云服务.
    但是很少有人使用 Scala 3, 基本都是使用 Scala 2.

- No 6. __Deno__
  - [Node](https://github.com/nodejs/node)
  - [Deno](https://github.com/denoland/deno)
  - [Bun](https://github.com/oven-sh/bun)
  - 个人从未正经使用过 Deno 和 Bun, 这里纯粹是追忆陪伴 Node 的青春岁月.
  - Deno 大概率最先消亡~

- No 7. __MySQL__
  - [MySQL](https://github.com/mysql/mysql-server)
  - 被 Oracle 玩死了~

- No 8. __Kotlin__
  - [Kotlin](https://github.com/JetBrains/kotlin)

- No 9. __Spring__
  - [Spring Framework](https://github.com/spring-projects/spring-framework)
  - [Spring Boot](https://github.com/spring-projects/spring-boot)
  - 我还是那句话, 打败 Spring 的, 绝对不是另一个 Web Framework!
  - 而是类似
    [Dapr](https://github.com/dapr/dapr)
    等类似产物
