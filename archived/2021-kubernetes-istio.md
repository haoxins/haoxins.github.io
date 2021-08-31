---
title: Service mesh - Istio
description: 白云一片去悠悠, 青枫浦上不胜愁. 谁家今夜扁舟子? 何处相思明月楼?
date: 2021-08-04
---

* [Service Mesh Comparison](https://servicemesh.es)
  - *Istio*: Proxy sidecar
  - *Dapr*: Service sidecar

------------------

* [Istio in Action](https://book.douban.com/subject/33406485/)
  - 开篇先说, 要解决的**问题**, *赞*
  - 不能面向简历搞技术

* Although *unit tests* are critical, a strong focus for
  automated testing should be ***scenario or feature tests***.
  - 赞同, 也是我的个人习惯


------------------

* [Istio 服务网格技术解析与实践](https://book.douban.com/subject/35001667/)
  - 微信读书, 免费阅读 :)

* Container: 隔离
* Kubernetes: 编排, 调度
* Istio: 流量
  - 控制面
  - 数据面

* 控制面
  - Pilot   流量
  - Mixer   监控
  - Citadel 安全
  - Galley

* **xDS**
  - Envoy 的各种服务发现协议

* `南北向`: 入口请求到集群服务的流量管理
* `东西向`: 集群内服务网格之间的流量管理

* Virtual service
  - Rules

* Service Entry
  - 用于把一个服务添加到 Istio 抽象模型或服务注册表中.
  - 添加服务条目后, Envoy 代理可以将流量发送到服务,
    如同这个添加的服务条目是网格中的其他服务一样.
    使用服务条目有很多方便之处,
    可以管理在网格外部运行的服务的流量.

* Istio 提供两种设置负载均衡的方式
  - 标准负载均衡
  - 会话保持

* SDS (秘钥发现服务)
  - `Envoy 1.8.0` 版本开始引入

* Knative
  - [Serving](https://github.com/knative/serving)
  - [Eventing](https://github.com/knative/eventing)

> * [Build: Tekton Pipelines](https://github.com/tektoncd/pipeline)
