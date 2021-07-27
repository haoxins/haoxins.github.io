---
title: (2021) 初识 Kubeflow, Components~
description: 行到水穷处, 坐看云起时. 偶然值林叟, 谈笑无还期.
date: 2021-07-23
---

* (Kubeflow components)[https://www.kubeflow.org/docs/components/]

## Notebooks

## Pipelines

* [pipelines](https://github.com/kubeflow/pipelines)
* [Metadata](https://github.com/kubeflow/metadata)

* UI 简陋, 远不如 [Airflow](https://github.com/apache/airflow)
* A pipeline component is a self-contained set of user code,
  packaged as a Docker image,
  that performs one step in the pipeline.
  - 虽然 Airflow 也有 Docker Operator
  - 但是 KFP 明显更加范式统一
* Kubeflow Pipelines SDK v2

## Training

* [Arena](https://github.com/kubeflow/arena)
* [Katib (AutoML)](https://github.com/kubeflow/katib)
* [TensorFlow Operator](https://github.com/kubeflow/tf-operator)
* [XGBoost Operator](https://github.com/kubeflow/xgboost-operator)
* [MPI Operator](https://github.com/kubeflow/mpi-operator)

### TF Jobs

> **Note**: TFJob doesn't work in a user namespace by default
> because of Istio automatic sidecar injection.
> In order to get TFJob running, it needs annotation
> `sidecar.istio.io/inject: "false"` to disable it for TFJob pods.

## Serving

* [KFServing](https://github.com/kubeflow/kfserving)
  - 个人暂未使用
