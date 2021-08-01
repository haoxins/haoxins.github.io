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
再次强调: 容器的 "单进程模型" 并不是指容器里只能运行一个进程,
而是指容器无法管理多个进程.
这是因为容器里 PID=1 的进程就是应用本身, 其他进程都是这个 PID=1 进程的子进程.
可是, 用户编写的应用不像正常操作系统里的 init 进程或者 systemd 那样拥有进程管理的功能.
比如, 你的应用是一个 Java Web 程序 (PID=1),
然后你执行 docker exec 在后台启动了一个 Nginx 进程 (PID=3)
可是, 当这个 Nginx 进程异常退出时, 你该怎么知道呢?
这个进程退出后的垃圾收集工作又该由谁去做呢?
```

```
关于 Pod 最重要的一个事实是:
它只是一个逻辑概念.
也就是说, Kubernetes 真正处理的,
还是宿主机操作系统上 Linux 容器的 Namespace 和 Cgroups,
并不存在所谓的 Pod 的边界或者隔离环境.
Pod 其实是一组共享了某些资源的容器.
具体地说, Pod 里的所有容器者共享一个 Network Namespace,
并且可以声明共享同一个 Volume.
```

* Pod = Infra container, A container, B container, ...

* 基于调谐的状态逼近过程

```
调谐过程的存在确保了系统状态与终态保持一致的理论正确性.
确切地说, 调谐过程不停地执行 "检查 + Diff -> 执行" 的循环,
系统才能始终知道系统本身状态与终态之间的差异并采取必要行动.
相比之下, 仅仅拥有声明式描述是不充分的.
这个道理很容易理解, 你第一次提交这个描述时系统达成了你的期望状态,
并不能保证 1小时后 情况依然如此.

很多人会搞混 "声明式应用管理" 和 "声明式 API",
其实就是没有正确认识调谐的必要性.
```

```
IaD 设计中的 Data 具体表现出来, 其实就是声明式的 Kubernetes objects;
而 Kubernetes 中的 控制循环 确保系统本身能够始终跟这些 Data 所描述的状态保持一致.
在使用 Kubernetes 时之所以要写那么多 YAML文件,
只是因为我们需要通过一种方式把 Data 提交给 Kubernetes 而已.
在此过程中, YAML 只是一种为了让人类格式化地编写 Data 的一种载体.

既然 Kubernetes 需要处理这些 Data,
那么 Data 本身是不是也应该有一个固定的 "格式" 或 "规范",
这样 Kubernetes 才能解析它们?

没错, 这些 Data 的格式在 Kubernetes 中就叫作 API Object 的 Schema (比如: CRD).
这个 Schema 在编写自定义控制器时体现得就非常直接了,
它正是通过自定义 API Object 的 CRD 来进行规范的.
```

* [KubeVela](https://kubevela.io)
  - https://github.com/oam-dev/kubevela

* [Dapr](https://dapr.io)
  - https://github.com/dapr/dapr

## 编排

* Projected Volume (投射数据卷)

```
在 Kubernetes 中有几种特殊的 Volume,
它们存在的意义不是为了存放容器里的数据,
也不是用于容器和宿主机之间的致据交换,
而是为容器提供预先定义好的数据.

到目前为止, Kubernetes 支持的常用 Projected Volume 共有以下4种:

1. Secret
2. ConfigMap
3. Downward API
4. ServiceAccountToken
```

* ServiceAccountToken

```
一旦 Pod 创建完成, 容器里的应用就可以直接从默认
ServiceAccountToken 的挂载目录里访问授权信息和文件.
这个容器内的路径在 Kubernetes 里是固定的:
/var/run/secrets/kubernetes.io/serviceaccount
```

```
在 Kubernetes 的 Pod 中, 还有一个名叫
readinessProbe 的字段.
虽然它的用法与
livenessProbe 类似,
作用却大不相同.
readinessProbe 检查结果决定了这个 Pod 能否通过
Service 的方式访问, 而不影响 Pod 的生命周期.
```

```
Deployment 的控制器实际上控制的是 ReplicaSet 的数目,
以及每个 ReplicaSet 的属性.
而一个应用的版本对应的正是一个 ReplicaSet,
这个版本应用的 Pod 数量则由 ReplicaSet 通过它自己的控制器
(ReplicaSet Controller) 来保证.
通过这样的多个 ReplicaSet 对象,
Kubernetes 项目就实现了对多个应用版本的描述.
```

## 存储

## 网络

## 调度

## CRI

## Metric
