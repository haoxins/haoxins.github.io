---
title: Kubernetes in Action (2/4) - 2nd Edition
description: 澹泊之守, 须从秾艳场中试来; 镇定之操, 还向纷纭境上勘过.
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

- Kubernetes only schedules workloads to control plane
  Nodes if you explicitly allow it.
  - This rule also applies to workloads
    deployed through a DaemonSet.
- In short, some Nodes may specify taints, and a Pod
  must tolerate a Node's taints to
  be scheduled to that Node.

---

- The DaemonSet controller sets the `nodeAffinity`
  field and leaves the `nodeName` field empty.
  - This leaves scheduling to the Scheduler,
    which also takes into account the Pod's
    resource requirements and other properties.
- A DaemonSet deploys Pods to all cluster nodes that
  don't have taints that the Pod doesn't tolerate,
  but you may want a particular workload to run
  only on a subset of those nodes.
  - With a DaemonSet, you can do this by specifying a
    node selector in the Pod template.

```yaml
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      nodeSelector:
        gpu: cuda
```

- Unlike the Pod label selector,
  the node selector is __mutable__.

- At the time of writing, DaemonSets support
  the strategies listed in the following table.
  - `RollingUpdate`
  - In this update strategy, Pods are replaced one by one.
  - When a Pod is deleted and recreated, the controller waits
    until the new Pod is ready.
  - Then it waits an additional amount of time, specified in the
    `spec.minReadySeconds` field of the DaemonSet, before
    updating the Pods on the other Nodes.
  - This is the __default__ strategy.
  - `OnDelete`
  - It waits for you to manually delete each Pod,
    and then replaces it with a new Pod
    from the updated template.

---

- If you set `maxSurge` above zero, two instances of the
  Pod run on the Node during an update for the time
  specified in the `minReadySeconds` field.
  - Most daemons don't support this mode because they
    use locks to prevent multiple instances
    from running simultaneously.
  - If you tried to update such a daemon in this way,
    the new Pod would never be ready because it couldn't
    obtain the lock, and the update would fail.
- The `maxUnavailable` parameter is set to one,
  which means that the DaemonSet controller updates
  only one Node at a time.
  - It doesn't start updating the Pod on the next Node
    until the Pod on the previous node
    is ready and available.
- Likewise, if you delete an existing Pod during a
  rolling update, it's replaced with a new Pod.
  - The same thing happens if you configure the
    DaemonSet with the `OnDelete` update strategy.

### Special features in Pods running node agents and daemons

- If you want to give a process running in a
  container full access to the operating
  system kernel, you can mark the
  container as __privileged__.

```yaml
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      containers:
      - name: kube-proxy
        securityContext:
          privileged: true
    ...
```

- This gives the process running in the `kube-proxy`
  container root access to the host's kernel and
  allows it to modify the node's
  network packet filtering rules.

---

```yaml
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      containers:
      - name: kindnet-cni
        securityContext:
          capabilities:
            add:
            - NET_RAW
            - NET_ADMIN
          privileged: false
```

- Instead of being fully privileged, the capabilities
  `NET_RAW` and `NET_ADMIN` are added to the container.

---

- As you know, each Pod gets its own network interface.
  However, you may want some of your Pods,
  especially those deployed through a DaemonSet,
  to use the node's network interface(s)
  instead of having their own.

```yaml
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      dnsPolicy: ClusterFirst
      hostNetwork: true
```

- Another option is for the Pod to use its own network,
  but forward one or more host ports to the container
  by using the `hostPort` field in the container's port list.
- Containers in a Pod configured with `hostNetwork: true`
  continue to use the other namespace types,
  so they remain isolated from the node in other respects.

---

- Each cluster usually comes with two priority classes:
  - `system-cluster-critical` and `system-node-critical`,
  - but you can also create your own.
- Each priority class has a value. The higher the value,
  the higher the priority.
  - The preemption policy in each class determines whether
    or not Pods with lower priority should be evicted
    when a Pod with that class is
    scheduled to an overbooked Node.
- You specify which priority class a Pod belongs to by
  specifying the class name in the `priorityClassName`
  field of the Pod's spec section.

```yaml
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      priorityClassName: system-node-critical
```

### Communicating with the local daemon Pod

1. __Binding directly to a host port__

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-agent
  ...
spec:
  template:
    spec:
      containers:
      - name: node-agent
        ...
        ports:
        - name: http
          containerPort: 80
          hostPort: 11559
