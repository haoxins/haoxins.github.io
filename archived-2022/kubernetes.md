---
title: Kubernetes stack, components and cases
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

## K8s common

* [Lens](https://github.com/lensapp/lens)
* [kubectx + kubens](https://github.com/ahmetb/kubectx)

```zsh
k config get-contexts
k config set-context --current --namespace new_ns

k exec --stdin --tty pod_name -- bash
k exec --stdin --tty pod_name -c container_name -- bash

k top pod pod_name --containers
```

* Options

```zsh
k api-resources
k explain
```

* Shortcuts

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
k get   ev,ns,po,rs,cm,svc,pv,pvc,deploy,secret
```

```zsh
k rollout status deploy deploy_name
k rollout restart deploy deploy_name
```

### YAML

* `1.4`, `8` 这种值需要注意 *String* or *Number*
  - `"1.4"` or `1.4`
  - `v1.4`, `1.4.0` 是明确的 *String*

* `deployment.pod_annotations.sidecar\.istio\.io\/inject`

```yaml
deployment:
  pod_annotations:
    sidecar.istio.io/inject:
    ...
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

------------------

## Etcd

------------------

## Prometheus

* [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)
* [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)

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

* An **`Issuer`** is scoped to a *single namespace*,
  and can only fulfill Certificate resources
  within its *own namespace*.

* On the other hand, a **`ClusterIssuer`** is a
  cluster wide version of an Issuer.
  It is able to be referenced by Certificate
  resources in *any namespace*.

## External DNS

### Let's Encrypt: DNS-01

* [Configuring DNS01 Challenge Provider](https://cert-manager.io/docs/configuration/acme/dns01/)
* [Let's Encrypt: DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)
* [GCP: Let's Encrypt DNS-01 Challenge](https://kosyfrances.com/letsencrypt-dns01/)
  - *DNS-01 Challenge Provider* for
    *Let's Encrypt Issuer*
    using *Google CloudDNS*
  - https://letsencrypt.org/docs/rate-limits/

------------------

## Operator

* Operator Lifecycle Manager (OLM)
  - [Dependency Resolution](https://olm.operatorframework.io/docs/concepts/olm-architecture/dependency-resolution/)

* With `CRDs`, however, each `Kind` will
  correspond to a *single resource*.
* Each controller focuses on one root Kind,
  but may interact with other Kinds.
* A reconciler takes the name of an object, and
  returns whether or not we need to try again.
  - We return an empty result and no error, which
    indicates to controller-runtime that we've
    successfully reconciled this object and don't
    need to try again until there's some changes.
* `config/manager/controller_manager_config.yaml`
------------------

## GCP/GKE

```zsh
export PROJECT_ID=$(gcloud config get-value project)

gcloud container clusters create $PROJECT_ID-sg-test \
  --project=$PROJECT_ID \
  --workload-pool=$PROJECT_ID.svc.id.goog \
  --machine-type=n1-standard-4 \
  --enable-autoscaling --min-nodes 3 --max-nodes 99 \
  --scopes compute-rw,gke-default,storage-rw \
  --num-nodes=3 \
  --zone=asia-southeast1-c
```

* *Storage classes* (Default)

```
standard      kubernetes.io/gce-pd   pd-standard
standard-rwo  pd.csi.storage.gke.io  pd-balanced
premium-rwo   pd.csi.storage.gke.io  pd-ssd
```

* **Workload Identity**
  - 基于 *Google Compute Engine (GCE)* `metadata service`.

```zsh
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/?recursive=true \
  --header "Metadata-Flavor: Google"
```

> - 如果报错: `Request cannot contain header: X-Forwarded-For`
> - 十有八九: `Envoy` 的**锅**

------------------

## Cases & Tips

* Ingress 常见报错

```
response 404 (backend NotFound),
service rules for the path non-existent
```

* 更新 `Secrets` 之后, 最好 `Delete` *相关的* `Pods`
  - 否则不会立即生效
  - `Certificates` 本质上也是 `Secrets`
  - **Prod** 需要**平滑升级**,
    `Create new`, `Apply new`, `Delete later`

* **Jaeger**: 2021-11
  - 把自己的 K8s 上的 **Jaeger** *storage backend* 从
    **Cassandra** 切换到了 **Elasticsearch**
  - The *Jaeger* team recommends *Elasticsearch*
    as the storage backend over *Cassandra*

* **GKE**: 2021-09
  - Updates `default` kubectl from `1.18` to `1.20`.

```zsh
# Default namespaces
default
kube-node-lease
kube-public
kube-system
```

### Cert Manager

* **ClusterIssuer** 的
  `.spec.acme.solvers.dns01.cloudDNS.serviceAccountSecretRef`
  需要与 **Cert Manager** 在同一个 **Namespace**
  - 比如 *Cert Manager* 默认的 `ns`: `cert-manager`
