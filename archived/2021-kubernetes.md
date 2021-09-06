---
title: Kubernetes stack
description: 汉下白登道, 胡窥青海湾. 由来征战地, 不见有人还.
date: 2021-08-24
---

## Argo

```zsh
kubectl port-forward svc/argocd-server -n argocd 8080:443
# Username: admin
# Get password
kubectl -n argocd get secret \
  argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

## Istio WebAssembly

## Prometheus

* [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)
* [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)

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
