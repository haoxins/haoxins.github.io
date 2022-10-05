---
title: Kubernetes, Kubeflow, and ML Ops
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

## K8s common

- [kubectx + kubens](https://github.com/ahmetb/kubectx)

```zsh
k cp ns/pod:file_full_path -c container target_file_full_path
```

```zsh
k api-resources
k explain
```

- Shortcuts

```zsh
-A  --all-namespaces
-n  --namespace
-l  --selector
-L  --label-columns
```

```zsh
k apply -k kustomization_directory
k logs  pod_name -f --all-containers
k get   ev       -w
k get   ev,ns,po,rs,cm,svc,ds,pv,pvc,deploy,secret
```

```zsh
k rollout status deploy deploy_name
k rollout restart deploy deploy_name
```

### YAML

- `1.4`, `8` 这种值需要注意 `String` or `Number`
  - `"1.4"` or `1.4`
  - `v1.4`, `1.4.0` 是明确的 `String`

- `deployment.pod_annotations.sidecar\.istio\.io\/inject`

```yaml
deployment:
  pod_annotations:
    sidecar.istio.io/inject:
    ...
```

------------------

## ML Ops

### pip

- `~/.config/pip/pip.conf`

### Jupyter

```py
# %env GOOGLE_APPLICATION_CREDENTIALS="/home/jovyan/abc.json"
# Not works, the error is:
# File "/home/jovyan/abc.json" not found
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/jovyan/abc.json"
# This works
```

### Training

```
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1 Score = 2 / ((1 / Precision) + (1 / Recall))
```

------------------

## Argo

```zsh
k port-forward svc/argocd-server \
  -n argocd 8080:443
# Username: admin
# Get password
k get secret argocd-initial-admin-secret \
  -n argocd \
  -o jsonpath="{.data.password}" | base64 -d
```

------------------

## Kyverno

- [Kyverno](https://github.com/kyverno/kyverno)

------------------

## Prometheus

```zsh
# Whenever the Grafana dashboard doesn't provide
# enough details we can query Prometheus directly.
k port-forward svc/kube-prometheus-stack-prometheus \
  -n monitoring 9090
# Username: admin
# Password: prom-operator
```

## Grafana

```zsh
k port-forward svc/kube-prometheus-stack-grafana \
  -n monitoring 3000:80
# Username: admin
k get secret kube-prometheus-stack-grafana \
  -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d
```

------------------

## Cert Manager

- An **`Issuer`** is scoped to a *single namespace*,
  and can only fulfill Certificate resources
  within its *own namespace*.

- On the other hand, a **`ClusterIssuer`** is a
  cluster wide version of an Issuer.
  It is able to be referenced by Certificate
  resources in *any namespace*.

## External DNS

### Let's Encrypt: DNS-01

- [Configuring DNS01 Challenge Provider](https://cert-manager.io/docs/configuration/acme/dns01/)
- [Let's Encrypt: DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)
- [GCP: Let's Encrypt DNS-01 Challenge](https://kosyfrances.com/letsencrypt-dns01/)
  - *DNS-01 Challenge Provider* for
    *Let's Encrypt Issuer*
    using *Google CloudDNS*
  - https://letsencrypt.org/docs/rate-limits/

------------------

## K8s Operator

- A reconciler takes the name of an object, and
  returns whether or not we need to try again.
  - We return an empty result and no error, which
    indicates to controller-runtime that we've
    successfully reconciled this object and don't
    need to try again until there's some changes.
- `config/manager/controller_manager_config.yaml`

------------------

## GCP & GKE

```zsh
gcloud compute ssh node-id
```

- Storage classes (Default)

```
standard      kubernetes.io/gce-pd   pd-standard
standard-rwo  pd.csi.storage.gke.io  pd-balanced
premium-rwo   pd.csi.storage.gke.io  pd-ssd
```

- **Workload Identity**
  - 基于 Google Compute Engine (GCE) metadata service.

```zsh
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/?recursive=true \
  --header "Metadata-Flavor: Google"
```

> - 如果报错: `Request cannot contain header: X-Forwarded-For`
> - 十有八九: `Envoy` 的**锅**

------------------

## Cases & Tips

- Ingress 常见报错

```
response 404 (backend NotFound),
service rules for the path non-existent
```

- 更新 `Secrets` 之后, 最好 `Delete` *相关的* `Pods`
  - 否则不会立即生效
  - `Certificates` 本质上也是 `Secrets`
  - **Prod** 需要**平滑升级**,
    `Create new`, `Apply new`, `Delete later`

- **GKE**: 2021-09
  - Updates `default` kubectl from `1.18` to `1.20`.

```zsh
# Default namespaces
default
kube-node-lease
kube-public
kube-system
```

### Cert Manager

- **ClusterIssuer** 的
  `.spec.acme.solvers.dns01.cloudDNS.serviceAccountSecretRef`
  需要与 **Cert Manager** 在同一个 **Namespace**
  - 比如 *Cert Manager* 默认的 `ns`: `cert-manager`

------------------

## Events

### 2022

- [Apache Flink Kubernetes Operator 1.0.0 Release Announcement](https://flink.apache.org/news/2022/06/05/release-kubernetes-operator-1.0.0.html)
  - `05 Jun 2022`
  - Flink `1.15` (Recommended)
  - What's Next?
  - Auto-scaling using Horizontal Pod Autoscaler

- 我喜欢的 JupyterLab `v3.4` 细节优化
  - 即时地 Python __lint__ 提示
  - 即时地 Python __hint__ 展示
  - 字体等 UI 优化

- [Indexed Job for Parallel Processing with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/)
  - FEATURE STATE: Kubernetes `v1.24`

- `2022-04-30`: 关于 K8s 下一代的遐想
  - 下一代大概率不会影响到 使用者, 而是 提供者, 比如: 云厂商
  - __kubelet__ 应该是改革重点
  - kubelet 和 __Linux kernel__ 应该更紧密, 甚至整合
  - kubelet 应该深度整合 __WebAssembly__

- 2022-04-25: Incident with GitHub Packages and GitHub Pages
  - 尤其是很多开源项目的 Images, 逐步都迁移到了 GitHub

- `2022-04`, 公司内部在推 [Splunk](https://www.splunk.com)
  - 我个人是**不认可**这个选择的
  - [OpenTelemetry](https://github.com/open-telemetry)
  - __OpenTelemetry__: the merger of
    `OpenCensus` (metrics and traces) and
    `OpenTracing` projects.
  - 个人现在对于 `Open xxx` 这种项目有点审美疲劳,
    有**一点点**道德绑架的感觉.
  - [Grafana](https://github.com/grafana)
  - [Loki logs](https://github.com/grafana/loki)
  - [Tempo tracing](https://github.com/grafana/tempo)
  - [Mimir Prometheus](https://github.com/grafana/mimir)

- [Google Cloud](https://cloud.google.com) 是真不行!
  - 靠谱的产品估计只有: __GCS__ (对象存储), __GKE__ (K8s), BigQuery
  - __GKE__ 的 `StorageClass` 居然不支持 `ReadWriteMany`
  - 难怪 GCP 没啥市场份额

- 2022-04: 删除了自己维护的 K8s clusters 上的
  [Jaeger](https://github.com/jaegertracing/jaeger)
  和
  [Prometheus](https://github.com/prometheus/prometheus)
  - 期待 [Grafana Tempo](https://github.com/grafana/tempo)
  - 还有 [Grafana Mimir](https://github.com/grafana/mimir)

- **Kubeflow** 的社区问题!
  - `2021` 年, 我个人对 [Kubeflow](https://github.com/kubeflow/kubeflow) 社区的评价较差
  - 几乎处于**无人维护**的状态
  - [Training operator](https://github.com/kubeflow/training-operator)
  - [Kubeflow pipelines](https://github.com/kubeflow/pipelines)
  - 等子项目还稍微好些
  - 或许该思考下如何重新组装 `Kubeflow` 了
  - [MLflow](https://github.com/mlflow)
  - [Ray](https://github.com/ray-project)
  - 是不错的候选, 尤其是 **Ray**
