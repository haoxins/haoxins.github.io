---
title: Istio and Envoy
description: 弃我去者, 昨日之日不可留; 乱我心者, 今日之日多烦忧.
date: 2021-09-24
---

- https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/

```
downstream ->

Gateway (Envoy Listeners)
  - VirtualService (Envoy Routes)
    - Host (from)
      - Protocol
        - Route
          - DestinationRule (Envoy Clusters)
            - host (dest)
            - subset

ServiceEntry
```

- `AuthorizationPolicy` enforcement is activated
  **only if** one of its rules **matches** the
  **source and the operation**.
- The presence of an empty rule means that
  all requests are allowed.

```yaml
kind: AuthorizationPolicy
spec:
  rules:
  - {}
```

```zsh
istioctl proxy-status
istioctl analyze -n istio-system
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

## Kiali

```zsh
k get secret -n istio-system \
  $(kubectl get sa kiali-service-account \
  -n istio-system \
  -o "jsonpath={.secrets[0].name}") \
  -o jsonpath={.data.token} | base64 -d

k port-forward svc/kiali \
  -n istio-system \
  20001:20001
```

## Debug

```zsh
k logs -n istio-system -l app=istiod --tail=10000
```

------------------

## Cases & Tips

- `spec.LoadBalancerSourceRanges`
  - `Invalid value: "[59.100.192.6]"`
  - `must be a list of IP ranges. For example, 10.240.0.0/24,10.250.0.0/24`
  - `59.100.192.6` 不行, 得是 `59.100.192.6/32`

- Connection reset by peer
  - `EnvoyFilter`
  - `LISTENER`

- upstream connect error or disconnect/reset before headers
  - `AuthorizationPolicy`

------------------

## Events

### 2022

- `2022-11-15`: Announcing Istio `1.16`
  - Kubernetes Gateway API Implementation Promoted to Beta

```
Istio's implementation of the Gateway API has been promoted to Beta.
This is a significant step toward our goal of making the Gateway API
the default API for traffic management in the future.
```

> `2022`年下半年, 个人手头上 Istio 相关项目都交接出去了.
  所以能够以无事一身轻的心态看待这些变化.

- `2022-06-17`: Kubeflow 的 Cluster 有很大的 VMs 之间的网络流量
  - `PILOT_ENABLE_STATUS: true` 删除之后, 解决
  - 应该是某一次升级 (也或许是之前切换 Node pool) 导致
    Istiod 陷入一个 Check status 死循环,
  - 然后导致 Istiod CPU & Memory 上涨,
  - 再导致 Istiod & Istio IngressGateway scale up,
  - 网络流量就爆了.

- [Envoy Gateway](https://github.com/envoyproxy/gateway)
  - `2022-05`, 还只是个没代码的空壳 Repo
  - [Kubernetes Gateway API](https://github.com/kubernetes-sigs/gateway-api)
  - K8s 的号召力真强
  - [wazero](https://github.com/tetratelabs/wazero)
  - The zero dependency WebAssembly runtime for Go developers
  - `2022-06`, 代码已经 Push 出来了, 个人感觉:
    首先, 对 Istio 用户没影响;
    其次, 估计是为了吸引 Nginx, Ingress Nginx 用户

- `2022-04-30`: 关于 Istio 的遐想
  - Istio 越来越专注于 Ingress 了
  - 或许 Mesh 部分将来就交与 Cilium 了

- [Announcing Istio 1.13](https://istio.io/latest/news/releases/1.13.x/announcing-1.13/)
  - Istio `1.13` is officially supported on
    Kubernetes versions `1.20` to `1.23`.

- [Open Service Mesh (OSM)](https://github.com/openservicemesh/osm)
  - [Announcing OSM v1.0.0](https://openservicemesh.io/blog/announcing-osm-v1/)
  - 不看好, 注定凉凉的项目
