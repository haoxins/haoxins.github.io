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

```
As with Deployments, in a StatefulSet you specify a Pod template,
the desired number of replicas, and a label selector.
However, you can also specify a PersistentVolumeClaim template.

Each time the StatefulSet controller creates a new replica,
it creates not only a new Pod object,
but also one or more PersistentVolumeClaim objects.
```

```
When a StatefulSet Pod is deleted and recreated,
it's given the same name as the Pod it replaced.
Also, a Pod with a particular ordinal number is always
associated with PersistentVolumeClaims with the same number.

When you create a StatefulSet, only the first Pod is created initially.
Then the StatefulSet controller waits until the Pod is ready
before creating the next one.
```

- When using a __headless__ Service with a StatefulSet,
  an additional DNS record is created for each Pod so that
  the IP address of each Pod can be looked up by its name.
  - This is how stateful Pods maintain their stable network identity.
  - These DNS records don't exist when the __headless__ Service
    isn't associated with a StatefulSet.
