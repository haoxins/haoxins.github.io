---
title: (2021) 初识 Kubeflow, 使用 ArgoCD 安装~
date: 2021-08-04
---

* [argoflow/argoflow](https://github.com/argoflow/argoflow)
  - [argoflow/argoflow-gcp](https://github.com/argoflow/argoflow-gcp)

### Create 一个 K8s cluster

* **ENVs**

```zsh
export PROJECT_ID=$(gcloud config get-value project)
export CLUSTER_NAME=kubeflow-sg-dev
export CLUSTER_ZONE=asia-southeast1-c
```

