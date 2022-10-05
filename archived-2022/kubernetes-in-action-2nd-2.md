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
  - each Pod has its own PersistentVolume,
  - each Pod is addressable by its own unique address,
  - when a Pod is deleted and replaced,
    the new Pod is assigned the same
    address and PersistentVolume.

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

```yaml
apiVersion: v1
kind: Service
metadata:
  name: quiz-pods
spec:
  clusterIP: None
  publishNotReadyAddresses: true
  selector:
    app: quiz
  ports:
  - name: mongodb
    port: 27017
```

- In the listing, the `clusterIP` field is set to `None`,
  which makes this a __headless__ Service.
- If you set `publishNotReadyAddresses` to `true`,
  the DNS records for each Pod are created immediately when
  the Pod is created, rather than only when the Pod is ready.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: quiz
spec:
  serviceName: quiz-pods
  podManagementPolicy: Parallel
  replicas: 3
  selector:
    matchLabels:
      app: quiz
  template:
    metadata:
      labels:
        app: quiz
        ver: "0.1"
    spec:
      volumes:
      - name: db-data
        persistentVolumeClaim:
          claimName: db-data
      containers:
      - name: quiz-api
        ...
      - name: mongo
        ...
        volumeMounts:
        - name: db-data
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: db-data
      labels:
        app: quiz
    spec:
      resources:
        requests:
          storage: 10Gi
      accessModes:
      - ReadWriteOnce
```

- In the `serviceName` field, for example,
  you specify the name of the headless Service
  that governs this StatefulSet.
- By setting `podManagementPolicy` to `Parallel`,
  the StatefulSet controller creates all Pods simultaneously.
- Unlike the Pod templates, where you omit the name field,
  you __must__ specify the name in the PersistentVolumeClaim template.
  - This name __must__ match the name in the
    volumes section of the Pod template.

---

- The only label you defined in the Pod template in the
  StatefulSet manifest was `app`, but the StatefulSet
  controller added two additional labels to the Pod:
  - The label `controller-revision-hash` serves the same
    purpose as the label `pod-template-hash` on the
    Pods of a ReplicaSet.
  - It allows the controller to determine to which
    revision of the StatefulSet a particular Pod belongs.
  - The label `statefulset.kubernetes.io/pod-name` specifies
    the Pod name and allows you to create a Service for
    a specific Pod instance by using this label in
    the Service's label selector.
- Since this Pod object is managed by the StatefulSet,
  the `ownerReferences` field indicates this fact.
  - Unlike Deployments, where Pods are owned by ReplicaSets,
    which in turn are owned by the Deployment,
  - StatefulSets own the Pods directly.
- The Pod's containers match the containers defined
  in the StatefulSet's Pod template, but that's
  __not__ the case for the Pod's volumes.
  - In the template you specified the `claimName` as `db-data`,
    but here in the Pod it's been changed to `db-data-quiz-0`.
  - This is because each Pod instance gets its own
    PersistentVolumeClaim.
  - The name of the claim is made up of the `claimName`
    and the name of the Pod.

---

- A Service object not only exposes a set of Pods at a stable
  IP address but also makes the cluster DNS resolve the Service
  name to this IP address.
- With a headless Service, __on the other hand__, the name
  resolves to the IPs of the Pods that belong to the Service.
- __However__, when a headless Service is associated with a
  StatefulSet, each Pod also gets its own `A` or `AAAA` record
  that resolves directly to the individual Pod's IP.
  - In addition to the `A` and `AAAA` records,
    each stateful Pod also gets `SRV` records.

### Understanding StatefulSet behavior

- A StatefulSet guarantees __at-most-one__ semantics for its Pods.
  Since two Pods with the same name can't be in the same namespace
  at the same time, the ordinal-based naming scheme of StatefulSets
  is sufficient to prevent two Pods with the same identity
  from running at the same time.

- This is an important fact because it explains why the StatefulSet
  controller shouldn't delete and recreate the Pod.
  - If the StatefulSet controller deletes and recreates the Pod
    while the Kubelet is down, the new Pod would be scheduled to
    another node and the Pod's containers would start.
  - There would then be two instances of the same workload running
    with the same identity.
  - That's why the StatefulSet controller doesn't do that.
  - If you want the Pod to be recreated elsewhere,
    __manual__ intervention is __required__.

```zsh
# To delete the Pod without waiting for confirmation,
# you must delete it as follows:
kubectl delete pod quiz-1 --force --grace-period 0
# Immediate deletion does not wait for confirmation
# that the running resource has been terminated.
# The resource may continue to run on the cluster indefinitely.
```

- If the PersistentVolume is a local volume on the failed node,
  the Pod can't be scheduled and its `STATUS` remains `Pending`.
- If the cluster uses network-attached volumes, the Pod will be
  scheduled to another node but may not be able to run if the
  volume can't be detached from the failed node and attached
  to that other node.

```
What do you do if the Pod can't be attached to the same volume?

