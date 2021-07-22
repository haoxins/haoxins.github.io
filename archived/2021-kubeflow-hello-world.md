---
title: (2021) 初识 Kubeflow
description: 行到水穷处, 坐看云起时. 偶然值林叟, 谈笑无还期.
date: 2021-07-22
---

* **2021年7月**, 最近工作需要, 进行 **Kubeflow** 的调研.
  - 调研的目标是:
  - Kubeflow 如果可用, 则完成一些基本的使用场景;
  - 如果不可用, 出具具体的原由.

* [Kubeflow](https://github.com/kubeflow) 是一个 **ML Stack**
  - 由一系列 Components 组成,
  - 可以参见 [kubeflow/manifests](https://github.com/kubeflow/manifests)
  - 由于公司使用的云平台是 [GCP](https://cloud.google.com)
  - 所以本人通过 GKE (Google Kubernetes Engine) 安装并运行 `Kubeflow's components`

* 在本人调研 Kubeflow 的时候, GCP 也有维护的 Kubeflow 服务
  - 比如: AI Platform Pipelines (Kubeflow Pipelines) 等
  - 但是往往在初始化的时候就可能出错 :(
  - 同时, 版本滞后.
  - 比如: GCP Pipelines latest 版本 1.4.1 (2021-02-26)
  - 但开源 latest 版本 1.5.1 (2021-06-20)
  - 未来或许不算啥, 但在早期, 很多 bug 盼着新版本 fix 的阶段, 会急死人的

## Setup

* 不建议在本机 Local 安装, 不管是 Kind, K3s 还是 MicroK8s
  - 一来会有意料之外的报错
  - 二来无法 Scale 做一些基本的性能/花费评估

* 首先, 任意云平台 Setup 一个 K8s cluster

```zsh
export PROJECT_ID=$(gcloud config get-value project)
export CLUSTER_NAME=kubeflow-testing
```

```zsh
gcloud container clusters create $CLUSTER_NAME \
  --project=$PROJECT_ID \
  --cluster-version=latest \
  --machine-type=n1-standard-2 \
  --scopes compute-rw,gke-default,storage-rw \
  --num-nodes=3 \
  --zone=us-central1-a
```

* 截止目前 (2021-07), Kubeflow 的安装
  - 文档不全 & 陈旧
  - 依赖较多, 且各个 Components 更新频繁
  - 个人尝试了不少方式, 现罗列 `3个` 未来依旧有价值的方式

### Kubeflow Pipelines Standalone Deployment

```zsh
export PIPELINE_VERSION=1.6.0
export PIPELINE_MANIFESTS="github.com/kubeflow/pipelines/manifests/kustomize"
```

```zsh
kubectl apply -k "${PIPELINE_MANIFESTS}/cluster-scoped-resources?ref=$PIPELINE_VERSION"

kubectl wait \
  --for condition=established \
  --timeout=60s \
  crd/applications.app.k8s.io

kubectl apply -k "${PIPELINE_MANIFESTS}/env/dev?ref=$PIPELINE_VERSION"
```

> BTW, the Third Party dependencies: Argo, Envoy, MinIO, ML Metadata

* Get the public URL for the Kubeflow Pipelines UI

```zsh
kubectl describe configmap inverse-proxy-config -n kubeflow | grep googleusercontent.com
```

> * Deploy on GCP with Cloud SQL and Google Cloud Storage.
> * Note: This is recommended for production environments.
> * By default, the KFP standalone deployment installs an
>   inverting proxy agent that exposes a public URL.

* Verify that the Kubeflow Pipelines UI is accessible by port-forwarding:

```zsh
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```
