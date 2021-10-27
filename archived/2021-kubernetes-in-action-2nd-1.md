---
title: Kubernetes in Action (上) - 2nd Edition
description: 东临碣石, 以观沧海. 水何澹澹, 山岛竦峙.
date: 2021-08-30
---

* [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)
  - https://www.manning.com/books/kubernetes-in-action-second-edition

> Each application must be small enough to
  fit on *one of* the worker nodes.

* a Kubernetes cluster consists of nodes divided into **two groups**:
  - A set of **master nodes** that host the *Control Plane* components,
    which are the brains of the system,
    since they control the entire cluster.
  - A set of **worker nodes** that form the *Workload Plane*,
    which is where your workloads (or applications) run.

* Everything in Kubernetes is represented by an **object**.
  - You create and retrieve these objects via the *Kubernetes API*.
  - These objects are usually defined in one or more *manifest*
    files in either *YAML* or *JSON* format.

* These actions take place when you **deploy** the application:
  1. You submit the application *manifest*
     to the Kubernetes API.
     The API Server writes the *objects* defined
     in the manifest to *etcd*.
  2. A *controller* notices the newly created *objects*
     and creates several new objects -
     one for each application instance.
  3. The *Scheduler* assigns a node to each instance.
  4. The *Kubelet* notices that an instance is assigned
     to the Kubelet's node.
     It runs the application instance
     via the *Container Runtime*.
  5. The *Kube Proxy* notices that the application instances
     are ready to accept connections from clients and
     configures a *load balancer* for them.
  6. The *Kubelets* and the *Controllers* monitor
     the system and keep the applications running.

* A **controller** is interested in a particular *object type*.
  It waits for the API server to notify it that
  a new object has been created, and then performs
  operations to bring that object to life.

* The **scheduler** is a special type of *controller*,
  whose only task is to schedule application
  instances onto worker nodes.

* The **Kubelet** that runs on each *worker node*
  is also a type of *controller*.
  Its task is to wait for application instances
  to be assigned to the node on which it is
  located and run the application.

* The **Kube Proxy**, another *controller*
  running alongside the *Kubelet*,
  is responsible for setting up the *load balancer*.

* Once the application is up and running,
  the *Kubelet* keeps the application healthy
  by restarting it when it terminates.
  It also reports the *status* of the application
  by updating the *object* that
  represents the application instance.

* Using Kubernetes is *ten times easier*
  than **managing** it.

* The *filesystem* of a container consists of
  *read-only* layers from the container image and
  an additional *read/write* layer stacked on top.
  When an application running in container A changes
  a file in one of the *read-only* layers,
  the entire file is **copied** into the container's
  *read/write* layer and the file contents are changed there.

* *Open Container Initiative* (**OCI**)
* *Container Runtime Interface* (**CRI**)
  - One implementation of *CRI* is **CRI-O**,
    a lightweight alternative to *Docker* that
    allows you to leverage any *OCI-compliant*
    container runtime with *Kubernetes*.
    Examples of *OCI-compliant* runtimes include
    *runC*, and *Kata Containers*.

* The following types of **namespaces** exist:
  - The *Mount namespace* (mnt) isolates
    mount points (*file systems*).
  - The *Process ID namespace* (pid) isolates process IDs.
  - The *Network namespace* (net) isolates
    network devices, stacks, ports, etc.
  - The *Inter-process communication namespace* (ipc) isolates
    the communication between processes
    (this includes isolating message queues,
    shared memory, and others).
  - The *UNIX Time-sharing System* (UTS) namespace isolates
    the system hostname and the
    *Network Information Service* (NIS) domain name.
  - The *User ID namespace* (user) isolates user and group IDs.
  - The *Cgroup namespace* isolates the
    *Control Groups* root directory.

* In summary, processes may want to
  *share some resources but not others*.
  This is possible because separate namespace types exist.
  A process has an associated namespace for each type.

* **Linux Namespaces** make it possible for processes
  to access only some of the host's resources,
  but they don't *limit how much* of a single resource
  each process can consume.
* The *second* Linux kernel feature that makes
  containers possible is called
  **Linux Control Groups** (*cgroups*).
  It *limits*, accounts for and isolates system resources
  such as CPU, memory and disk or network bandwidth.

## Introducing the Kubernetes API objects

* *`~/.kube/config`*

* Each pod has its own `IP`, `hostname`, `processes`,
  `network interfaces` and `other` resources.
  Containers that are part of the same pod think that
  they're the only ones running on the computer.

* A *service* with the type *LoadBalancer*
  provisions an external *load balancer*, which
  makes the service accessible via a *public IP*.
  - If your cluster is deployed in the **cloud**,
    Kubernetes can ask the cloud infrastructure
    to provision a load balancer and configure
    it to forward traffic into your cluster.
  - The infrastructure tells Kubernetes the
    IP address of the load balancer and this
    becomes the external address of your service.

* When you create a *service*, it is assigned
  a static IP address that never changes
  during lifetime of the service.

> If you are familiar with relational database systems,
  you can compare *resources* and *object* types
  with *views* and *tables*.
  *Resources* are *views* through which
  you interact with *objects*.

* The **manifest** of most Kubernetes API *objects*
  consists of the following four sections:
  - **Type Metadata** contains information about
    the type of object this manifest describes.
    It specifies the *object type*, the *group*
    to which the type belongs, and the API version.
  - **Object Metadata** holds the basic information
    about the object instance, including its
    name, time of creation, owner of the object,
    and other identifying information. The fields in
    the *Object Metadata* are the *same for all object types*.
  - **Spec** is the part in which you specify the
    desired state of the object. Its fields differ
    between different object types. For pods, this is
    the part that specifies the pod's containers,
    storage volumes and other information
    related to its operation.
  - **Status** contains the current actual state
    of the object.