If the workload running in the Pod can rebuild its data from scratch,
for example by replicating the data from the other replicas,
you can delete the PersistentVolumeClaim so that a new one can be
created and bound to a new PersistentVolume.

However, since the StatefulSet controller only creates the
PersistentVolumeClaims when it creates the Pod,
you must also delete the Pod object.
```

- __Unlike__ ReplicaSets, when you scale down a StatefulSet,
  the Pod with the highest ordinal number is deleted first.
- __Unlike__ Pods, their PersistentVolumeClaims are preserved.
  - Retaining PersistentVolumeClaims is the default behavior,
    but you can configure the StatefulSet to delete them via
    the `persistentVolumeClaimRetentionPolicy` field.

> It's common for a StatefulSet to be associated with __both__
  a regular Service and a headless Service.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: quiz
spec:
  persistentVolumeClaimRetentionPolicy:
    whenScaled: Delete
    whenDeleted: Retain
  ...
```

- If you want to delete a StatefulSet but keep the Pods and the
  PersistentVolumeClaims, you can use the `--cascade=orphan` option.
  - In this case, the PersistentVolumeClaims will be preserved
    even if the retention policy is set to `Delete`.

- Another way to ensure data retention is to set the
  `reclaimPolicy` in the StorageClass referenced in the
  PersistentVolumeClaim template to `Retain`.

---

- The default `podManagementPolicy` is `OrderedReady`,
  but you can relax the StatefulSet ordering guarantees
  by changing the policy to `Parallel`.
  - __OrderedReady__
  - Pods are created one at a time in ascending order.
  - After creating each Pod, the controller waits until the
    Pod is ready before creating the next Pod.
  - When scaling down, the Pods are deleted in reverse order.
  - The controller waits until each deleted Pod is
    finished before deleting the next one.
  - __Parallel__
  - All Pods are created and deleted at the same time.
  - The controller doesn't wait for individual Pods to be ready.
- Another feature of the __OrderedReady__ Pod management policy is
  that the controller blocks the scale-down operation
  if not all replicas are ready.
- The __OrderedReady__ Pod management policy affects the
  initial rollout of StatefulSet Pods,
  their scaling, and how Pods are replaced when a node fails.
  - However, the policy __doesn't__ apply when you delete the StatefulSet.
  - If you want to terminate the Pods in order,
    you should first scale the StatefulSet to zero,
    wait until the last Pod finishes,
    and only then delete the StatefulSet.

---

- You can also specify the update strategy in the `updateStrategy`
  field in the spec section of the StatefulSet manifest,
  but the available strategies are
  different from those in a Deployment.
  - __RollingUpdate__
  - The Pod with the highest ordinal number is deleted first
    and replaced with a Pod created with the new template.
  - When this new Pod is ready, the Pod with the next highest
    ordinal number is replaced.
  - This is the default strategy.
  - __OnDelete__
  - The StatefulSet controller waits for
    each Pod to be manually deleted.
  - When you delete the Pod, the controller replaces it with
    a Pod created with the new template.
