---
title: Istio & WebAssembly
description: 弃我去者, 昨日之日不可留; 乱我心者, 今日之日多烦忧.
date: 2021-09-24
---

------------------

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

* [Announcing Istio 1.12](https://istio.io/latest/news/releases/1.12.x/announcing-1.12/)
  - Istio `1.12` is officially supported on
    Kubernetes versions `1.19` to `1.22`.
  - [Wasm Plugin](https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/)
  - [Telemetry API](https://istio.io/latest/docs/reference/config/telemetry/)
  - [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io)
  - Initial support has been added for
    **gRPC native Proxyless Service Mesh**.
  - Experimental support for `HTTP/3` Gateways.
