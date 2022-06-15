---
title: Kubernetes in Action (中) - 2nd Edition
description: 树木丛生, 百草丰茂. 秋风萧瑟, 洪波涌起.
date: 2021-09-07
---

- [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)
  - https://www.manning.com/books/kubernetes-in-action-second-edition

## Deploying stateful workloads with StatefulSets

- Therefore, to deploy a MongoDB replica set in Kubernetes,
  you need to ensure that:
  - each Pod has its own `PersistentVolume`,
  - each Pod is addressable by its own unique address,
  - when a Pod is deleted and replaced,
    the new Pod is assigned the same
    address and `PersistentVolume`.