- The RollingUpdate strategy in a StatefulSet behaves
  similarly to the RollingUpdate strategy in Deployments,
  but only one Pod is replaced at a time.
  - You may recall that you can configure the Deployment
    to replace multiple Pods at once using the `maxSurge`
    and `maxUnavailable` parameters.
- If the StatefulSet is configured with the RollingUpdate
  strategy and you trigger the update when not all
  Pods are ready, the rollout is held back.
  - If a new Pod fails to become ready during the update,
    the update is also paused, just like a Deployment update.

> A ControllerRevision is a generic object that represents
  an immutable snapshot of the state of an
  object at a particular point in time.

- StatefulSets don't have a `pause` field that you can use to
  prevent a Deployment rollout from being triggered,
  or to pause it halfway.

- In a StatefulSet you can achieve the same result and more
  with the `partition` parameter of the RollingUpdate strategy.
  - The value of this field specifies the ordinal number at
    which the StatefulSet should be partitioned.
  - If you set the `partition` value appropriately, you can
    implement a Canary deployment, control the rollout manually,
    or stage an update instead of triggering it immediately.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: quiz
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 3
  replicas: 3
  ...
```

- To deploy a canary, set the `partition` value to
  the number of replicas minus one.
- You'll see that only the Pod `quiz-2` has been
  updated because only its ordinal number is
  __greater than or equal__ to the partition value.
- When the `partition` field is set to `zero`,
  the StatefulSet updates all Pods.

---

- If you use the `OnDelete` strategy, the rollout is semi-automatic.
  - You manually delete each Pod, and the StatefulSet controller
    then creates the replacement Pod with the new template.
  - With this strategy, you can decide which Pod to update and when.
  - You don't necessarily have to delete the Pod with
    the highest ordinal number first.
- Since the update strategy also applies when you use the
  `kubectl rollout undo` command, the rollback process
  is also semi-automatic.
  - You must delete each Pod yourself if you want to
    roll it back to the previous revision.
- If you delete a Pod and the new Pod isn't ready,
  but you still delete the next Pod, the controller will
  update that second Pod as well.
  - It's your responsibility to consider Pod readiness.

## Deploying node agents and daemons with DaemonSets

> 2022年10月5日, 终于又更新了!

```
A DaemonSet is an API object that ensures that
exactly one replica of a Pod is running on
each cluster node.
By default, daemon Pods are deployed on every node,
but you can use a node selector to restrict
deployment to some of the nodes.

Although you could run system software on your
cluster nodes using standard methods such as
init scripts or systemd, using a DaemonSet
ensures that you manage all workloads
in your cluster in the same way.
```

```
In each pass of its reconciliation loop,
the DaemonSet controller finds the Pods
that match the label selector, checks that
each node has exactly one matching Pod,
and creates or removes Pods to
ensure that this is the case.
```

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: demo
spec:
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
      - name: demo
        image: busybox
        command:
        - sleep
        - infinity
```

> The `selector` is __immutable__, but you can
  change the labels as long as they
  still match the `selector`.

```yaml
...
status:
  currentNumberScheduled: 2
  desiredNumberScheduled: 2
  numberAvailable: 2
  numberMisscheduled: 0
  numberReady: 2
  observedGeneration: 1
  updatedNumberScheduled: 2
```

- `currentNumberScheduled`
- The number of Nodes that run at least one
  Pod associated with this DaemonSet.
- `desiredNumberScheduled`
- The number of Nodes that should run the daemon Pod,
  regardless of whether they actually run it.
- `numberAvailable`
- The number of Nodes that run at least
  one daemon Pod that's available.
- `numberMisscheduled`
- The number of Nodes that are running a
  daemon Pod but shouldn't be running it.
- `numberReady`
- The number of Nodes that have at least
  one daemon Pod running and ready.
- `updatedNumberScheduled`
- The number of Nodes whose daemon Pod is
  current with respect to the
  Pod template in the DaemonSet.

---

