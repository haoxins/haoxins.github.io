---
title: kubernetes (k8s) tips
description: kubernetes is good
date: 2018-05-10
---

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
