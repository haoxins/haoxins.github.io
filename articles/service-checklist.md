---
title: Service checklist
description: todo ~
date: 2019-04-08
---

1. 将系统功能拆分为独立的节点
2. 选择分布式架构模式
3. 确定节点间通讯的网络协议
4. 确定节点间 接口, 状态, 数据 模型
5. 确定每一个节点的每一个接口的重试策略
  - `最多一次 (most once)`, `至少一次 (at least once)`, `恰好一次 (exactly once)`
6. 针对不同节点的数据和状态, 确定共享策略
  - `无共享 (share nothing)`, `部分共享 (share something)`, `完全共享 (share everything)`
7. 确定各个节点 扩展/收缩 时的比例
8. 确定哪些接口需要应用 背压/负载 调节
9. 确定运维模式, 确定 系统/业务 的 警报, 日志, 监控
10. 明确哪些节点需要自动化支持

### 配置

* 将配置排除在代码之外的标准: 代码是否可以直接开源而无信息泄漏?
  - 不推荐按 `env` 区分的配置文件, 不易扩展

### 事务

* 事务完备性: 永远切记, `service` 随时会被 `shutdown`

### 伸缩

* Amdahl 定律: `S(N) = 1/((1-P) + P/N)`
  - S(N): 系统在 N 个核上执行时, 获得的加速
  - P: 程序中可以并行的部分的比例
* Little 定律: `L=λW`, `响应时间 = 队列长度 / 到达速率`
* 容量测试
  - soak testing
  - spike testing
  - stress testing
  - load testing

### Ops

* 出错务必大声吼出来!
* `log`, `metric`, `alarm`
