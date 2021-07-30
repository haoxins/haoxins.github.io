---
title: (2021) 初识 Kubeflow, Components~
description: 行到水穷处, 坐看云起时. 偶然值林叟, 谈笑无还期.
date: 2021-07-23
---

* [Kubeflow components](https://www.kubeflow.org/docs/components/)

## Notebooks

* [Kubeflow Public Images](https://console.cloud.google.com/gcr/images/kubeflow-images-public)

* 个人推荐使用 [code-server](https://github.com/cdr/code-server)
  - Run VS Code on any machine anywhere and access it in the browser.
  - `Command + Shift + P` -> `Jupyter: Create New Blank Notebook`

### Use kfp

```
export PATH=$PATH:~/.local/bin

kfp pipeline upload pipeline.yaml --pipeline-name pipeline-1
```

## Pipelines

* [pipelines](https://github.com/kubeflow/pipelines)
* [Metadata](https://github.com/kubeflow/metadata)

> * Kubeflow Pipelines with **Argo** which is the default.
>   - Another Kubeflow Pipelines with **Tekton** comes from IBM

* Kubeflow Pipelines separates its resources by
  Kubernetes namespaces (Kubeflow profiles).

* A pipeline component is a self-contained set of user code,
  packaged as a Docker image,
  that performs one step in the pipeline.
  - 虽然 Airflow 也有 Docker Operator
  - 但是 KFP 明显更加范式统一

* Kubeflow Pipelines SDK v2

```
Pipelines
  - Versions

Experiments
  - Runs
  - Run -> pipeline with a specific version
  - Run -> Archive -> Delete
```

* [Rest APIs](https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/)
* [SDK Docs](https://kubeflow-pipelines.readthedocs.io/en/stable/)

## Training

* [Arena](https://github.com/kubeflow/arena)
* [Katib (AutoML)](https://github.com/kubeflow/katib)

### Operators

* [TensorFlow Operator](https://github.com/kubeflow/tf-operator)
* [MPI Operator](https://github.com/kubeflow/mpi-operator)
* [XGBoost Operator](https://github.com/kubeflow/xgboost-operator)

### TF Jobs

> **Note**: TFJob doesn't work in a user namespace by default
> because of Istio automatic sidecar injection.
> In order to get TFJob running, it needs annotation
> `sidecar.istio.io/inject: "false"` to disable it for TFJob pods.

## Serving

* [KFServing](https://github.com/kubeflow/kfserving)
  - 个人暂未使用

## Auth

```
After Kubeflow is installed and configured,
you will by default be accessing your primary profile.

A profile owns a Kubernetes namespace
of the same name along with
a collection of Kubernetes resources.
Users have view and modify access to their primary profiles.
```

> - [Manual profile creation](https://www.kubeflow.org/docs/components/multi-tenancy/getting-started/#manual-profile-creation)
> - [Managing contributors through the Kubeflow UI](https://www.kubeflow.org/docs/components/multi-tenancy/getting-started/#managing-contributors-through-the-kubeflow-ui)

* [GCP Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  - `GKE` 会为每个 GCP Project 自动创建一个固定的
  - `Workload Identity Pool (PROJECT_ID.svc.id.goog)`
  - 用于 Project 中的所有 GKE Clusters
  - `serviceAccount:PROJECT_ID.svc.id.goog[K8S_NAMESPACE/KSA_NAME]`
  - `PROJECT_ID.svc.id.goog` 是 Cluster 上的 `Workload Identity Pool`
  - `KSA_NAME` 是发出请求的 K8s Service Account 的名称
  - `K8S_NAMESPACE` 是在其中定义了 K8s Service Account 的 K8s Namespace

### Pipelines

* [Connecting to Kubeflow Pipelines on Google Cloud using the SDK](https://www.kubeflow.org/docs/distributions/gke/pipelines/authentication-sdk/)
