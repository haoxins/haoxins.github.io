---
title: Cilium, Envoy, Istio and WebAssembly
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

- *Connection reset by peer*
  - `EnvoyFilter`
  - `LISTENER`

- *upstream connect error or disconnect/reset before headers*
  - `AuthorizationPolicy`

------------------

## Events

### 2022

- [Envoy Gateway](https://github.com/envoyproxy/gateway)
  - `2022-05`, 还只是个没代码的空壳 Repo
  - [Kubernetes Gateway API](https://github.com/kubernetes-sigs/gateway-api)
  - K8s 的号召力真强
  - [wazero](https://github.com/tetratelabs/wazero)
  - The zero dependency WebAssembly runtime for Go developers

- `2022-04-30`: 关于 Istio 的遐想
  - Istio 越来越专注于 Ingress 了
  - 或许 Mesh 部分将来就交与 Cilium 了

- [Announcing Istio 1.13](https://istio.io/latest/news/releases/1.13.x/announcing-1.13/)
  - Istio `1.13` is officially supported on
    Kubernetes versions `1.20` to `1.23`.

- [Open Service Mesh (OSM)](https://github.com/openservicemesh/osm)
  - [Announcing OSM v1.0.0](https://openservicemesh.io/blog/announcing-osm-v1/)
  - 不看好, 注定凉凉的项目

### 2021

* [Announcing the alpha availability of WebAssembly Plugins](https://istio.io/latest/blog/2021/wasm-api-alpha/)
  - Introduction to the new Wasm Plugin API and
    updates to the Wasm-based plugin
    support in Envoy and Istio.

```yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: your-filter
spec:
  selector:
    matchLabels:
      app: server
  phase: AUTHN
  priority: 10
  pluginConfig:
    someSetting: true
    someOtherSetting: false
    youNameIt:
    - first
    - second
  url: docker.io/your-org/your-filter:1.0.0
```

* [Announcing Istio 1.12](https://istio.io/latest/news/releases/1.12.x/announcing-1.12/)
  - Istio `1.12` is officially supported on
    Kubernetes versions `1.19` to `1.22`.
  - [Wasm Plugin](https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/)
  - [Telemetry API](https://istio.io/latest/docs/reference/config/telemetry/)
  - [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io)
  - Initial support has been added for
    **gRPC native Proxyless Service Mesh**.
  - Experimental support for `HTTP/3` Gateways.
