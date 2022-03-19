---
title: Kubernetes in Action (中) - 2nd Edition
description: 树木丛生, 百草丰茂. 秋风萧瑟, 洪波涌起.
date: 2021-09-07
---

* [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)
  - https://www.manning.com/books/kubernetes-in-action-second-edition

## Replicating Pods with ReplicaSets

* A `ReplicaSet` represents a group of
  `Pod` replicas (exact copies of a `Pod`).
* And just as with `Services`, the `ReplicaSet's`
  label selector and `Pod` labels determine which
  `Pods` belong to the `ReplicaSet`.
  - A `ReplicaSet` only cares about the `Pods` that
    match its label selector and ignores the rest.
* The `selector` and `template` fields are **required**,
  but you can omit the `replicas` field.
  - If you do, a single replica is created.
* You'll notice that the labels in the `Pod template`
  match those in the `selector` field.
  - If they don't, the Kubernetes API will reject
    the ReplicaSet.
* Did you notice that there's no Pod name
  in the template?
  - That's because the Pod names are
    generated from the ReplicaSet name.

* status fields of the ReplicaSet
  - `fullyLabeledReplicas`
  - `readyReplicas`
  - `availableReplicas`

* There's even a special metadata field that
  lets you create objects without giving the full name.
  - Instead of the name field, you specify the
    name prefix in the `generateName` field.
* When Kubernetes creates `Pods` for a `ReplicaSet`, it
  sets the `generateName` field to match the `ReplicaSet` name.
  - The Kubernetes API server then generates the full name
    and puts it in the name field.

* In the case of `ReplicaSet` Pods, giving the Pods
  random names makes sense because these Pods are
  exact copies of each other and therefore fungible.
* However, for stateful workloads, it may make sense
  to number the Pods sequentially.
  - That's what happens when you use a
    `StatefulSet` object to create the Pods.

```zsh
kubectl get po kiada-abc -o yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: kiada
  name: kiada-abc
  namespace: kiada
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: kiada
    uid: 8e19d9b3-bbf1-4830-b0b4-da81dd0e6e22
```

* The metadata section in an object manifest sometimes
  contains the `ownerReferences` field, which contains
  references to the owner(s) of the object.
  - This field can contain multiple owners,
    but most objects have only a single owner.
  - In the case of this Pod, the *kiada* `ReplicaSet`
    is the **owner**, and the Pod is the
    so-called **dependent**.
* Kubernetes has a garbage collector that automatically
  deletes **dependent** objects when their owner is deleted.
  - If an object has multiple owners, the object is
    deleted when all its owners are gone.
* An owner reference can also indicate which owner
  is the controller of the object.
* In a ReplicaSet
  - The **selector is immutable**,
  - but you can update the other two properties.

* When you scale down a ReplicaSet, Kubernetes follows
  some well thought out rules to decide which Pod(s)
  to delete first. It deletes Pods in the following order:
  1. Pods that aren't yet assigned to a node.
  2. Pods whose phase is unknown.
  3. Pods that aren't ready.
  4. Pods that have a lower deletion cost.
  5. Pods that are collocated with a
    greater number of related replicas.
  6. Pods that have been ready for a shorter time.
  7. Pods with a greater number of container restarts.
  8. Pods that were created later than the other Pods.

* You can also influence which Pod is deleted
  first by setting the annotation
  `controller.kubernetes.io/pod-deletion-cost`
  on your Pods.
  - Pods without this annotation and those with a
    lower value will be deleted
    before Pods with higher values.

* Kubernetes also tries to keep the Pods evenly
  distributed across the cluster nodes.

* In some cases, it's useful to scale the number of
  replicas down to zero. All Pods managed by the ReplicaSet
  will be deleted, but the ReplicaSet object itself will
  remain and can be scaled back up at will.
  - A ReplicaSet scaled to zero is very common when
    the ReplicaSet is owned by a Deployment object.

* To add a label to the Pods that the ReplicaSet creates, you must add the label to its Pod template.
* Did you notice that the labels in the Pod template and
  those in the selector aren't identical?
  - They don't have to be identical, but the
    **labels in the selector** must be a
    **subset** of the **labels in the template**.
* When you change the Pod template, only the
  cookie cutter changes and that only affects
  the Pods that are created afterwards.

* Pods whose containers continually crash or fail their
  probes are never automatically deleted, even though
  the ReplicaSet controller could easily replace them
  with Pods that might run properly.
* Therefore, be aware that a ReplicaSet doesn't
  guarantee that you'll always have as many healthy
  replicas as you specify in the ReplicaSet object.
* A ReplicaSet only ensures that the desired number of
  Pods are present. It doesn't ensure that their
  containers are actually running and
  ready to handle traffic.

* To preserve the Pods when you delete the ReplicaSet
  object, use the following command:
  - `kubectl delete rs kiada --cascade=orphan`

## Managing Pods with Deployments

* A Deployment object doesn't directly manage the Pod objects,
  but manages them through a ReplicaSet object that's
  automatically created when you create the Deployment object.
