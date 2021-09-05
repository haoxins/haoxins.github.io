---
title: Kubernetes in Action - 2nd Edition
description: 东临碣石, 以观沧海. 水何澹澹, 山岛竦峙. 树木丛生, 百草丰茂. 秋风萧瑟, 洪波涌起.
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

## Introducing the Kubernetes API objects

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

## Deploying highly-available clusters

## Managing the computing resources available to Pods

## Advanced scheduling using affinity and anti-affinity

## Automatic scaling using the HorizontalPodAutoscaler

## Securing the Kubernetes API using RBAC

## Protecting cluster nodes with PodSecurityPolicies

## Locking down network communication using NetworkPolicies

## Upgrading, backing up, and restoring Kubernetes clusters

## Adding centralized logging, metrics, alerting, and tracing

## Best practices for Kubernetes application development and deployment

## Extending Kubernetes with CustomResourceDefinitions and operators