* `kubectl explain <kind>`
  - `kubectl explain node.spec.xxx`

> Unlike other objects, each *Event object* is deleted
  *one hour after its creation* to reduce the burden
  on etcd, the data store for Kubernetes API objects.

* The `kubectl get` command allows you to specify
  the field selector with the `--field-selector` option.
  To list only events that represent warnings,
  you execute the following command:

```zsh
kubectl get ev --field-selector type=Warning
```

## Running applications in Pods

* When a *pod* has multiple containers,
  all of them run on the *same* worker *node*
  - *a single pod instance never spans multiple nodes*.

* This *sharing of namespaces* is exactly how
  Kubernetes and the container runtime
  combine containers into pods.

* *each container always has its own Mount namespace*,
  giving it its own file system, but when two
  containers must share a part of the file system,
  you can add a **volume** to the pod and
  mount it into both containers.

* Placing several containers in a single pod is
  *only appropriate if* the application consists of
  *a primary process* and one or more processes
  that complement the operation of the primary process.
  - *primary container*
  - *sidecar container*

* The Kubernetes network model dictates that
  each pod is accessible from any other pod and
  that each node can reach any pod
  on any node in the cluster.

* The application in the container must be
  bound to a port on the *loopback device* for
  the Kubelet to reach it. If it listens only
  on the pod's **`eth0`** network interface,
  you won't be able to reach it with the
  `kubectl port-forward` command.

* a new Kubernetes feature called **ephemeral containers**
  allows you to debug running containers by
  attaching a debug container to them.

* ***Envoy***

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-ssl
spec:
  containers:
  - name: kiada
    image: luksa/kiada:0.2
    ports:
    - name: http
      containerPort: 8080
  - name: envoy
    image: luksa/kiada-ssl-proxy:0.1
    ports:
    - name: https
      containerPort: 8443
    - name: admin
      containerPort: 9901
```

* you also specify the container name using
  the `--container` or `-c` option.
  - `kubectl exec -it kiada-ssl -c envoy -- bash`
  - If you don't provide the name, kubectl
    exec defaults to the *first container*
    specified in the pod manifest.

* **Init containers** are like the pod's
  regular containers, but they don't run in parallel
  - *only one init container runs at a time*.

* **Init containers** are typically added
  to pods to achieve the following:
  - Initialize files in the volumes used
    by the pod's main containers.
  - Initialize the pod's networking system.
  - Delay the start of the pod's main
    containers until a precondition is met.
  - Notify an external service that the pod
    is about to start running.

* In a *pod manifest*, init containers are
  defined in the `initContainers` field
  in the spec section, just as regular
  containers are defined in its `containers` field.

* Whenever you create objects from a file,
  you can also delete them by passing the file to
  the delete command instead of
  specifying the name of the pod.
  - `kubectl delete -f abcd.yaml`
  - This makes *deploying* and *removing* the
    application as easy as executing
    `kubectl apply -f app.yaml` and
    `kubectl delete -f app.yaml`, respectively.
  - This applies to all files in the directory
    that have the correct file extension
    (`.yaml`, `.json`)
  - `kubectl apply -f apps/`
  - `kubectl delete -f apps/`

* *`kubectl delete all --all`*
  - The first `all` in the command indicates that
    you want to delete *objects of all types*.
  - The `--all` option indicates that you want to
    delete *all instances of each object type*.

## Managing the lifecycle of the Pod's containers

* A pod's *status* section contains the following information:
  - the *IP* addresses of the pod and the worker *node* that hosts it
  - *when* the pod was *started*
  - the pod's *quality-of-service* (QoS) class
  - what *phase* the pod is in,
  - the *conditions* of the pod, and
  - the *state* of its individual *containers*.

* **Pod Phase**
  - *Pending*
  - *Running*
  - *Succeeded*
  - *Failed*
  - *Unknown*

* **Pod Condition**
  - *PodScheduled*
  - *Initialized*
  - *ContainersReady*
  - *Ready*

* Each condition is either `fulfilled` or `not`.

* *Container State*
  - *Waiting*
  - *Running*
  - *Terminated*
  - *Unknown*

* Kubernetes *never restarts* a container,
  but instead discards it and
  *creates a new container*.
  Regardless, we *call* this
  *restarting a container*.

* If init containers are defined in the pod and
  one of the pod's regular containers is restarted,
  the *init containers are not executed again*.

* **Restart Policy**
  - *Always* (default)
  - *OnFailure*
  - *Never*

* Kubernetes can be configured to check whether
  an application is still alive by
  defining a **liveness probe**.
  - *Liveness probes* can only be used in the
    pod's regular containers. They can't be
    defined in *init containers*.

* Unlike *liveness probes*, it's perfectly normal
  for a *startup probe* to fail. A failure only
  indicates that the application hasn't yet been
  completely started. A successful *startup probe*
  indicates that the application has started
  successfully, and Kubernetes should
  *switch to the liveness probe*.

* You may also want to run additional processes
  every time a container starts and just
  before it stops. You can do this by adding
  *lifecycle hooks* to the container. Two types
  of hooks are currently supported:
  - *Post-start hooks*, which are executed
    when the container starts, and
  - *Pre-stop hooks*, which are executed
    shortly before the container stops.
* These lifecycle hooks are *specified per container*,
  as opposed to *init containers*,
  which are *specified at the pod level*.

* Like liveness probes, lifecycle hooks
  can be used to either
  - execute a command inside the container, or
  - send an `HTTP GET` request to the
    application in the container.

* Another problem with `HTTP GET` *post-start* hooks
  is that Kubernetes doesn't treat the hook as failed
  if the HTTP server responds with status code
  such as `404 Not Found`.

* If the `imagePullPolicy` is set to `Always` and
  the image registry is *offline*, the container will
  not run even if the same image
  is already stored locally.

* When the first *init container* is complete, the
  image for the *next init container* is pulled and
  the container is started. This process is repeated
  until all init containers are successfully completed.

* Init containers are normally only executed once.
  Even if one of the pod's main containers is
  terminated later, the pod's init containers
  are not re-executed.

* When all *init containers* are successfully
  completed, the pod's regular containers
  are all created in parallel.

* Perhaps surprisingly, if the restart policy is
  set to `Never` and the startup hook fails,
  the pod's status is shown as `Completed`
  *even though the post-start hook failed*.

* The pod's containers are terminated in parallel.

* Any time you delete a pod, the pod's
  `terminationGracePeriodSeconds` determines the
  amount of time the pod is given to shut down,
  but you can override this time when you execute
  the `kubectl delete` command using the
  `--grace-period` command line option.

## Mounting storage volumes into the Pod's containers

* A *volume* is defined at the *pod level* and then
  mounted at the desired location in the container.

* The lifecycle of a volume is tied to the lifecycle
  of the entire pod and is independent of the
  lifecycle of the container in which it is mounted.

* All volumes in a pod are created when the pod is
  set up - *before* any of its containers are started.
  They are torn down when the pod is shut down.

* While technologies such as `Network File System`
  (**NFS**) allow you to attach the volume in
  `read/write` mode on multiple computers, other
  technologies typically available in cloud environments,
  such as the *Google Compute Engine Persistent Disk*,
  allow the volume to be used either in `read/write`
  mode on a single cluster node, or in
  `read-only` mode on many nodes.

* When you add a volume to a pod, you must specify the
  volume type. A wide range of volume types is available.
  - **`emptyDir`**: A simple directory that allows the
    pod to store data for the duration of its life cycle.
  - **`hostPath`**: Used for mounting files from the
    *`worker node's filesystem`* into the pod.
  - **`nfs`**
  - `gcePersistentDisk`, `awsElasticBlockStore`
  - `azureFile`, `azureDisk`
  - **`configMap`**
  - **`secret`**
  - **`downwardAPI`**
  - **`projected`**
  - Special types of volumes used to
    expose information about the pod and other
    Kubernetes objects through files.
  - **`persistentVolumeClaim`**
  - **`csi`**: A pluggable way of adding storage
    via the *Container Storage Interface*.

