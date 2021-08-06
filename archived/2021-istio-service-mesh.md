---
title: (2021) Istio & Service mesh
description: 白云一片去悠悠, 青枫浦上不胜愁. 谁家今夜扁舟子? 何处相思明月楼?
date: 2021-08-04
---

* [Service Mesh Comparison](https://servicemesh.es)

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
