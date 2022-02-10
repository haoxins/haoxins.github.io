---
title: Istio & WebAssembly & Cilium
description: 弃我去者, 昨日之日不可留; 乱我心者, 今日之日多烦忧.
date: 2021-09-24
---

* https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/

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

* `AuthorizationPolicy` enforcement is activated
  **only if** one of its rules **matches** the
  **source and the operation**.
* The presence of an empty rule means that
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

## WASM

* [WebAssembly for Proxies (ABI specification)](https://github.com/proxy-wasm/spec)
  - 正好最近打算写 `Envoy filter/plugin`

```
Host environment

Sandboxed Wasm VMs communicate with the embedding
host environment (i.e. proxy) using clearly
defined interfaces, that include:
functions exported from the Wasm module,
which proxy can invoke,
helper functions which Wasm VM can invoke,
and Wasm functions for memory management.

Because this interface is very low-level and
fairly stable, it allows us to define a stable ABI
(function prototypes to be defined in a separate document),
which the extensions can use.
```

## Envoy

* 保留端口
  - `:15021/healthz/ready`

## Kiali

```zsh
k get secret -A | grep kiali-service-account

k get secret the_secret_name \
  -o jsonpath={.data.token} | base64 -d

k port-forward svc/kiali \
  20001:20001
```

## Debug

```zsh
k logs -n istio-system -l app=istiod --tail=10000
```

------------------

## Cases & Tips

* `spec.LoadBalancerSourceRanges`
  - `Invalid value: "[59.100.192.6]"`
  - `must be a list of IP ranges. For example, 10.240.0.0/24,10.250.0.0/24`
  - `59.100.192.6` 不行, 得是 `59.100.192.6/32`

* *Connection reset by peer*
  - `EnvoyFilter`
  - `LISTENER`

* *upstream connect error or disconnect/reset before headers*
  - `AuthorizationPolicy`

------------------

## Events

### 2022

* [Open Service Mesh (OSM)](https://github.com/openservicemesh/osm)
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