* **`emptyDir`**
  - This volume type is used in *single-container pods*
    when data must be preserved even if the
    container is restarted.
  - It's also used when the container's filesystem
    is marked *`read-only`*, and you want part of it
    to be writable.
  - In pods with two or more containers, an *`emptyDir`*
    volume is used to share data between them.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quiz
spec:
  volumes:
  - name: quiz-data
    emptyDir: {}
  containers:
  - name: mongo
    image: mongo
    volumeMounts:
    - name: quiz-data
      mountPath: /data/db
```

* The files in an `emptyDir` volume are stored
  in a directory in the *host node's filesystem*.
  It's nothing but a normal file directory.
  - If you delete the pod, the directory is deleted.
    This means that the data is lost once again.
  - Creating the `emptyDir` volume in `memory` is
    also a good idea whenever it's
    used to store sensitive data.
  - The size of an `emptyDir` volume can be limited
    by setting the `sizeLimit` field.

```yaml
volumes:
  - name: content
    emptyDir:
      medium: Memory
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quiz
spec:
  volumes:
  - name: quiz-data
    gcePersistentDisk:
      pdName: quiz-data
      fsType: ext4
  containers:
  - name: mongo
    image: mongo
    volumeMounts:
    - name: quiz-data
      mountPath: /data/db
```

* you can't mount the same *GCE Persistent Disk*
  on multiple hosts *simultaneously* in `read/write`
  mode. You can only mount it on multiple hosts
  if you use the `read-only` mode.

* Use the following command to see which
  network volumes that are attached to a node:

```zsh
kubectl get node node_name -o json \
  | jq .status.volumesAttached
```

* A *network volume* is mounted by the *host node*,
  and then the *pod* is given access to the
  *mount point*.
* The underlying storage technology may not allow
  a volume to be attached to more than one node
  at a time in *`read/write` mode*, but multiple
  pods on the *same node* can all use the
  volume in *`read/write` mode*.

* Replicas of the same pod typically can't use
  the same network volume in `read/write` mode.

* A **`hostPath`** volume points to a specific file
  or directory in the filesystem of the host node.
  Pods running on the same node and using the same
  path in their `hostPath` volume have access to
  the same files, whereas pods on other nodes do not.

* Typically, a **`hostPath`** volume is used in cases
  where the pod needs to read or write files in the
  node's filesystem that the processes running on the
  node read or generate, such as *system-level logs*.
  - The *`hostPath`* volume type is one of the
    *most dangerous volume* types in Kubernetes and
    is usually reserved for use in privileged pods only.

## Persisting application data with PersistentVolumes

* To make pod manifests *portable* across different
  cluster environments, the environment-specific
  information about the actual storage volume is
  moved to a *`PersistentVolume`* object.
  - A *`PersistentVolumeClaim`* object connects the
    pod to this *`PersistentVolume`* object.

* Before a user can use a *persistent volume* in
  their pods, they must first *claim* the volume by
  creating a `PersistentVolumeClaim` object.
  - After claiming the volume, the user has exclusive
    rights to it and can use it in their pods.
  - They can delete the pod at any time, and they
    won't lose ownership of the persistent volume.
  - When the volume is no longer needed, the user
    releases it by *deleting* the
    `PersistentVolumeClaim` object.

* *Multiple pods* can use the same *storage volume* if
  they refer to the *same persistent volume claim* and
  therefore transitively to the *same persistent volume*.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: quiz-data
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  - ReadOnlyMany
  gcePersistentDisk:
    pdName: quiz-data
    fsType: ext4
```