```

- The manifest defines a DaemonSet that deploys
  node agent Pods listening on port `80` of the
  Pod's network interface.
  - However, in the list of ports, the container's
    port `80` is also accessible through port
    `11559` of the host Node.
  - The process in the container binds only to
    port `80`, but Kubernetes ensures that traffic
    received by the host Node on port `11559` is
    forwarded to port `80` within
    the node-agent container,

- For the application to connect to the local agent,
  you must pass the IP of the host node and port
  `11559` in this variable.
  - Of course, this IP depends on which Node the
    individual Kiada Pod is scheduled, so you can't
    just specify a fixed IP address in the Pod manifest.
  - Instead, you use the Downward API to get the local
    Node IP.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kiada
spec:
  template:
    spec:
      containers:
      - name: kiada
        env:
        ...
        - name: NODE_IP
          valueFrom:
            fieldRef:
              fieldPath: status.hostIP
        - name: NODE_AGENT_URL
          value: http://$(NODE_IP):11559
```

2. __Using the node's network stack__

- A similar approach to the previous section is for
  the agent Pod to directly use the Node's network
  environment instead of having its own.
  - In this case, the agent is reachable through the
    node's IP address via the port to which it binds.
  - When the agent binds to port `11559`, client Pods
    can connect to the agent through this port on
    the node's network interface.
- From the client's point of view, this is exactly
  like using the `hostPort` field in the previous section,
  but from the agent's point of view, it's different
  because the agent was previously bound to port `80`
  and traffic from the node's port `11559` was
  forwarded to the container's port `80`, whereas now
  it's bound directly to port `11559`.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-agent
  ...
spec:
  template:
    spec:
      hostNetwork: true
      ...
      containers:
      - name: node-agent
        ...
        ports:
        - name: http
          containerPort: 11559
```

3. __Using a local Service__

- You can configure a Service to forward traffic only
  within the same node by setting the
  `internalTrafficPolicy` in the Service
  manifest to `Local`.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: node-agent
  labels:
    app: node-agent
spec:
  internalTrafficPolicy: Local
  selector:
    app: node-agent
  ports:
  - name: http
    port: 80
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kiada
spec:
  template:
    spec:
      containers:
      - name: kiada
        env:
        ...
        - name: NODE_AGENT_URL
          value: http://node-agent
```

- Use the `hostPort` or `hostNetwork` approach only if
  you need to reach the agent from outside the cluster.
- If the agent exposes multiple ports, you may think
  it's easier to use `hostNetwork` instead of `hostPort`
  so you don't have to forward each port individually,
  but that's not ideal from a security perspective.
  - If the Pod is configured to use the host network,
    an attacker can use the Pod to bind to any port
    on the Node, potentially enabling
    man-in-the-middle attacks.

## Running finite workloads with Jobs and CronJobs

> Unlike Deployments and other resources that contain
  a Pod template, you can't modify the template in a
  Job object after creating the object.

- In a Job's pod template, you must explicitly set the
  restart policy to either `OnFailure` or `Never`.

---

- By default, you must delete Job objects manually.
  However, you can flag the Job for automatic deletion
  by setting the `ttlSecondsAfterFinished`
  field in the Job's spec.
  - As the name implies, this field specifies how long the
    Job and its Pods are kept after the Job is finished.
  - If you set the `ttlSecondsAfterFinished` field in a Job,
    the Job and its pods are deleted whether the
    Job completes successfully or not.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: generate-responses
  labels:
    app: quiz
spec:
  completions: 5
  parallelism: 2
  template:
    metadata:
      labels:
        app: quiz
    spec:
      restartPolicy: OnFailure
    ...
