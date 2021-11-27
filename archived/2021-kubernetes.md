---
title: Kubernetes stack, components and cases
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

## K8s common

* [kubectx + kubens](https://github.com/ahmetb/kubectx)

```zsh
k config get-contexts
k config set-context --current --namespace new_ns

k exec --stdin --tty pod_name -- bash
k exec --stdin --tty pod_name -c container_name -- bash
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
k get   po,ev,cm,svc,ns,pv,pvc,secret,deploy,rs
```

```zsh
k rollout status deploy deploy_name
k rollout restart deploy deploy_name
```

### YAML

* `1.4`, `8` 这种值需要注意 *String* or *Number*
  - `"1.4"` or `1.4`
  - `v1.4`, `1.4.0` 是明确的 *String*

------------------

## Argo

```zsh
k port-forward svc/argocd-server \
  -n argocd 8080:80
# Username: admin
# Get password
k get secret argocd-initial-admin-secret \
  -n argocd \
  -o jsonpath="{.data.password}" | base64 -d
```

------------------

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

------------------

## Cert Manager

* An **`Issuer`** is scoped to a *single namespace*,
  and can only fulfill Certificate resources
  within its *own namespace*.

* On the other hand, a **`ClusterIssuer`** is a
  cluster wide version of an Issuer.
  It is able to be referenced by Certificate
  resources in *any namespace*.

### Let's Encrypt: DNS-01

* [Configuring DNS01 Challenge Provider](https://cert-manager.io/docs/configuration/acme/dns01/)
* [Let's Encrypt: DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)
* [GCP: Let's Encrypt DNS-01 Challenge](https://kosyfrances.com/letsencrypt-dns01/)
  - *DNS-01 Challenge Provider* for
    *Let's Encrypt Issuer*
    using *Google CloudDNS*

------------------

## GCP/GKE

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

## Istio

```zsh
istioctl proxy-status

k get envoyfilter -n istio-system
```

```zsh
istioctl analyze -n istio-system
```

```zsh
k get svc istio-ingressgateway \
  -n istio-system \
  -o yaml
```

```zsh
k exec -it deploy/istiod \
  -n istio-system \
  -- curl localhost:15014/metrics

# Aliases:
#   proxy-config, pc

istioctl pc secret \
  deploy/istio-ingressgateway \
  -n istio-system

istioctl pc routes \
  deploy/istio-ingressgateway \
  -n istio-system

istioctl pc listeners \
  deploy/istio-ingressgateway \
  -n istio-system

# Envoy Administration dashboard
k port-forward deploy/istio-ingressgateway \
  -n istio-system 15000
```

### Envoy

* 保留端口
  - `:15021/healthz/ready`

### Kiali

```zsh
k port-forward svc/kiali \
  -n monitoring 20001
```

```zsh
kiali_token_name=$(kubectl get sa \
  kiali-service-account \
  -n monitoring \
  -o jsonpath="{.secrets[0].name}")

k get secret \
  -n monitoring \
  $kiali_token_name \
  -o jsonpath={.data.token} | base64 -d
```

* [Known Problem: Uninstall Hangs](https://kiali.io/documentation/latest/installation-guide#_known_problem_uninstall_hangs)

### WebAssembly

### Debug

```zsh
k logs -n istio-system -l app=istiod --tail=10000
```

------------------

## Jaeger

```zsh
k port-forward svc/jaeger-query \
  -n istio-system 8086:80
# Forwarding from 127.0.0.1:8086 -> 16686
# Forwarding from [::1]:8086 -> 16686
```

------------------

## Cases & Tips

* 更新 `Secrets` 之后, 最好 `Delete` *相关的* `Pods`
  - 否则不会立即生效

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
  需要与 **Certificate** 在同一个 **Namespace**

### Istio

* *Connection reset by peer*
  - `EnvoyFilter`
  - `LISTENER`
* *upstream connect error or disconnect/reset before headers*
  - `AuthorizationPolicy`