* The *`capacity`* of the volume indicates the
  size of the underlying volume.
  - Each persistent volume must specify its
    capacity so that Kubernetes can determine
    whether a particular persistent volume
    can meet the requirements specified in
    the persistent volume claim
    before it can bind them.
* Each persistent volume must specify a
  list of *`accessModes`* it supports.
  - The access mode determines how many
    **nodes**, not *pods*, can
    attach the volume at a time.
  - *`ReadWriteOnce`*: The volume can be
    mounted by a *single* worker *node*
    in *`read/write` mode*.
  - *`ReadOnlyMany`*: The volume can be
    mounted on *multiple* worker *nodes*
    simultaneously in *`read-only` mode*.
  - *`ReadWriteMany`*: The volume can be
    mounted in *`read/write` mode* on
    multiple worker nodes at the same time.

* **Volume Mode**
  - *Filesystem* (default)
  - *Block*

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: quiz-data
spec:
  resources:
    requests:
      storage: 1Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: ""
  volumeName: quiz-data
```

* The field **must be set to an empty string** if you
  want Kubernetes to bind a `pre-provisioned`
  persistent volume to this claim instead of
  *provisioning a new one*.

* If the cluster administrator creates a bunch of
  persistent volumes with non-descript names,
  and you *don't care which one you get*,
  you can skip the `volumeName` field.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quiz
spec:
  volumes:
  - name: quiz-data
    persistentVolumeClaim:
      claimName: quiz-data
  containers:
  - name: mongo
    image: mongo
    volumeMounts:
    - name: quiz-data
      mountPath: /data/db
```

* When you no longer plan to deploy pods that
  will use this claim, you can delete it.
  This **releases** the persistent volume.
* You might wonder if you can then *recreate* the
  claim and access the *same volume and data*.
* The `STATUS` column shows the volume as `Released`
  rather than `Available`, as was the case initially.
* The `CLAIM` column still shows the quiz-data claim
  to which it was previously bound,
  even if the claim *no longer exists*.
* To make the volume available again, you must
  *delete and recreate* the `PersistentVolume` object.
  - But will this cause the data stored
    in the volume to be lost?
* With a `pre-provisioned` persistent volume like the
  one at hand, deleting the object is equivalent to
  deleting a **data pointer**.
  - The `PersistentVolume` object merely points to a
    GCE Persistent Disk. It doesn't store the data.
  - If you delete and recreate the object, you end up
    with a *new pointer* to the same GCE PD
    and thus *the same data*.
* An alternative way of making a persistent volume
  available again is to edit the `PersistentVolume`
  object and remove the `claimRef`
  from the spec section.

* **Reclaim policy**:
  - `PersistentVolume.spec.persistentVolumeReclaimPolicy`
  - **`Retain`**: This is the *default* policy for
    *manually created* persistent volumes.
  - **`Delete`**: This is the *default* policy for
    *dynamically provisioned* persistent volumes

* The *`ReadWriteOnce`* mode doesn't mean that only a
  single pod can use it, but that a single node can
  *attach the volume*.
* You don't need `ReadWriteMany` for multiple pods to
  write to the volume if they are on the *same node*.
  - As explained before, the word `"Once"` in
    `ReadWriteOnce` refers to **nodes**, not **pods**.
* If the claim supports access mode `ReadOnlyMany`,
  why can't both nodes attach the volume and
  run the reader pods? This is caused by the writer pods.
  The first node attached the persistent volume in
  *`read-write`* mode. This **prevents** other nodes
  from attaching the volume, *even in `read-only` mode*.
* Kubernetes can't *detach the volume* or
  *change the mode* in which it is attached
  while it's being used by pods.

* The `ReadOnlyMany` access mode doesn't need
  further explanation. If no pod mounts the volume in
  `read-write` mode, any number of pods can use
  the volume, even on many different nodes.

* When using **manually provisioned** persistent volumes,
  the lifecycle of the underlying storage volume is not
  coupled to the lifecycle of the `PersistentVolume` object.
  - Each time you create the object, its initial status
    is `Available`.
  - When a `PersistentVolumeClaim` object appears,
    the persistent volume is bound to it,
    if it meets the requirements set forth in the claim.
  - Until the claim is bound to the volume,
    it has the status `Pending`; then both the volume
    and the claim are displayed as `Bound`.

* **dynamic provisioning of persistent volumes**
  - If your Kubernetes cluster is managed by a
    cloud provider, it probably already has a
    persistent volume provisioner configured.

* A Kubernetes cluster can run multiple
  persistent volume provisioners, and a single
  provisioner may support several different
  types of storage volumes.
  - When creating a claim, you use the
    `storageClassName` field to specify which
    storage class you want.
  - `kubectl get sc`

* Remember that **omitting** the `storageClassName`
  field causes the *default storage class* to be used,
  whereas explicitly setting the field to **`""`**
  *disables dynamic provisioning* and causes an
  *existing persistent volume* to be selected
  and bound to the claim.

* You'll notice that `StorageClass` objects have
  no *`spec`* or *`status`* sections.
  This is because the object only contains
  *static* information.
  - Regardless of what provisioner is used,
    the volume's *reclaim policy* is set to
    whatever is specified in the *storage class*.

* In summary, a *`StorageClass`* object
  represents a class of storage that
  can be *dynamically provisioned*.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: quiz-data-default
spec:
  resources:
    requests:
      storage: 1Gi
  accessModes:
  - ReadWriteOnce
