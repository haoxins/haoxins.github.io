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


## ConfigMaps, Secrets, and the Downward API

## Organizing objects using labels, selectors, and Namespaces

## Exposing Pods with Services and Ingresses

## Deploying applications using Deployments

## Deploying stateful applications using StatefulSets

## Running special workloads using DaemonSets, Jobs, and CronJobs

## Understanding the fine details of the Kubernetes API

## Diving deep into the Control Plane

## Diving deep into the Worker Nodes

## Understanding the internal operation of Kubernetes controllers
