---
title: kubernetes (k8s) tips
description: kubernetes is good
date: 2018-05-10
---

### 基本问题

* 为什么推荐一个容器, 一个进程
* 为什么 k8s 的最小部署单元是 pod, 而非 container

* node -> machine (or vm)

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

##  Kubernetes

* [kubernetes bootcamp](https://kubernetesbootcamp.github.io/kubernetes-bootcamp)
* [feiskyer / kubernetes handbook](https://github.com/feiskyer/kubernetes-handbook)
* [rootsongjc / kubernetes handbook](https://github.com/rootsongjc/kubernetes-handbook)
* [kubernetes 101 networking](http://www.dasblinkenlichten.com/kubernetes-101-networking)
