---
title: (2021) 初识 Kubeflow, 使用 ArgoCD 安装~
description: 人生代代无穷已, 江月年年望相似. 不知江月待何人, 但见长江送流水.
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

```zsh
gcloud container clusters create $CLUSTER_NAME \
  --project=$PROJECT_ID \
  --machine-type=n1-standard-1 \
  --scopes compute-rw,gke-default,storage-rw \
  --num-nodes=3 \
  --zone=$CLUSTER_ZONE
```

* If you want to delete

```zsh
gcloud container clusters delete $CLUSTER_NAME \
  --zone=$CLUSTER_ZONE
```
