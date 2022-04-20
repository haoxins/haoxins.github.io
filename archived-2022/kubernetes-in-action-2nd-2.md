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
  to delete first.
* It deletes Pods in the following order:
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

* The `spec` section of a Deployment object isn't much
  different from a ReplicaSet's.
  - The `replicas`, `selector`, and `template` fields serve
    the same purpose as those in ReplicaSets.
  - In the additional `strategy` field, you can configure
    the update strategy to be used when you
    update this Deployment.

* The `Controlled By` line indicates that this ReplicaSet
  has been created and is owned and controlled by the
  `kiada` Deployment.
  - You'll notice that the Pod template, selector, and
    the ReplicaSet itself contain an additional label key
    `pod-template-hash` that you never defined
    in the Deployment object.
  - The value of this label matches the last part of
    the ReplicaSet's name.

* The value of the `pod-template-hash` label isn't random
  but calculated from the contents of the Pod template.
  - Because the same value is used for the ReplicaSet name,
    the name depends on the contents of the Pod template.
  - It follows that every time you change the Pod template,
    a new ReplicaSet is created.

* Everything you learned about ReplicaSet scaling and
  how the ReplicaSet controller ensures that the actual
  number of Pods always matches the desired number of
  replicas also applies to Pods deployed via a Deployment.

* If you make changes to an object that is owned by another
  object, you should expect that your changes will be undone
  by the controller that manages the object.
* As you might expect, the Deployment controller will undo
  any changes you make to the ReplicaSet, not just when you
  scale it. Even if you delete the ReplicaSet object,
  the Deployment controller will recreate it.

* When you `kubectl apply`, the value of the
  `kubectl.kubernetes.io/last-applied-configuration`
  is used to calculate the changes
  needed to be made to the API object.

* The **advantage** only becomes clear when you update
  the Pod template in the Deployment.
  - You may recall that this has no immediate effect
    with a ReplicaSet. The updated template is only used
    when the ReplicaSet controller creates a new Pod.
  - However, when you update the Pod template in a
    Deployment, the Pods are replaced immediately.

* The way the Pods are replaced depends on the update
  strategy configured in the Deployment.
  - **Recreate**: All Pods are deleted at the same time,
    and then, when all their containers are finished,
    the new Pods are created at the same time.
  - For a short time, while the old Pods are being
    terminated and before the new Pods are ready,
    the service is unavailable.
  - **RollingUpdate**: When a Pod is removed,
    Kubernetes waits until the new Pod is ready before
    removing the next Pod.
  - This way, the service provided by the Pods remains
    available throughout the upgrade process.
  - This is the **default** strategy.

* The `Recreate` strategy has no configuration options,
  while the `RollingUpdate` strategy lets you configure
  how many Pods Kubernetes replaces at a time.

* The labels you specify in the Pod template in a
  Deployment are also applied to the ReplicaSet.
* When you originally created the Deployment, only one
  ReplicaSet was created and all Pods belonged to it.
  - When you updated the Deployment,
    a new ReplicaSet was created.

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 0
      maxUnavailable: 1
  minReadySeconds: 10
```

* The two parameters that affect how fast Pods are replaced
  during a rolling update are `maxSurge` and `maxUnavailable`.
  - `maxSurge`: The maximum number of Pods above the
    desired number of replicas that the Deployment can
    have during the rolling update.
  - The value can be an absolute number or a percentage
    of the desired number of replicas.
  - `maxUnavailable`: The maximum number of Pods relative
    to the desired replica count that can be unavailable
    during the rolling update.
  - The value can be an absolute number or a percentage
    of the desired number of replicas.
* The most **important** thing about these two parameters
  is that their values are relative to the
  desired number of replicas.
  - For example, if the desired number of replicas is three,
    `maxUnavailable` is one, and the current number of Pods
    is five, the number of Pods that must be
    available is two, not four.
* You can't set both `maxSurge` and `maxUnavailable` to zero,
  as this wouldn't allow the Deployment to exceed the desired
  number of replicas or remove Pods,
  as one Pod would then be unavailable.

* The Deployment controller doesn't count the Pods itself,
  but gets the information about the number of Pods
  from the status of the underlying ReplicaSets.

* Instead of setting `maxSurge` and `maxUnavailable` to
  an absolute number, you can set them to a percentage of
  the desired number of replicas.
  - The controller calculates the absolute `maxSurge`
    number by **rounding up**,
  - and `maxUnavailable` by **rounding down**.
  - The default value for `maxSurge`
    and `maxUnavailable` is `25%`.

* To **pause** an update in the middle of the rolling
  update process, use the following command:
  - `kubectl rollout pause deployment kiada`
  - `kubectl rollout resume deployment kiada`

* When a new Pod is created in a rolling update,
  the Deployment controller waits until the Pod
  is available before continuing the rollout process.
  - By default, the Pod is considered available when
    it's ready (as indicated by the Pod's readiness probe).
  - If you specify `minReadySeconds`, the Pod isn't
    considered available until the specified amount of
    time has elapsed after the Pod is ready.
  - If the Pod's containers crash or fail their readiness
    probe during this time, the timer is reset.

* You can configure a different progress deadline by
  setting the `spec.progressDeadlineSeconds` field in
  the Deployment object.
  - If you increase `minReadySeconds` to more than `600`,
    you must set the `progressDeadlineSeconds`
    field accordingly.

* You may wonder where the revision history is stored.
  You won't find it in the Deployment object.
  - Instead, the history of a Deployment is represented
    by the ReplicaSets associated with the Deployment.
  - Each ReplicaSet represents one revision.
  - This is the reason why the Deployment controller
    **doesn't delete** the old ReplicaSet object after
    the update process is complete.
* The size of the revision history, and thus the number
  of ReplicaSets that the Deployment controller keeps
  for a given Deployment, is determined by the
  `revisionHistoryLimit` field in the Deployment's spec.
  - The default value is `10`.
* You might think that using `kubectl rollout undo` to
  revert to the previous version of the Deployment manifest
  is equivalent to applying the previous manifest file,
  but that's **not** the case.
  - The `kubectl rollout undo` command reverts **only**
    the Pod template and preserves any other changes
    you made to the Deployment manifest.
  - This includes changes to the update strategy and
    the desired number of replicas.
  - The `kubectl apply command`, on the other hand,
    overwrites these changes.