```

- The `completions` field specifies the number of
  Pods that must be successfully completed
  for this Job to be complete.
- The `parallelism` field specifies how many of
  these Pods may run in parallel.
- If you set `parallelism` higher than `completions`,
  the Job controller creates only as many Pods as
  you specified in the `completions` field.
- If `parallelism` is lower than `completions`, the
  Job controller runs at most `parallelism` Pods in
  parallel but creates additional Pods
  when those first Pods complete.

---

- When a container in the Pod fails, the Pod's `restartPolicy`
  determines whether the failure is handled at the Pod level
  by the Kubelet or at the Job level by the Job controller.
  - If the `restartPolicy` is `OnFailure`, the failed
    container is restarted within the same Pod.
  - However, if the policy is `Never`, the entire Pod is
    marked as failed and the Job controller creates a new Pod.

---

- At the time of writing, two completion modes are supported:
  - `Indexed` and `NonIndexed`.
  - __NonIndexed__
  - The Job is considered complete when the number of successfully
    completed Pods created by this Job equals the value of the
    `spec.completions` field in the Job manifest.
  - All Pods are equal to each other.
  - This is the __default__ mode.
  - __Indexed__
  - Each Pod is given a completion index (starting at `0`) to
    distinguish the Pods from each other.
  - The Job is considered complete when there is one
    successfully completed Pod for each index.
  - If a Pod with a particular index fails, the Job controller
    creates a new Pod with the same index.
  - The completion index assigned to each Pod is specified in
    the Pod annotation `batch.kubernetes.io/job-completion-index`
    and in the `JOB_COMPLETION_INDEX` environment variable
    in the Pod's containers.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: aggregate-responses-2021
  labels:
    app: aggregate-responses
    year: "2021"
spec:
  completionMode: Indexed
  completions: 12
  parallelism: 3
  template:
    metadata:
      labels:
        app: aggregate-responses
        year: "2021"
    spec:
      restartPolicy: OnFailure
      containers:
      ...
```

- In addition to setting the environment variable, the Job
  controller also sets the job completion index in the
  `batch.kubernetes.io/job-completion-index`
  annotation of the Pod.
  - Instead of using the `JOB_COMPLETION_INDEX` environment
    variable, you can pass the index via any environment
    variable by using the Downward API.

```yaml
env:
- name: MONTH
  valueFrom:
    fieldRef:
      fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
```

---

1. Headless Service for communication between Job Pods

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  clusterIP: none
  selector:
    job-name: comm-demo
  ports:
  - name: http
    port: 80
```

2. A Job manifest enabling pod-to-pod communication

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: comm-demo
spec:
  completionMode: Indexed
  completions: 2
  parallelism: 2
  template:
    spec:
      subdomain: demo-service
      restartPolicy: Never
      containers:
      - name: comm-demo
        image: busybox
        command:
        - sleep
        - "600"
```

- So the second Pod can connect to the first Pod
  using the address `comm-demo-0.demo-service`.

---

- A CronJob is just a thin wrapper around a Job.
  There are only two parts in the CronJob spec:
  - the `schedule` and the `jobTemplate`.
- By default, the time zone isn't specified.
  However, you can specify it using the `timeZone`
  field in the spec section of the CronJob manifest.

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: runs-at-3am-cet
spec:
  schedule: "0 3 * * *"
  timeZone: CET
  jobTemplate:
    ...
```

- In the CronJob's spec, you can use the fields
  `successfulJobsHistoryLimit` and `failedJobsHistoryLimit`
  to specify how many successful and failed Jobs to keep.
  - By default, CronJobs keeps `3` successful and `1` failed Job.
  - The Pods associated with each kept Job are also preserved,
    so you can view their logs.

```yaml
apiVersion: batch/v1
kind: CronJob
spec:
  schedule: "* * * * *"
  startingDeadlineSeconds: 30
  ...
```

- If the CronJob controller can't create the Job within
  `30` seconds of the scheduled time, it won't create it.
  - Instead, a `MissSchedule` event will be generated to
    inform you why the Job wasn't created.
- If the `startingDeadlineSeconds` field isn't set and the
  CronJob controller is offline for an extended period of time,
  undesirable behavior may occur when the
  controller comes back online.
  - This is because the controller will immediately create all
    the Jobs that should have been created while it was offline.
- However, this will only happen if the number of missing jobs
  is less than `100`. If the controller detects that more than
  `100` Jobs were missed, it doesn't create any Jobs.
  - Instead, it generates a `TooManyMissedTimes` event.
  - By setting the start deadline, you can
    prevent this from happening.

---

- By default, the CronJob controller creates new Jobs
  regardless of how many previous Jobs are still active.
  - However, you can change this behavior by setting the
    `concurrencyPolicy` in the CronJob spec.
- The following are the three supported concurrency policies.
  - `Allow`
  - Multiple Jobs are allowed to run at the same time.
  - This is the __default__ setting.
  - `Forbid`
  - Concurrent runs are prohibited.
  - If the previous run is still active when a new run
    is to be scheduled, the CronJob controller records a
    `JobAlreadyActive` event and skips creating a new Job.
  - `Replace`
  - The active Job is canceled and replaced by a new one.
  - The CronJob controller cancels the active
    Job by deleting the Job object.
  - The Job controller then deletes the Pods,
    but they're allowed to terminate gracefully.
  - This means that two Jobs are still running at the
    same time, but one of them is being terminated.