```

* This `PersistentVolumeClaim` manifest contains only
  the storage size request and the desired access mode,
  but no `storageClassName` field, so the default
  storage class is used.

* Some types of volumes require this type of behavior,
  because the system needs to know where the pod is
  scheduled before it can provision the volume.
* This is the case with provisioners that create
  *`node-local`* volumes, such as the one you find
  in clusters created with the *kind* tool.

* **Volume binding mode**
  - **`Immediate`**
  - The provision and binding of the persistent volume
    takes place *immediately* after the claim is created.
  - Because the consumer of the claim is unknown at
    this point, this mode is only applicable to volumes
    that are can be accessed from *any cluster node*.
  - **`WaitForFirstConsumer`**
  - The volume is provisioned and bound to the claim
    when the first pod that uses this claim is created.
  - This mode is used for *topology-constrained*
    volume types.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: quiz-data-fast
spec:
  storageClassName: fast
  resources:
    requests:
      storage: 1Gi
  accessModes:
  - ReadWriteOnce
```

* If a persistent volume claim refers to a
  *non-existent* storage class, the claim remains
  `Pending` until the storage class is created.

* Kubernetes does not support *changing* the
  *storage class* name in an existing claim.
  - The part that is **mutable** is
    `spec.resources.requests`, which is where
    you indicate the desired size of the volume.
  - To **resize** the persistent volume, you
    may need to *delete and recreate* the pod
    that uses the claim.
  - When the cluster administrator creates a
    storage class, they can use the
    `spec.allowVolumeExpansion` field to
    indicate whether volumes of this
    class can be *resized*.

* The underlying volume is typically provisioned
  **asynchronously**. When the process completes,
  the status of the `PersistentVolume` object
  changes to `Available`; at this point,
  the volume is bound to the claim.
* Users can then deploy pods that refer to the
  claim to gain access to the underlying
  storage volume. When the volume is no longer
  needed, the user deletes the claim. This
  typically triggers the deletion of both
  the `PersistentVolume` object and the
  underlying storage volume.

* The Kubernetes scheduler ensures that the
  pod is always scheduled on the node to
  which the **local volume** is attached.
  - *Local persistent volumes* are also
    better than `hostPath` volumes because
    they offer much better security.

* **Local persistent volumes** are used when
  applications need to access disks that are
  directly attached to nodes.
  - This affects the *scheduling* of the *pods*,
    since the pod must be scheduled to one of
    the nodes that can provide a
    local persistent volume.
  - If the pod is subsequently deleted and
    recreated, it will always be scheduled
    to the **same node**.

## ConfigMaps, Secrets, and the Downward API

* Values that the **YAML** parser might
  interpret as something other than a string
  must be enclosed in *quotes*.
  - This includes *numeric* values such as `1234`,
  - and *Boolean* values such as `true` and `false`.
  - Some other *special strings* must also be *quoted*,
    otherwise they would also be interpreted as
    `Boolean` or other types.
  - These include the values
    `true`, `false`, *`yes`*, *`no`*, *`on`*, *`off`*,
    **`y`**, **`n`**, **`t`**, **`f`**,
    `null`, and *others*.

```yaml
kind: Pod
metadata:
  name: kiada
spec:
  containers:
  - name: kiada
    image: luksa/kiada:0.4
    env:
    - name: POD_NAME
      value: kiada
```

* Since *environment variables* values must be
  *strings*, you must enclose values that aren't
  strings in *quotes* to prevent the YAML parser
  from treating them as anything
  other than a string.

* Referring to an environment variable
  in another variable

```yaml
env:
- name: POD_NAME
  value: kiada
- name: INITIAL_STATUS_MESSAGE
  value: My name is $(POD_NAME).
```

* You can only use the `$(VAR_NAME)` syntax to
  refer to variables defined in the *same manifest*.
* The referenced variable must be *defined*
  *before* the variable that *references* it.
* When you want a variable to contain the
  *literal string* `$(VAR_NAME)` and don't want
  Kubernetes to resolve it, use a *double dollar*
  sign as in `$$(VAR_NAME)`. Kubernetes will remove
  one of the *dollar* signs and skip
  resolving the variable.

* However, you can use a different approach.
  If you run the command through a *shell*,
  you can have the *shell* resolve the variable.

* By default, the hostname is the same as
  the pod's name, but you can override it using
  the hostname field in the pod's spec.
* You can also set the subdomain field so that
  the fully qualified domain name (FQDN)
  of the pod is as follows:
  - `<hostname>.<subdomain>.<pod ns>.svc.<cluster domain>`

* A **`ConfigMap`** is a Kubernetes API object
  that simply contains a list of `key/value` pairs.
* The `key/value` pairs in the config map are
  passed to containers as **environment variables**
  or **mounted as files** in the container's
  filesystem via a **configMap volume**.
* *Keys* in a config map may only consist of
  *alphanumeric* characters, *dashes*,
  *underscores*, or *dots*.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kiada-config
data:
  status-message: This message is set in the config map
```

```yaml
kind: Pod
spec:
  containers:
  - name: kiada
    env:
    - name: INITIAL_STATUS_MESSAGE
      valueFrom:
        configMapKeyRef:
          name: kiada-config
          key: status-message
          optional: true
```

* Using `envFrom` to inject the entire
  config map into environment variables

```yaml
kind: Pod
spec:
  containers:
  - name: kiada
    envFrom:
    - configMapRef:
        name: kiada-config
        optional: true
```

* You can combine entries from *multiple config maps*.
  If two config maps contain the *same key*,
  the *last one* takes precedence.
* You can also combine the `envFrom` field with
  the `env` field if you wish to inject all entries
  of one config map and particular entries of another.
* When an environment variable is configured in
  the `env` field, it takes precedence *over*
  environment variables set in the `envFrom` field.

* A config map manifest containing a multi-line value

```yaml
apiVersion: v1
kind: ConfigMap
binaryData:
  dummy.bin: n29IJxo+rdJ06cz5...
