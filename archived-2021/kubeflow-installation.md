---
title: 初识 Kubeflow, 安装~ (Outdated)
description: 中岁颇好道, 晚家南山陲. 兴来每独往, 胜事空自知.
date: 2021-07-22
---

* **Warning!!!**, only works for
  - **Kubeflow v1.3**
  - **kpt v0.39**
  - **Kubernetes 1.18**
  - https://github.com/kubeflow/gcp-blueprints/issues/294
  - https://github.com/kubeflow/pipelines/issues/5714

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

* 截止目前 (2021-07), Kubeflow 的安装
  - 文档不全, 依赖较多, 各个 Components 更新频繁
  - 个人尝试了不少方式, 现列举几个未来依旧有价值的方式

### Create 一个 K8s cluster

* **ENVs**

```zsh
export PROJECT_ID=$(gcloud config get-value project)
export CLUSTER_NAME=kubeflow-testing
export CLUSTER_ZONE=us-central1-a
```

```zsh
gcloud container clusters create $CLUSTER_NAME \
  --project=$PROJECT_ID \
  --cluster-version=latest \
  --machine-type=n1-standard-2 \
  --scopes compute-rw,gke-default,storage-rw \
  --num-nodes=3 \
  --zone=$CLUSTER_ZONE
```

* If you want to delete

```zsh
gcloud container clusters delete $CLUSTER_NAME \
  --zone=$CLUSTER_ZONE
```

### Kubeflow Pipelines Standalone Deployment

* **ENVs**

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

> BTW, KFP 的 UI 仅兼容 Chrome

### Kubeflow on GCP/GKE

* Make sure that you have the Owner role for the project in Cloud IAM.

```zsh
gcloud services enable \
  compute.googleapis.com \
  container.googleapis.com \
  iam.googleapis.com \
  servicemanagement.googleapis.com \
  cloudresourcemanager.googleapis.com \
  ml.googleapis.com \
  iap.googleapis.com \
  sqladmin.googleapis.com \
  meshconfig.googleapis.com
```

* [Anthos](https://cloud.google.com/anthos)

```zsh
curl --request POST \
  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
  --data '' \
  https://meshconfig.googleapis.com/v1alpha1/projects/${PROJECT_ID}:initialize
```

> * If you encounter a `Workload Identity Pool does not exist` error,
>   - refer to the following issue:
>   - https://github.com/kubeflow/website/issues/2121

```zsh
gcloud container clusters create tmp-cluster \
  --release-channel regular \
  --workload-pool=${PROJECT_ID}.svc.id.goog \
  --zone=$CLUSTER_ZONE

gcloud container clusters delete tmp-cluster \
  --zone=$CLUSTER_ZONE
```

* gcloud components

```zsh
gcloud components install kubectl kpt anthoscli beta
gcloud components update
# If the output said
# the Cloud SDK component manager is disabled for installation,
# copy the command from output and run it.
```

* Kustomize

```zsh
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash

sudo mv ./kustomize /usr/local/bin/kustomize
```

* yq and jq

```zsh
sudo wget https://github.com/mikefarah/yq/releases/download/3.4.1/yq_linux_amd64 \
  -O /usr/bin/yq && \
  sudo chmod +x /usr/bin/yq

sudo apt install jq
```

* Fetch kubeflow/gcp-blueprints package

```zsh
git clone https://github.com/kubeflow/gcp-blueprints.git
cd gcp-blueprints

git checkout tags/v1.3.0 -b v1.3.0
cd management
# ~/gcp-blueprints/management
```

* **ENVs**

```zsh
export MGMT_PROJECT=$(gcloud config get-value project)
export MGMT_DIR="~/gcp-blueprints/management/"
export MGMT_NAME=kubeflow-mgmt
export LOCATION=${CLUSTER_ZONE}
```

* Configure kpt setter values

```zsh
bash kpt-set.sh

kpt cfg list-setters .
```

* Deploy Management Cluster

```zsh
make apply-cluster

make create-context

make apply-kcc
```

* **ENVs**

```zsh
cd ../kubeflow
# ~/gcp-blueprints/kubeflow

gcloud auth login

export CLIENT_ID=<Your CLIENT_ID>
export CLIENT_SECRET=<Your CLIENT_SECRET>
export KF_PROJECT=$(gcloud config get-value project)
export KF_PROJECT_NUMBER=<Your project number>
export ADMIN_EMAIL=$(gcloud config get-value account)
export MGMTCTXT="${MGMT_NAME}"

export KF_NAME=kubeflow
export CLOUDSQL_NAME="${KF_NAME}-kfp"
export BUCKET_NAME="${KF_PROJECT}-kfp"
export REGION=us-central1
export ZONE=us-central1-a
export ASM_LABEL=asm-193-2
```

* kpt setter config

```zsh
bash ./kpt-set.sh
```

* Management cluster config

```zsh
kubectl config use-context "${MGMTCTXT}"

# Create if not exists
kubectl create namespace "${KF_PROJECT}"
```

```zsh
pushd "../management"
# ~/gcp-blueprints/management

kpt cfg set -R . name "${MGMT_NAME}"
kpt cfg set -R . gcloud.core.project "${MGMT_PROJECT}"
kpt cfg set -R . managed-project "${KF_PROJECT}"

gcloud beta anthos apply ./managed-project/iam.yaml

popd
# ~/gcp-blueprints/kubeflow
```

* Deploy Kubeflow

```zsh
make apply
```

```
If resources can't be created because
webhook.cert-manager.io is unavailable
wait and then rerun make apply

  This issue is being tracked in kubeflow/manifests#1234

If resources can't be created with an error message like:

  error: unable to recognize ".build/application/app.k8s.
  io_v1beta1_application_application-controller-kubeflow.yaml":
  no matches for kind "Application" in version "app.k8s.io/v1beta1"

This issue occurs when the CRD endpoint isn't established
in the Kubernetes API server
when the CRD's custom object is applied.
This issue is expected and can happen multiple times
for different kinds of resource.
To resolve this issue, try running make apply again.
```

* Access the Kubeflow user interface (UI)

```zsh
gcloud projects add-iam-policy-binding "${KF_PROJECT}" \
  --member=user:${ADMIN_EMAIL} \
  --role=roles/iap.httpsResourceAccessor

kubectl -n istio-system get ingress

# port forward
kubectl port-forward \
  -n istio-system svc/istio-ingressgateway 8080:80
```

> [Set up OAuth client](https://www.kubeflow.org/docs/distributions/gke/deploy/oauth-setup/)

```
Name           Nodes  vCPUs  Memory
kubeflow       2      16     64 GB
kubeflow-mgmt  1      4      15 GB
```

* 添加更多的成员

```zsh
gcloud projects add-iam-policy-binding "${KF_PROJECT}" \
  --member=user:<Another OWNER_EMAIL> \
  --role=roles/iap.httpsResourceAccessor
```

### Kubeflow Operator

* [kubeflow/kfctl](https://github.com/kubeflow/kfctl)
  - 个人觉得 *ArgoCD* 部署是较好的方案
  - 即使是 *Operator* 模式, *Kubeflow* 也应该是多个 *Operators*

### Deploying Kubeflow with ArgoCD

* [argoflow/argoflow](https://github.com/argoflow/argoflow)
  - [argoflow/argoflow-gcp](https://github.com/argoflow/argoflow-gcp)

### Others

* [Blog: Running Kubeflow at Intuit: Enmeshed in the service mesh](https://blog.kubeflow.org/running-kubeflow-at-intuit/)
