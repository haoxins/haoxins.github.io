---
title: Kubeflow Components~
description: 行到水穷处, 坐看云起时. 偶然值林叟, 谈笑无还期.
date: 2021-07-23
---

> After: Kubeflow `1.4`

### Profiles

* If you want to **delete** `Profiles`/`User namespaces`
  - Remove the `profiles`, not remove `ns` directly

### Pipelines

* `Run`: *One time*
* `Job`: *Recurring/Cron*
  - *Every time* `-> Run`

* The Kubeflow Pipelines API service
  *deployment* is `ml-pipeline-ui`.

* [Multi-User mode](https://www.kubeflow.org/docs/components/pipelines/sdk/connect-api/#multi-user-mode)
  - Kubeflow Pipelines **multi-user** support is not available
    in **standalone**, because **multi-user** support depends
    on other Kubeflow components.

* From `1.7.0`
  - [Use argo emissary executor by default](https://argoproj.github.io/argo-workflows/workflow-executors/#emissary-emissary)
  - Output artifacts can be located on
    the base layer (e.g. `/tmp`).
  - `command` **must** be specified for containers.

### Training Operator

* [Kubeflow Training Operator](https://github.com/kubeflow/training-operator)
  - Starting from `v1.3`, this training operator provides
    Kubernetes custom resources that makes it easy to run
    distributed or non-distributed
    `TensorFlow/PyTorch/MXNet/XGBoost`
    jobs on Kubernetes.
  - Before `v1.2` release, Kubeflow Training Operator
    only supports `TFJob` on Kubernetes.

------------------

> Before: Kubeflow `1.3` (2021-10)

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
  - 虽然 *Airflow* 也有 Docker Operator
  - 但是 `KFP` 明显更加范式统一
  - `KFP` 基于 K8s & *Argo workflows*, `dev & debug` 会容易很多

* Kubeflow Pipelines SDK v2

```
Pipelines
  - Versions

Experiments
  - Runs
  - Run -> pipeline with a specific version
  - Run -> Archive -> Delete
```

> `Delete Archived Runs` 才会删除 `Completed Pods`

* [Building Python function-based components](https://www.kubeflow.org/docs/components/pipelines/sdk/python-function-components/)
  - **lightweight**

```
It should not use any code declared outside of the function definition.

Import statements must be added inside the function.

Helper functions must be defined inside this function.

If the function accepts or returns large amounts of data
or complex data types, you must pass that data as a file.

If the function accepts numeric values as parameters,
the parameters must have type hints.
Supported types are int and float.
Otherwise, parameters are passed as strings.

If your component returns multiple small outputs
(short strings, numbers, or booleans),
annotate your function with the `typing.NamedTuple` type hint
and use the `collections.namedtuple` function
return your function's outputs as a new subclass of tuple.

If your function has complex dependencies, choose or build a
container image for your Python function to run in.
```

* Understanding how data is passed between components

```
When Kubeflow Pipelines runs a component,
a container image is started in a Kubernetes Pod
and your component's inputs are passed in as
command-line arguments.
When your component has finished,
the component's outputs are returned as files.

In your component's specification,
you define the components inputs and outputs and
how the inputs and output paths are passed to
your program as command-line arguments.
You can pass small inputs, such as short strings or numbers,
to your component by value. Large inputs, such as datasets,
must be passed to your component as file paths.
Outputs are written to the paths that Kubeflow Pipelines provides.
```

> The function's arguments are decorated
> with the `kfp.components.InputPath`
> and the `kfp.components.OutputPath` annotations.

* [Rest APIs](https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/)
* [SDK Docs](https://kubeflow-pipelines.readthedocs.io/en/stable/)

## Training

* [Arena](https://github.com/kubeflow/arena)
  - Arena's goal is to make the data scientists
    feel like to work on a single machine
    but with the Power of GPU clusters indeed.
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

```zsh
git clone https://github.com/kubeflow/tf-operator

cd tf-operator/examples/v1/mnist_with_summaries

kubectl apply -f tfevent-volume

kubectl apply -f tf_job_mnist.yaml
```

```zsh
kubectl -n kubeflow get tfjob mnist -o yaml

kubectl -n kubeflow delete tfjob mnist
```

## AutoML/Katib

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
