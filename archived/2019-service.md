---
title: Something about service
description: 空门说得恒沙劫, 应笑终年为一先
date: 2019-04-08
---

* 代码 -> **how** & **what**
* 文档 -> **why**
* 能删掉的代码, 就别注释掉

* [FMEA](https://zhuanlan.zhihu.com/p/23208961)

### aha

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

### 较大 feature 上线注意事项清单

* 是否有 DB Migrations? 是否会影响现有数据?
* 是否有配置项变更? 新增配置项?
* 是否有新的服务依赖?
* 如果服务被第三方依赖, 是否有 API Broken?
* 是否 Broken 既有代码, 流程, 或潜在影响? 是否有完整回归老的功能?
* 新的功能是否有非 Prod 环境难以体现的问题或功能?
* 新增功能是否 PM 知悉确认, 并 QA 覆盖主体流程?
* 是否有潜在问题, Edge Cases 清单, 并评估潜在影响?
* 针对可能的生产问题 (基本100%会出现), 是否有基本的预期及预案?

### Serverless

* Callers Auth
* Region & Time Zone

### 康威定律

* 组织沟通方式会通过系统设计表达出来
* 时间再多一件事情也不可能做的完美, 但总有时间做完一件事情
* 线型系统和线型组织架构间有潜在的异质同态特性
* 大的系统组织总是比小系统更倾向于分解

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
* `自动化机制` 处理 `人` 不擅长的事情: `重复` 的任务和 `快速` 的响应
* `人` 处理 `自动化机制` 不擅长的事情: 纵观全局

### APIs

* HTTP Response

```json
{
  "data": "Could be [], {}, null, ...",
  "meta": {
    "message": "Success or others ...",
    "error": "null (If Success) or Error message",
    "page": 3,
    "size": 50,
    "total": 1000,
    "errors": [
      {
        "domain": "A",
        "reason": "Aha"
      }
    ]
  }
}
```

### 名家语录

```
Show me your flowcharts and conceal your tables,
and I shall continue to be mystified.
Show me your tables,
and I won't usually need your flowcharts; they'll be obvious.

-- Fred Brooks
```
