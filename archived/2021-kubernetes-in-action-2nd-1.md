---
title: Kubernetes in Action (上) - 2nd Edition
description: 东临碣石, 以观沧海. 水何澹澹, 山岛竦峙.
date: 2021-08-30
---

* [Kubernetes in Action, Second Edition](https://book.douban.com/subject/34986745/)

> Each application must be small enough to
  fit on one of the worker nodes.

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

## Running applications in Pods

## Managing the lifecycle of the Pod's containers

## Mounting storage volumes into the Pod's containers

## Persisting application data with PersistentVolumes

## Configuring applications using ConfigMaps, Secrets, and the Downward API

## Organizing API objects using labels, selectors, and Namespaces

## Exposing Pods with Services and Ingresses

## Deploying applications using Deployments

## Deploying stateful applications using StatefulSets

## Running special workloads using DaemonSets, Jobs, and CronJobs

## Understanding the fine details of the Kubernetes API

## Diving deep into the Control Plane

## Diving deep into the Worker Nodes

## Understanding the internal operation of Kubernetes controllers