data:
  envoy.yaml: |
    admin:
      access_log_path: /var/log/envoy.admin.log
      address:
        socket_address:
          protocol: TCP
          address: 0.0.0.0
metadata:
  creationTimestamp: null
  name: kiada-envoy-config
```

* If a config map entry contains
  *non-UTF-8* byte sequences, it must be
  defined in the `binaryData` field.
* The values in this field are `Base64`
  encoded, which is how *binary* values
  are represented in YAML.
* In YAML, you can specify *multi-line values*
  using a *pipeline* character and
  appropriate indentation.

* When creating config maps from files,
  make sure that none of the lines in
  the file contain **trailing whitespace**.
* If any line **ends** with **whitespace**,
  the value of the entry in the manifest
  is *formatted as a quoted* string with
  the newline character escaped.

* To make config map entries available as
  files in the container's filesystem,
  you define a `configMap` volume in the
  pod and mount it in the container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-ssl
spec:
  volumes:
  - name: envoy-config
    configMap:
      name: kiada-envoy-config
  containers:
  - name: envoy
    image: luksa/kiada-ssl-proxy:0.1
    volumeMounts:
    - name: envoy-config
      mountPath: /etc/envoy
```

* Because all of the pod's volumes must be
  set up before the pod's containers can
  be started, referencing a missing config map
  in a volume prevents all the containers
  in the pod from starting, not just the
  container in which the volume is mounted.

* `configMap` volumes let you specify which
  config map entries to project into files.

```yaml
volumes:
- name: envoy-config
  configMap:
    name: kiada-envoy-config
    items:
    - key: envoy.yaml
      path: envoy.yaml
```

* The items field specifies the list of
  config map entries to include in the volume.
* Each item must specify the key and the
  file name in the path field.
* Entries not listed here aren't
  included in the volume.
* You can set the default permissions for
  the files in a `configMap` volume by setting
  the `defaultMode` field in the volume definition.
* When specifying file permissions in
  YAML manifests, make sure you never forget
  the leading zero, which indicates that
  the value is in `octal` form. If you omit
  the zero, the value will be treated as `decimal`.
* When you use `kubectl get -o yaml` to display
  the YAML definition of a pod, note that the
  file permissions are represented
  as `decimal` values.

* When you update a config map, the **files**
  in the `configMap` volume are
  automatically updated.
* Unlike files, *environment variables* can't
  be updated while the container is running.
* However, if the container is restarted for
  some reason, Kubernetes will use the new
  config map values when it sets up the
  environment variables for the new container.

* To prevent users from changing the values
  in a config map, you can mark the
  config map as `immutable`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-immutable-configmap
data:
  mykey: myvalue
  another-key: another-value
immutable: true
```

* When a config map is marked as `immutable`,
  the Kubelets on the worker nodes that use
  it don't have to be notified of changes
  to the `ConfigMap` object.
  This reduces the load on the API server.

* If you use the `subPath` field to mount
  individual files instead of the entire
  `configMap` volume, the file **won't** be
  **updated** when you modify the config map.
* To get around this problem, you can mount
  *the entire volume* in another directory
  and create a *symbolic link* in the desired
  location pointing to the file
  in the other directory.

* Every time you *change* the *config map*,
  Kubernetes creates a new *timestamped*
  directory, writes the files to it,
  and then associates the `..data`
  *symbolic* link with this new directory,
  replacing all files *instantaneously*.

* If you use `subPath` in your volume mount
  definition, this mechanism isn't used.
  Instead, the file is written directly to
  the target directory and the file isn't
  updated when you modify the config map.

* The `data` field in `secrets` corresponds to
  the `binaryData` field in `config maps`.
* It can contain `binary` values as
  `Base64-encoded` strings.
* The `stringData` field in secrets is
  equivalent to the `data` field in `config maps`
  and is used to store plain text values.
* This `stringData` field in secrets
  is `write-only`.
* When you read back the `Secret` object,
  any values you added to `stringData` will be
  included in the `data` field as
  `Base64-encoded` strings.

* *Built-in secret type*
  - *`Opaque`* (Default): This type of secret can
    contain secret data stored under arbitrary keys.
  - *`bootstrap.kubernetes.io/token`*: This type of
    secret is used for tokens that are used when
    bootstrapping new cluster nodes.
  - *`kubernetes.io/basic-auth`*: This type of secret
    stores the *credentials* required for basic
    authentication. It must contain the
    `username` and `password` keys.
  - *`kubernetes.io/service-account-token`*: This type
    of secret stores a token that identifies
    a Kubernetes service account.
  - *`kubernetes.io/ssh-auth`*: This type of secret
    stores the *private key* used for SSH authentication.
    The private key must be stored under the
    key *`ssh-privatekey`* in the secret.
  - *`kubernetes.io/tls`*: This type of secrets stores
    a TLS certificate and the associated private key.
    They must be stored in the secret under the key
    *`tls.crt`* and *`tls.key`*, respectively.

* Like *config maps*, the maximum size of a
  secret is approximately `1MB`.
* For obvious reasons, it's not the best idea to
  create `YAML` *manifests* for your *secrets*
  and store them in your version control system,
  as you do with config maps.

```yaml
apiVersion: v1
kind: Secret
data:
  pass: bXktcGFzc3dvcmQ=
  user: bXktdXNlcm5hbWU=
metadata:
  creationTimestamp: null
  name: my-credentials
```

* Since not all sensitive data is in binary form,
  Kubernetes also allows you to specify plain
  text values in secrets by using `stringData`
  instead of the `data` field.

```yaml
apiVersion: v1
kind: Secret
stringData:
  user: my-username
  pass: my-password
