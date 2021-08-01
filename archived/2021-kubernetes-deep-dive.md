---
title: (2021) 深入剖析 Kubernetes
description: 春江潮水连海平, 海上明月共潮生. 滟滟随波千万里, 何处春江无月明!
date: 2021-07-28
---

* [深入剖析 Kubernetes](https://book.douban.com/subject/35424872/)

* 现在, **2021**
  - **Docker** 的遗产基本只有 **Image** 了
  - [Docker hub](https://hub.docker.com)

* Linux
  - Cgroups and Namespace
  - Server (Cloud), Embedded (IoT), Mobile/Laptop 的未来发展必定是分离的
  - **Linux** 未来或许只能 **Focus server**!
  - GUI 等很多东西都会是多余的
* Container
  - 同一个 Kernel
  - 不能 Namespace 化: **Time**
  - `Docker exec` -> `Linux setns()`
* Cgroups 的不足: `/proc`
* Image
  - `chroot` -> Mount Namespace -> `rootfs`
  - **UnionFS**
  - whiteout

## Hello Kubernetes

```
Kubernetes 中有一种特殊的容器启动方法叫作 "Static Pod".
它允许你把要部署的 Pod 的 YAML 文件放在一个指定的目录中.
这样, 当这台机器上的 kubelet 启动时, 它会检查该目录,
加载所有 Pod YAML 文件并在这台机器上启动它们.
从这一点也可以看出, kubelet 在 Kubernetes 项目中的地位非常高,
在设计上它就是一个完全独立的组件, 而其他 Master 组件更像是辅助性的系统容器.
```

* `kube-system` namespace
* `Taint`
* `Controller pattern`
  - Deployment controls Pods
* `Object events`
  - Pod events

* **Controller** and **Operator**
  - CRD + Operator

```

* Pod = Infra container, A container, B container, ...

## 编排

## 存储

## 网络

## 调度

## CRI

## Metric
