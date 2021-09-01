---
title: Istio in Action
description: 白云一片去悠悠, 青枫浦上不胜愁. 谁家今夜扁舟子? 何处相思明月楼?
date: 2021-08-04
---

* [Service Mesh Comparison](https://servicemesh.es)
  - *Istio*: Proxy sidecar
  - *Dapr*: Service sidecar

------------------

* [Istio in Action](https://book.douban.com/subject/33406485/)
  - 开篇先说, 要解决的**问题**, *赞*
  - 新技术(在早期)有可能是*毒药*, 过了早期阶段, 大部分就消失了 :)

* Although *unit tests* are critical, a strong focus for
  automated testing should be ***scenario or feature tests***.
  - 赞同, 也是我的个人习惯
  - 不能**单纯**面向数字 (*Coverage*) 写 tests

* Lastly, as implementation details change because of
  refactoring, paying down technical debt, maintenance, etc.
  our *feature tests should rarely have to change*.
  - 从个人角度来讲, 单测*早期*针对 *feature tests* 难以覆盖的 codes
  - *后期*则是针对 *hot/key codes*

> * With Istio we can finely control traffic to
    new deployments and reduce the risk of doing deployments.
> * As we aspire to do deployments quickly we should also
    lower the risks of doing those deployments.

* **Challenges**
  - Keeping faults from jumping isolation boundaries
  - Building applications/services capable of
    responding to changes in their environment
  - Building systems capable of running in
    partially failed conditions
  - Understanding what's happening to the overall system
    as it constantly changes and evolves
  - Inability to control the runtime behaviors of the system
  - Implementing strong security as the attack surface grows
  - How to lower the risk of making changes to the system
  - How to enforce policies about `who/what/when` can use
    the components in the system

* Some patterns have evolved to help mitigate these types of
  *scenarios* and help make applications more resilient to
  unplanned, unexpected **failures**:
  - *Client side load balancing* - give the client
    the list of possible endpoints and
    let it decide which to call
  - *Service discovery* - a mechanism for finding the
    periodically updated list of healthy endpoints
    for a particular logical service
  - *Circuit breaking* - shedding load for a period of
    time to a service that appears to be misbehaving
  - *Bulk heading* - limiting client resource usage
    with explicit thresholds (connections, threads, sessions, etc)
    when making calls to a service
  - *Timeouts* - Enforcing time limitations on requests,
    sockets, liveness, etc when making calls to a service
  - *Retries* - Retrying a failed request
  - *Retry budgets* - Applying constraints to retries;
    ie, limiting the number of retries in a given period
    (e.g., can only retry 50% of the calls in a 10s window)
  - *Deadlines* - giving requests context about how long
    a response may still be useful; if outside of
    the deadline, disregard processing the request

> Collectively these types of patterns
  can be though of *"application networking"*.

* To do this, this *"service proxy"* will need to
  understand application constructs like
  messages and requests instead of more
  traditional infrastructure proxies which
  understand connections and packets.
  In other words, we need an **L7 proxy**.

* **Envoy** gives us networking capabilities like
  *retries*, *timeouts*, *circuit breaking*,
  *client-side load balancing*, *service discovery*,
  *security*, and *metrics-collection*
  without any explicit language or framework dependencies.

* This *`proxy+application`* combination forms the
  foundation of a communication bus known as a **service mesh**.

* Together, the *data plane* and the *control plane* provide
  important capabilities necessary in any
  cloud-native architecture such as:
  - Service resilience
  - Observability signals
  - Traffic control capabilities
  - Security
  - Policy enforcement

* Istio can assign *workload identity* and
  embed that into the certificates.
  Istio can use the *identity* of the
  different *workloads* to further
  implement powerful *access-control policies*.

* What are the drawbacks to using a service mesh?
  - for someone unfamiliar with operating Envoy,
    this could look very complex and
    inhibit existing debugging practices.
  - Another drawback of using a service mesh
    is in terms of *tenancy*.
    A mesh is as valuable as there are services
    running in the mesh. That is, the more services
    in the mesh the more valuable the mesh becomes
    to operating those services.
    However, without *proper policy*, *automation*, and *forethought*
    going into the tenancy and isolation models of
    the physical mesh deployment, you could end up in a situation
    where mis-configuring the mesh impacts many services.

## First steps with Istio

## Istio's data plane: Envoy Proxy

## Istio Gateway: getting traffic into your cluster

## Traffic control: fine-grained traffic routing

## Resilience: solving application-networking challenges

## Observability

## Securing microservice communication

## Troubleshooting the data plane

## Performance tuning the control plane

## Scaling Istio in your organization

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