```

* The `stringData` field is *`write-only`* and
  can only be used to set values. If you create
  this secret and read it back with
  `kubectl get -o yaml`, the `stringData` field
  is no longer present.
* Instead, any entries you specified in it
  will be displayed in the `data` field as
  `Base64-encoded` values.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-ssl
spec:
  volumes:
  - name: cert-and-key
    secret:
      secretName: kiada-tls
      items:
      - key: tls.crt
        path: example-com.crt
      - key: tls.key
        path: example-com.key
        mode: 0600
  containers:
  - name: envoy
    image: envoyproxy/envoy:v1
    volumeMounts:
    - name: cert-and-key
      mountPath: /etc/certs
      readOnly: true
```

* When you project the entries of a secret
  into a container via a *secret volume*,
  the projected file is not `Base64-encoded`.
  The application doesn't need to decode the file.
  The same is true if the secret entries are
  injected into *environment variables*.
* The files in a secret volume are stored
  in an in-memory filesystem (`tmpfs`),
  so they are less likely to be compromised.

```yaml
containers:
- name: my-container
  env:
  - name: TLS_CERT
    valueFrom:
      secretKeyRef:
        name: kiada-tls
        key: tls.crt
```

* *Kubernetes Downward API*, which allows
  you to expose pod and container metadata
  via environment variables or files.
  - It's simply a way to inject values
    from the pod's `metadata`, `spec`,
    or `status` fields down into the container.
  - You can't use the *Downward API* to inject
    any field from the pod object.
    Only *certain fields* are supported.

```
Field                        Allowed in env    Allowed in volume
metadata.name
metadata.namespace
metadata.uid
metadata.labels              NO
metadata.labels['key']
metadata.annotations         NO
metadata.annotations['key']
spec.nodeName                                  NO
spec.serviceAccountName                        NO
status.podIP                                   NO
status.hostIP                                  NO
```

* Information about the container's computational
  resource constraints is injected via the
  `resourceFieldRef` field. They can all be
  injected into `environment` *variables* and
  via a `downwardAPI` *volume*.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-ssl
spec:
  containers:
  - name: kiada
    image: luksa/kiada:0.4
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.name
    - name: POD_IP
      valueFrom:
        fieldRef:
          fieldPath: status.podIP
    - name: NODE_NAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName
    - name: NODE_IP
      valueFrom:
        fieldRef:
          fieldPath: status.hostIP
```

```yaml
env:
- name: MAX_CPU_CORES
  valueFrom:
    resourceFieldRef:
      resource: limits.cpu
- name: MAX_MEMORY_KB
  valueFrom:
    resourceFieldRef:
      resource: limits.memory
      divisor: 1k
```

* Each `resourceFieldRef` can also specify a **divisor**.
  It specifies which *unit* to use for the value.

* Injecting pod metadata into the container's filesystem

```yaml
volumes:
- name: pod-meta
  downwardAPI:
    items:
    - path: pod-name.txt
      fieldRef:
        fieldPath: metadata.name
containers:
- name: foo
  volumeMounts:
  - name: pod-meta
    mountPath: /pod-metadata
```

* ***Projected volumes*** allow you to combine
  information from multiple *config maps*,
  *secrets*, and the *Downward API* into a
  *single pod volume* that you can then mount
  in the pod's containers. They behave exactly
  like the `configMap`, `secret`, and
  `downwardAPI` volumes you learned about in
  the previous sections of this chapter.
  They provide the same features and are
  configured in almost the same way
  as the other volume types.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-ssl
spec:
  volumes:
  - name: etc-envoy
    projected:
      sources:
      - configMap:
          name: kiada-envoy-config
      - secret:
          name: kiada-tls
          items:
          - key: tls.crt
            path: example-com.crt
          - key: tls.key
            path: example-com.key
            mode: 0600
  containers:
  - name: envoy
    image: envoyproxy/envoy:v1
    volumeMounts:
    - name: etc-envoy
      mountPath: /etc/envoy
      readOnly: true
```

## Organizing objects using labels, selectors, and Namespaces

* Most Kubernetes API object types are **namespaced**,
  but a few are not.
  - `Pods`, `ConfigMaps`, `Secrets`, `PersistentVolumeClaims`,
    and `Events` are all **namespaced**.
  - `Nodes`, `PersistentVolumes`, `StorageClasses`, and
    `Namespaces` themselves are not.
* To see if a resource is *namespaced* or *cluster-scoped*,
  check the `NAMESPACED` column when
  running `kubectl api-resources`.

* `kubectl get ns`

```zsh
default
kube-node-lease
kube-public
kube-system
```

* Namespaces prefixed with `kube-` are reserved
  for Kubernetes system namespaces.

* You can also type `-A` instead of `--all-namespaces`.

* When users use namespaces in a single physical
  cluster, it's as if they each use their own
  virtual cluster. But this is only true up to the
  point of being able to create objects without
  running into naming conflicts.
* Unless explicitly configured to do so, Kubernetes
  doesn't provide network isolation between
  applications running in pods in different namespaces.
* An application running in one namespace can
  communicate with applications running in
  other namespaces.
  - By default, there is *no network isolation*
    between namespaces.
* When you delete the Namespace object, all the
  objects you created in that namespace are
  automatically deleted. You don't need
  to delete them first.

* Remember that the `kubectl get all` command lists
  only *some types of* objects. For example, it
  *doesn't list* `secrets`. Even though the command
  doesn't return anything, this doesn't mean that
  the namespace is empty.
* Here I just want to show you how to figure out
  which object is causing the namespace
  (the delete process) to be stuck.
