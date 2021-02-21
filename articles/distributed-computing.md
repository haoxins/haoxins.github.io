---
title: Distributed computing
description: ~
date: 2021-02-21
---

|            | 拜占庭容错 | 一致性 |  性能  | 可用性 |
| ---------- |:--------:|:-----:|:------:|:-----:|
|     2PC    |    N     |  强   |        |       |
|     TCC    |    N     |  最终 |        |       |
|     Raft   |    N     |  强   |        |       |
|    Gossip  |    N     |  最终 |    H   |   H   |
| Quorum NWR |    N     |  强   |        |       |
|     PBFT   |    Y     |       |        |       |
|     PoW    |    Y     |       |        |       |

* CAP
  - C -> ACID
  - A -> Base

* [The Raft Consensus Algorithm](https://raft.github.io)

```
Raft 的设计目标是 强一致性 (线性一致性)
Raft 可以提供 强一致性, 也可以提供 最终一致性
```
