---
title: kubernetes (k8s) tips
description: kubernetes is good
date: 2018-05-10
---

### 基本问题

* 为什么推荐一个容器, 一个进程
* 为什么 k8s 的最小部署单元是 pod, 而非 container

### Kubernetes API

```
API
  - apiVersion
  - kind: object kind
  - metadata
    - namespace
    - name
    - uid
  - spec
  - status
```

* Pod
  - a container
  - a group of containers (sidecar)
  - one IP, all containers share the same IP, ports. containers in same Pod can visit by localhost
  - pod and volume 同生共死
  - phase: Pending, Running, Successed, Failed, Unkonwn
  - labels
  - Annotation: 不能被 selector
  - PodSecurityPolicy
  - livenessProbe
  - hook
  - PodPreset
  - PodDisruptionBudget

* Node -> Machine
  - Address: HostName, ExternalIP, InternalIP
  - Condition: OutOfDisk, Ready, MemoryPressure, DiskPressure
  - Capacity: CPU, Memory
  - Info: version, ...

* namespace
  - 常用于: dev, test, prod

* Secret
* ConfigMap

### Controller

- long-running - Deployment
- batch - Job
- node-daemon - DaemonSet
- stateful application - StatefulSet

* Deployment:
  - RS, new RC (Replica Set), replace RC (Replication Controller)
  - Deployment -> ReplicaSet -> Pods

* StatefulSet
  - Pod + Volume, if Pod die, new Pod mount exists Volume
  - can use as VM
  - remove/scale StatefulSet , will not remove `volume`
  - Pod -> volume
  - StatefulSet Pod 有唯一身份 ID, 网络 ID

* DaemonSet
  - 一般用于: 监控, 日志

* Job

* CronJob

* HPA (Horizontal Pod Autoscaling)
  - only for: Deployment, ReplicaSet

* Volume
  - Docker 中, Volume -> Container
  - Kubernetes 中, Volume -> Pod

### Service

* Service == L4: TCP & UPD
* Endpoints
  - Pod Endpoint
  - k8s 外部 Endpoint (IP Address)
* Proxy
  - iptables
  - ipvs
* Headless Service (spec.clusterIP == None)
* ServiceTypes
  - ClusterIP: 集群内部
  - NodePort: 集群外部可访问
  - LoadBalancer: 外部
  - ExternalName

### Ingress

* Ingress == L7: HTTP

* node -> machine

* pod
  - 一般, one pod -> one container (docker or others)
  - one pod -> multi containers, 下面的文章给了示例, 何时适合
  - https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns
  - pod 内各种资源共享, 比如, 跨 container 通过 localhost 互访

* replication controller
  - replica set: next-generation replication controller

* deployment controller
  - provides declarative updates for Pods and ReplicaSets

* service
  - end point

### minikube 专属

> 对于 dev 环境, 可以简单粗暴

* `hostNetwork` -> `true`

## Serverless

* [cncf/wg-serverless](https://github.com/cncf/wg-serverless)

### Projects

* [kubeless/kubeless](https://github.com/kubeless/kubeless)
* [knative/serving](https://github.com/knative/serving)

## Container

* [docker curriculum](https://docker-curriculum.com)
* [Understanding CNI - Container Networking Interface](http://www.dasblinkenlichten.com/understanding-cni-container-networking-interface)

## Network

* [flannel](https://github.com/coreos/flannel)

## Kubernetes

* [kubernetes bootcamp](https://kubernetesbootcamp.github.io/kubernetes-bootcamp)
* [feiskyer / kubernetes handbook](https://github.com/feiskyer/kubernetes-handbook)
* [rootsongjc / kubernetes handbook](https://github.com/rootsongjc/kubernetes-handbook)
* [kubernetes 101 networking](http://www.dasblinkenlichten.com/kubernetes-101-networking)