* Here's a hint: Namespace objects also have a
  status field. While the `kubectl describe` command
  normally also displays the status of the object.
  - `kubectl get ns ns_name -o yaml`

---

* The label prefixes `kubernetes.io/` and `k8s.io/`
  are reserved for Kubernetes components. If you want
  to use a prefix for your labels, use your
  organization's domain name to avoid conflicts.

* The following syntax rules apply to the `label prefix`:
  - Must be a DNS subdomain (must contain only
    *lowercase* alphanumeric characters,
    *hyphens*, *underscores*, and *dots*).
  - Must be *no more* than `253` characters long
    (not including the *slash* character).
  - Must end with a *forward slash*.
  - The prefix must be followed by the
    `label name`, which:
  - Must *begin* and *end* with an
    *alphanumeric character*.
  - May contain *hyphens*, *underscores*,
    and *dots*.
  - May contain *uppercase* letters.
  - May *not be longer* than `63` characters.
* A `label value`:
  - May be *empty*.
  - Must *begin* with an *alphanumeric character*
    if not empty.
  - May contain only *alphanumeric characters*,
    *hyphens*, *underscores*, and *dots*.
  - Must *not* contain *spaces* or
    other *whitespace*.
  - Must be *no more* than `63` characters long.

* If you need to add values that don't follow
  these rules, you can add them as **annotations**
  instead of **labels**.

* **Well-known labels used by Kubernetes**

```
Label key                        Example value     Applied to

kubernetes.io/arch               amd64             Node
kubernetes.io/os                 linux             Node
kubernetes.io/hostname           worker-node2      Node
topology.kubernetes.io/region    asia-southeast1   Node,PV
topology.kubernetes.io/zone      asia-southeast1-c Node,PV
node.kubernetes.io/instance-type micro-1           Node
```

* The Kubernetes community has agreed on a set of
  standard labels that you can add to your objects
  so that `other users and tools`
  can understand them.

```
Label                        Example

app.kubernetes.io/name       quotes
app.kubernetes.io/instance   quotes-foo
app.kubernetes.io/component  database
app.kubernetes.io/part-of    kubia-demo
app.kubernetes.io/version    1.0.0
app.kubernetes.io/managed-by quotes-operator
```

* **Label selectors** allow you to select a
  subset of objects that contain a particular
  label and perform an operation on those objects.
* There are two types of label selectors:
  - **equality-based** selectors, and
  - **set-based** selectors.
* An **equality-based** selector can filter objects
  based on whether the value of a particular label
  is `equal` to or `not equal`
  to a particular value.
  - `app=quote`, `app!=quote`
* **Set-based selectors** are more powerful and
  allow you to specify:
  - a set of values that a particular label must
    have; for example: `app in (quiz, quote)`,
  - a set of values that a particular label must
    not have; for example: `app notin (kiada)`,
  - a particular label key that should be present
    in the object's labels; for example, to select
    objects that have the `app` label,
    the selector is simply `app`,
  - a particular label key that should not be
    present in the object's labels; for example,
    to select objects that do not have the
    `app` label, the selector is `!app`.
* When you filter objects, you can *combine multiple*
  selectors. To be selected, an object must
  **match all** of the specified selectors.
  - `app=quote,rel=canary`

```zsh
k get po -l app=quote,rel=canary
k get po -l 'app in (quiz, quote)'
k get po -l '!rel'
```

> **Make sure** to use **single quotes** around
  `!rel`, so your shell doesn't evaluate
  the `exclamation mark`.

* Scheduling pods to nodes with specific labels

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kiada-front-end
spec:
  nodeSelector:
    node-role: front-end
```

* In the `nodeSelector` field, you can specify
  one or more label keys and values that the
  `node` must match to be eligible to run the pod.
* Note that this field only supports specifying
  an `equality-based` label selector.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ssd-claim
spec:
  selector:
    matchLabels:
      type: ssd
```

* Unlike the node selector in the `Pod` object,
  the label selector in the `PersistentVolumeClaim`
  object supports both `equality-based` and
  `set-based` selectors and uses a
  slightly different syntax.
* As you can see in the listing, you can specify
  multiple expressions. The `PersistentVolume's`
  labels must match all of the specified
  expressions to be selected.
  - You must specify the `key`, `operator`,
    and `values` for each expression.
* The `key` is the `label key` to which the
  selector is applied. The `operator` must be
  *one of* `In`, `NotIn`, `Exists`, and
  `DoesNotExist`. When you use the `In` or `NotIn`
  operators, the values array must *not be empty*,
  but it must be empty when you use the `Exists`
  and `DoesNotExist` operators.

```yaml
spec:
  selector:
    matchExpressions:
    - key: type
      operator: NotIn
      values:
      - ssd
    - key: age
      operator: In
      values:
      - old
      - very-old
```

* The set of fields you can use in a
  **field selector** depends on the object kind.
  The `metadata.name` and `metadata.namespace`
  fields are always supported.
* Like `equality-based` label selectors,
  field selectors support the *equal* (`=` or `==`)
  and *not equal* (`!=`) operator, and you can
  combine multiple field selectors
  by separating them with a `comma`.

```zsh
k get po --field-selector status.phase!=Running
k get po --field-selector status.phase!=Running --all-namespaces
```

* *Like* labels, **annotations** are also `key-value` pairs,
  but they don't store identifying information and
  can't be used to filter objects.
* *Unlike* labels, an **annotation** value can be
  much longer (up to `256 KB`)
  and can contain any character.
* The same rules that apply to `label keys` also
  apply to `annotations keys`.
## Exposing Pods with Services and Ingresses

## Deploying applications using Deployments

## Deploying stateful applications using StatefulSets

## Running special workloads using DaemonSets, Jobs, and CronJobs
