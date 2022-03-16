---
title: Kubernetes deep dive
description: 春江潮水连海平, 海上明月共潮生. 滟滟随波千万里, 何处春江无月明!
date: 2021-07-28
---

------------------

* [Kubernetes 1.22: Server Side Apply moves to GA](https://kubernetes.io/blog/2021/08/06/server-side-apply-ga/)

* [Annotating Kubernetes Services for Humans](https://kubernetes.io/blog/2021/04/20/annotating-k8s-for-humans/)

------------------

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
* Pod template, `spec.template`

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

* **StatefulSet**

```
StatefulSet 的设计其实非常容易理解,
它把现实世界里的应用状态抽象为了两种情况.

1. 拓扑状态

应用的多个实例之间不是完全对等的.
这些应用实例必须按照某种顺序启动,
比如应用的主节点 A 要先于从节点 B 启动.
而如果删除 A 和 B 两个 Pod,
它们再次被创建出来时也必须严格按照这个顺序运行.
并且, 新创建出来的 Pod 必须和原来 Pod 的网络标识一样,
这样原先的访问者才能使用同样的方法访问到这个新 Pod.

2. 存储状态

应用的多个实例分别绑定了不同的存储数据.
对于这些应用实例来说, Pod A 第一次读取到的数据和隔了 10 分钟之后
再次读取到的数据应该是同一份,
哪怕在此期间 Pod A 被重新创建过.
这种情况最典型的例子是一个数据库应用的多个存储实例.

所以, StatefulSet 的核心功能, 就是通过某种方式记录这些状态,
然后在 Pod 被重新创建时能够为新 Pod 恢复这些状态.
```

```
首先, StatefulSet 的控制器直接管理的是 Pod.
这是因为 StatefulSet 里的不同 Pod 实例不再像 ReplicaSet
中那样都是完全一样的, 而是有了细微区别.

比如, 每个 Pod 的 hostname, name 等都不同, 都携带了编号.
而 StatefulSet 通过在 Pod 的名字里加上事先约定好的编号来区分这些实例.

其次, Kubernetes 通过 Headless Service 为这些有编号的 Pod,
在 DNS 服务器中生成带有相同编号的 DNS 记录.
只要 StatefulSet 能够保证这些 Pod 名字里的编号不变,
那么 Service 里类似于 web-0.nginx.default.svc.clusterlocal
这样的 DNS 记录就不会变, 而这条记录解析出来的 Pod 的 IP 地址,
会随着后端 Pod 的删除和重建而自动更新.
这当然是 Service 机制本身的能力, 不需要 StatefulSet 操心.

最后, StatefulSet 还为每个 Pod 分配并创建一个相同编号的 PVC.
这样, Kubernetes 就可以通过 Persistent Volume 机制
为这个 PVC 绑定对应的 PV, 从而保证了每个 Pod 都拥有一个独立的 Volume.

在这种情况下, 即使 Pod 被删除, 它所对应的 PVC 和 PV 依然会保留下来.
所以当这个 Pod 被重新创建出来之后, Kubernetes 会为它找到编号相同的 PVC,
挂载这个 PVC 对应的 Volume 从而获取以前保存在 Volume 里的数据.
```

* Operator

```
StatefulSet 管理的 "有状态应用" 的多个实例,
也都是通过同一个 Pod 模板创建出来的,
使用的是同一个 Image.
这也就意味着: 如果你的应用要求不同节点的 Image 不同,
就不能再使用 StatefulSet 了.
对于这种情况, 应该考虑 Operator.
```

```
Job Controller 实际上控制了作业执行的并行度 (parallelism),
以及总共需要完成的任务数 (completions) 这两个重要参数.

CronJob 与 Job 的的关系正如同
Deployment 与 Pod 的关系一样.
CronJob 是一个专门用来管理 Job 对象的控制器.
只不过, 它创建和删除 Job 的依据是 schedule 字段定义的,
一个标准的 Unix Cron 格式的表达式.

1. concurrencyPolicy: Allow
2. concurrencyPolicy: Forbid
3. concurrencyPolicy: Replace
```

```
在 Kubernetes 项目中, 一个 API Object 在 etcd 里的
完整资源路径是由 Group, Version, Resource 3个 部分组成的.
```

### CRD + Custom Controller

* **Informer**
  - `EventHandler`
  - resync

* **ListAndWatch**
  - `delta FIFO queue`

* [Code Generation for CustomResources](https://cloud.redhat.com/blog/kubernetes-deep-dive-code-generation-customresources)

### Operator

```
Operator 的工作原理, 实际上是利用 Kubernetes 的 CRD
来描述我们想要部署的 "有状态应用";
然后在 自定义控制器 里根据自定义 API 对象的变化,
来完成具体的部署和运维工作.
所以, 编写 etcd Operator 与前面编写 自定义控制器 的过程并无不同.
```

## 存储

* VolumeController

* 2 steps
  - Attach (nodeName) -> kube-controller-manager
  - Mount  (dir)      -> kubelet

* StorageClass -> PVs
  - PVC -> PV

* CSI

## 网络

* [The Layers of the OSI Model Illustrated](https://www.lifewire.com/layers-of-the-osi-model-illustrated-818017)

* CNI

* [IPVS proxy mode](https://kubernetes.io/docs/concepts/services-networking/service/#proxy-mode-ipvs)

* [**Cilium**](https://github.com/cilium/cilium)

* [Weave](https://github.com/weaveworks/weave)

* [Flannel](https://github.com/flannel-io/flannel)
  - 基于 UDP 在 用户态 实现 Overlay
  - 基于 VXLAN 在 内核台 实现 Overlay

* [Calico](https://github.com/projectcalico/calico)

## 调度

* 可压缩资源 & 不可压缩资源

* cpu: `1000m` 即 1
* memory
  - 1Mi = 1024 * 1024
  - 1M = 1000 * 1000

* QoS (Quality of Service)

```
当 Eviction 发生时, kubelet 具体会挑选哪些 Pod 进行删除,
就需要参考这些 Pod 的 QoS 类别了.

首当其冲的, 自然是 BestEffort 类别的 Pod.

其次, 是属于 Burstable 类别,
  并且发生 "饥饿" 的资源使用量已经超出 requests 的 Pod.

最后, 才是 Guaranteed 类别.

并且 Kubernetes 会保证只有当 Guaranteed 类别的 Pod 的资源
使用量超过其 limits 的限制,
或者宿主机本身正处于 Memory Pressure 状态时,
Guaranteed 类别的 Pod 才可能被选中进行 Eviction 操作.

当然, 对于同 QoS 类别的 Pod 来说,
Kubernetes 还会根据 Pod 的优先级来进一步地排序和选择.
```

* cpuset

* Device plugin
  - GPU

## CRI

* kubelet, CRI -> SIG-Node

* kubelet
  - SyncLoop

* CRI shim
  - containerd -> runC

* [gVisor](https://github.com/google/gvisor)
  - KVM (Kernel-based Virtual Machine)
