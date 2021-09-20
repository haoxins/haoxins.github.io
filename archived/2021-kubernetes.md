---
title: Kubernetes stack and cases
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

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

```zsh
k logs pod_name -f --all-containers
k get  po       --all-namespaces
k get  ev       -w
k get  po,ev,svc,ns,pv,pvc,secret,deploy
```

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

## Grafana

```zsh
k port-forward svc/kube-prometheus-stack-grafana \
  -n monitoring 3000:80
# Username: admin
k get secret kube-prometheus-stack-grafana \
  -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d
```

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

## Jaeger

```zsh
k port-forward svc/jaeger-query \
  -n istio-system 8086:80
# Forwarding from 127.0.0.1:8086 -> 16686
# Forwarding from [::1]:8086 -> 16686
```

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

## GCP/GKE

* *Storage classes* (Default)

```
standard      kubernetes.io/gce-pd   pd-standard
standard-rwo  pd.csi.storage.gke.io  pd-balanced
premium-rwo   pd.csi.storage.gke.io  pd-ssd
```

## Cert Manager

* An **`Issuer`** is scoped to a *single namespace*,
  and can only fulfill Certificate resources
  within its *own namespace*.

* On the other hand, a **`ClusterIssuer`** is a
  cluster wide version of an Issuer.
  It is able to be referenced by Certificate
  resources in *any namespace*.

## Others

* **GKE**, `1.20.8-gke`

```zsh
# Default namespaces
default
kube-node-lease
kube-public
kube-system
```

* *Kubernetes* 将会是各大*云厂商*和*开源社区*的`边界`
  - 云厂商: *存储*, *网络*, *弹性 VMs*, *API Services*
  - *Kubernetes* 天生就是跑在 *Cloud* 上的

------------------

## Cases

### Istio

* **Connection reset by peer**
  - *`EnvoyFilter`*
