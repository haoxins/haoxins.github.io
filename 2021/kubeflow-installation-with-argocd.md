---
title: 初识 Kubeflow, 使用 ArgoCD 安装~ (Outdated)
description: 人生代代无穷已, 江月年年望相似. 不知江月待何人, 但见长江送流水.
date: 2021-08-04
---

* **Outdated!!!**

* [argoflow/argoflow](https://github.com/argoflow/argoflow)
  - [argoflow/argoflow-gcp](https://github.com/argoflow/argoflow-gcp)

### Enable GCP APIs

```zsh
gcloud services enable \
  compute.googleapis.com \
  container.googleapis.com \
  cloudresourcemanager.googleapis.com \
  servicemanagement.googleapis.com \
  iamcredentials.googleapis.com \
  iam.googleapis.com \
  iap.googleapis.com
```

### Create 一个 K8s cluster

* **ENVs**

```zsh
export PROJECT_ID=$(gcloud config get-value project)
export CLUSTER_NAME=kubeflow-sg
export CLUSTER_ZONE=asia-southeast1-c
```

```zsh
gcloud container clusters create $CLUSTER_NAME \
  --project=$PROJECT_ID \
  --workload-pool=$PROJECT_ID.svc.id.goog \
  --machine-type=n1-standard-8 \
  --enable-autoscaling --min-nodes 3 --max-nodes 99 \
  --scopes compute-rw,gke-default,storage-rw \
  --num-nodes=3 \
  --zone=$CLUSTER_ZONE
# Why --min-nodes 3
# Some components need HA as default.
```

> 基本是最低资源配置了 :)

* Describe the cluster

```zsh
gcloud container clusters describe $CLUSTER_NAME \
  --project=$PROJECT_ID \
  --zone=$CLUSTER_ZONE
```

* If you want to delete

```zsh
gcloud container clusters delete $CLUSTER_NAME \
  --zone=$CLUSTER_ZONE
```

### Install ArgoCD

```zsh
cd argoflow-gcp
```

```zsh
kubectl apply -k ./distribution/argocd/base
```

* If you want to login ArgoCD UI

```zsh
# port forward
kubectl port-forward svc/argocd-server -n argocd 8080:80
# username: admin, get password
kubectl -n argocd get secret \
  argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

### Install Kubeflow

* [Follow this](https://github.com/argoflow/argoflow-gcp#installing-kubeflow)
  - `kubeflow/common/user-namespace/params.env`
  - `kubeflow/common/dex-istio/configmap-patch.yaml`
  - `metallb/configmap.yaml`

```zsh
kubectl apply -f ./distribution/kubeflow.yaml
```

```zsh
kubectl -n istio-system get svc

kubectl port-forward \
  -n istio-system svc/istio-ingressgateway 8088:443
```

### External access

* [GCP Cloud DNS](https://cloud.google.com/dns)

* [GKE Ingress: HTTP(S) Load Balancer](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer)
  - [Create Ingress](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer#creating_an_ingress_resource)
  - [kubernetes/ingress-gce](https://github.com/kubernetes/ingress-gce)

> - [Cloud Load Balancing: HTTP(S)](https://cloud.google.com/load-balancing/docs/https)
> - [Google Cloud Platform ESPv2](https://github.com/GoogleCloudPlatform/esp-v2)
