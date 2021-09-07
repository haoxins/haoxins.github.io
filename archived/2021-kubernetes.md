---
title: Kubernetes stack
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

```zsh
kubectl api-resources

kubectl explain <kind>
```

## Argo

```zsh
kubectl port-forward svc/argocd-server \
  -n argocd 8080:443
# Username: admin
# Get password
kubectl get secret argocd-initial-admin-secret \
  -n argocd \
  -o jsonpath="{.data.password}" | base64 -d
```

## Grafana

```zsh
kubectl port-forward svc/kube-prometheus-stack-grafana \
  -n monitoring 3000:80
# Username: admin
# Password: prom-operator
```

## Istio

```zsh
istioctl proxy-status
```

```zsh
# 优先使用 Kiali !!!
istioctl analyze -n istio-system
```

```zsh
kubectl get svc istio-ingressgateway \
  -n istio-system \
  -o yaml
```

```zsh
istioctl pc routes deploy/istio-ingressgateway \
  -n istio-system \
  --name http.80
```

```zsh
kubectl exec -it -n istio-system deploy/istiod \
  -- curl localhost:15014/metrics
```

### Envoy

```zsh
# Envoy Administration dashboard
kubectl port-forward deploy/istio-ingressgateway \
  -n istio-system 15000
```

```zsh
istioctl proxy-config listeners \
  deploy/istio-ingressgateway -n istio-system
```

### Kiali

```zsh
kubectl port-forward svc/kiali \
  -n monitoring 20001
```

```zsh
kiali_token_name=$(kubectl get sa \
  kiali-service-account \
  -n monitoring \
  -o jsonpath="{.secrets[0].name}")

kubectl get secret \
  -n monitoring \
  $kiali_token_name \
  -o jsonpath={.data.token} | base64 -d
```

### WebAssembly

## Jaeger

```zsh
kubectl port-forward svc/jaeger-query \
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
kubectl port-forward svc/kube-prometheus-stack-prometheus \
  -n monitoring 9090
# Username: admin
# Password: prom-operator
```

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
