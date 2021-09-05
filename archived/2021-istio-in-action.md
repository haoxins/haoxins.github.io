---
title: Istio in Action
description: 白云一片去悠悠, 青枫浦上不胜愁. 谁家今夜扁舟子? 何处相思明月楼?
date: 2021-08-04
---

* [Service Mesh Comparison](https://servicemesh.es)
  - *Istio*: Proxy sidecar
  - *Dapr*: Service sidecar

------------------

* [Istio in Action](https://book.douban.com/subject/33406485/)
  - 开篇先说, 要解决的**问题**, *赞*
  - 新技术(在早期)有可能是*毒药*, 过了早期阶段, 大部分就消失了 :)

* Istio **1.10**
* Kubernetes **1.18**

* Although *unit tests* are critical, a strong focus for
  automated testing should be ***scenario or feature tests***.
  - 赞同, 也是我的个人习惯
  - 不能**单纯**面向数字 (*Coverage*) 写 tests

* Lastly, as implementation details change because of
  refactoring, paying down technical debt, maintenance, etc.
  our *feature tests should rarely have to change*.
  - 从个人角度来讲, 单测*早期*针对 *feature tests* 难以覆盖的 codes
  - *后期*则是针对 *hot/key codes*

> * With Istio we can finely control traffic to
    new deployments and reduce the risk of doing deployments.
> * As we aspire to do deployments quickly we should also
    lower the risks of doing those deployments.

* **Challenges**
  - Keeping faults from jumping isolation boundaries
  - Building applications/services capable of
    responding to changes in their environment
  - Building systems capable of running in
    partially failed conditions
  - Understanding what's happening to the overall system
    as it constantly changes and evolves
  - Inability to control the runtime behaviors of the system
  - Implementing strong security as the attack surface grows
  - How to lower the risk of making changes to the system
  - How to enforce policies about `who/what/when` can use
    the components in the system

* Some patterns have evolved to help mitigate these types of
  *scenarios* and help make applications more resilient to
  unplanned, unexpected **failures**:
  - *Client side load balancing* - give the client
    the list of possible endpoints and
    let it decide which to call
  - *Service discovery* - a mechanism for finding the
    periodically updated list of healthy endpoints
    for a particular logical service
  - *Circuit breaking* - shedding load for a period of
    time to a service that appears to be misbehaving
  - *Bulk heading* - limiting client resource usage
    with explicit thresholds (connections, threads, sessions, etc)
    when making calls to a service
  - *Timeouts* - Enforcing time limitations on requests,
    sockets, liveness, etc when making calls to a service
  - *Retries* - Retrying a failed request
  - *Retry budgets* - Applying constraints to retries;
    ie, limiting the number of retries in a given period
    (e.g., can only retry 50% of the calls in a 10s window)
  - *Deadlines* - giving requests context about how long
    a response may still be useful; if outside of
    the deadline, disregard processing the request

> Collectively these types of patterns
  can be though of *"application networking"*.

* To do this, this *"service proxy"* will need to
  understand application constructs like
  messages and requests instead of more
  traditional infrastructure proxies which
  understand connections and packets.
  In other words, we need an **L7 proxy**.

* **Envoy** gives us networking capabilities like
  *retries*, *timeouts*, *circuit breaking*,
  *client-side load balancing*, *service discovery*,
  *security*, and *metrics-collection*
  without any explicit language or framework dependencies.

* This *`proxy+application`* combination forms the
  foundation of a communication bus known as a **service mesh**.

* Together, the *data plane* and the *control plane* provide
  important capabilities necessary in any
  cloud-native architecture such as:
  - Service resilience
  - Observability signals
  - Traffic control capabilities
  - Security
  - Policy enforcement

* Istio can assign *workload identity* and
  embed that into the certificates.
  Istio can use the *identity* of the
  different *workloads* to further
  implement powerful *access-control policies*.

* What are the drawbacks to using a service mesh?
  - for someone unfamiliar with operating Envoy,
    this could look very complex and
    inhibit existing debugging practices.
  - Another drawback of using a service mesh
    is in terms of *tenancy*.
    A mesh is as valuable as there are services
    running in the mesh. That is, the more services
    in the mesh the more valuable the mesh becomes
    to operating those services.
    However, without *proper policy*, *automation*, and *forethought*
    going into the tenancy and isolation models of
    the physical mesh deployment, you could end up in a situation
    where mis-configuring the mesh impacts many services.

## First steps with Istio

* ***istioctl***

* Kubernetes is conceptually implemented as
  a set of *reconciliation controllers*.
  An *operator* is just a user (or in this case, Istio)
  supplied controller.

* The **istio-system** namespace is special in that
  the *control plane* is deployed into it and is able to
  act as a cluster-wide *control plane* for Istio.

* For Istio, the control plane provides the following functions:
  - APIs for operators to specify desired routing/resilience
    behavior APIs for the data plane to consume
    localized configuration Service discovery abstraction
    for the data plane
  - APIs for specifying usage policies
  - Certificate issuance and rotation
  - Assigning workload identity
  - Unified telemetry collection
  - Service-proxy sidecar injection
  - Specifying network boundaries and how to access them

* The bulk of these responsibilities are implemented
  in a *single* component of
  the control plane called **Istiod**.

* This *data-plane* API exposed by Istiod
  implements Envoy's **"discovery APIs"**.
  These discovery APIs, like those for
  service discovery (*Listener Discovery Service* - **LDS**),
  endpoints (*Endpoint Discovery Service* - **EDS**), or
  routing rules (*Route Discovery Service* - **RDS**)
  are known as the **xDS APIs**.

* Istio uses **X.509** certificates to encrypt the traffic.

* *istio-ingressgateway* and *istio-egressgateway*
  - Both of these components are really just *Envoy proxies*
    that can understand Istio configurations.
  - These components reside in the *data plane* and
    are configured very similarly to istio service proxies
    that live with the applications.
  - The only real difference is that they're independent of
    any application workload and are really just to
    let traffic *into* and *out* of the cluster.

* *Istio Ingress Gateway*
  - On a *cloud provider*, it will be the
    public *load balancer* assigned to
    the Kubernetes *service*.

```zsh
istioctl proxy-config routes \
  deploy/istio-ingressgateway.istio-system
```

> To get **metrics**, we will use *Prometheus* and *Grafana*.

## Istio's data plane: Envoy Proxy

* **Listeners** - expose a port to the outside world
  into which application can connect;
  for example, a listener on port 8080 would
  accept traffic and apply any configured
  behavior to that traffic
* **Routes** - rules for how to handle traffic
  that came in on *listeners*;
  for example, if a request comes in and
  matches `/catalog`, then direct that
  traffic to the catalog cluster
* **Clusters** - specific upstream services to
  which Envoy can direct traffic;
  for example, `catalog-v1` and `catalog-v2` can be
  separate clusters and routes can specify rules
  about how traffic can be directed to either
  `v1` or `v2` of the catalog service

* Envoy provides out of the box **load balancing algorithms**
  for the following strategies:
  - *random*
  - *round robin*
  - *weighted*, *least request*
  - *consistent hashing* (sticky)

* Envoy generates a `x-request-id` header to correlate
  calls across services and can also generate the
  `initial x-b3*` headers when tracing is triggered.
* The headers that the *application* is responsible
  for propagating are:
  - `x-b3-traceid`
  - `x-b3-spanid`
  - `x-b3-parentspanid`
  - `x-b3-sampled`
  - `x-b3-flags`

* Envoy filters are written in C++ and compiled into the *Envoy binary*.
  - Additionally, Envoy supports *Lua* scripting and *WebAssembly*
    for a less invasive approach to extending Envoy functionality.

* **Static configuration**
  - We can specify *listeners*, *route rules*, and *clusters*
    using Envoy's configuration file.

* **Dynamic configuration**
  - *Listener Discovery Service* (**LDS**)
  - an API that allows Envoy to query what
    listeners should be exposed on this proxy
  - *Route Discovery Service* (**RDS**)
  - a part of the configuration for listeners that
    specifies which routes to use;
    this is a subset of `LDS` for when static and
    dynamic configuration should be used
  - *Cluster Discovery Service* (**CDS**)
  - an API that allows Envoy to discover what
    clusters and respective configuration for
    each cluster this proxy should have
  - *Endpoint Discovery Service* (**EDS**)
  - a part of the configuration for clusters that
    specifies which endpoints to use for a specific cluster;
    this is a subset of `CDS`
  - *Secret Discovery Service* (**SDS**)
  - an API used to distribute certificates
  - *Aggregate Discovery Service* (**ADS**)
  - a serialized stream of all the changes
    to the rest of the APIs; you can use this single API
    to get all of the changes in order

* One thing to note is that Envoy's xDS APIs are
  built on a premise of *"eventual consistency"* and
  that correct configurations will converge eventually.
* Envoy introduced the *Aggregated Discovery Service* (**ADS**)
  to account for this ordering *race conditions*.
* Istio implements the *Aggregated Discovery Service* and
  uses **ADS** for proxy configuration changes.

* The **Admin API** gives us insight into
  how the proxy is behaving,
  access to its metrics,
  and access to its configuration.
  - `http://proxy:15000/stats`
  - `/certs` - the certificates on the machine
  - `/clusters` - the clusters Envoy is configured with
  - `/config_dump` - dump the actual Envoy config
  - `/listeners` - the listeners Envoy is configured with
  - `/logging` - can view and change logging settings
  - `/stats` - Envoy statistics
  - `/stats/prometheus` - Envoy statistics as prometheus records

* When Istio is deployed on Kubernetes,
  Kubernetes' *service registry* is what
  Istio uses for *service discovery*.
* Other registries can also be used
  like *HashiCorp's Consul*.
* Istio configures the data plane to
  integrate with time-series systems
  like *Prometheus*.
* Istio integrates with the *Jaeger* tracing engine.

## Istio Gateway: getting traffic into your cluster

* **Virtual Hosting**
  - Hosting multiple different services at
    a single entry point is known as **virtual hosting**.
  - We need some way to decide to which *virtual-host*
    group a particular request should be routed.
  - With `HTTP/1.1`, we can use the **Host** *header*,
  - with `HTTP/2` we can use the **:authority** *header*,
  - and with TCP connections we can rely on
    *Server Name Indication* (**SNI**) with TLS.

* Istio uses a *single* Envoy *proxy* as the *ingress gateway*.

* To configure Istio's *`ingress gateway`* to allow
  traffic into the cluster and through the service mesh,
  we'll start by exploring two Istio resources:
  the **Gateway** and **VirtualService** resources.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: coolstore-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "webapp.istioinaction.io"
```

```zsh
istioctl -n istio-system proxy-config \
  listener deploy/istio-ingressgateway
```

* In Istio, a **VirtualService** resource defines how
  a client talks to a specific *service* through its
  fully qualified *domain name*,
  which *versions* of a service are available,
  and other *routing properties*
  (like retries and request timeouts).

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: webapp-vs-from-gw
spec:
  hosts:
  - "webapp.istioinaction.io"
  gateways:
  - coolstore-gateway
  http:
  - route:
    - destination:
        host: webapp
        port:
          number: 8080
```

* *Istio Ingress Gateway* vs *Kubernetes Ingress*
  - *Istio Gateway* handles the `L4` and `L5` concerns
    while *VirtualService* handles the `L7` concerns.
  - https://gateway-api.sigs.k8s.io

* In fact, for production, you should run the
  *ingress gateway* component in its own namespace,
  separate from *istio-system*.

* [cert-manager](https://cert-manager.io)
  - **X.509** certificate management for Kubernetes

* HTTP redirect to HTTPS

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: custom-coolstore-gateway
spec:
  selector:
    istio: custom-ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "webapp.istioinaction.io"
    tls:
      httpsRedirect: true
  - port:
      number: 443
      name: https
      protocol: HTTPS
    tls:
      mode: SIMPLE
      serverCertificate: /etc/istio/ingressgateway-certs/tls.crt
      privateKey: /etc/istio/ingressgateway-certs/tls.key
    hosts:
    - "webapp.istioinaction.io"
```

* **mTLS**

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: coolstore-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "webapp.istioinaction.io"
  - port:
      number: 443
      name: https
      protocol: HTTPS
    tls:
      mode: MUTUAL
      credentialName: webapp-credential-mtls
    hosts:
    - "webapp.istioinaction.io"
```

```zsh
istioctl pc secret -n istio-system \
  deploy/istio-ingressgateway
```

* Serving multiple virtual hosts with TLS

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: coolstore-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 443
      name: https-webapp
      protocol: HTTPS
    tls:
      mode: SIMPLE
      credentialName: webapp-credential
    hosts:
    - "webapp.istioinaction.io"
  - port:
      number: 443
      name: https-catalog
      protocol: HTTPS
    tls:
      mode: SIMPLE
      credentialName: catalog-credential
    hosts:
    - "catalog.istioinaction.io"
```

* *Server Name Indication* (**SNI**)
  - Basically, when a HTTPS connection is created,
    the client first identifies which service it's
    trying to reach using the ClientHello part
    of the TLS *handshake*.
  - Istio's Gateway (Envoy specifically) implements
    SNI on TLS which is how it's able to present
    the correct cert and route to the correct service.

* Traffic routing with *SNI* **Passthrough**
  - All the gateway will do is inspect the
    *SNI headers* and route the traffic to the
    specific backend which will then *terminate*
    the TLS connection.
    The connection will *"pass through"* the gateway
    and be handled by the actual service,
    not the *gateway*.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: sni-passthrough-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 31400
      name: tcp-sni
      protocol: TLS
    hosts:
    - "simple-sni-1.istioinaction.io"
    tls:
      mode: PASSTHROUGH
```

> Although we positioned the *ingress gateway* as
  the single point of ingress, the truth is
  you can and sometimes should have
  **multiple** points of *ingress*.

* How to define and install a new custom gateway

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: my-user-gateway-install
  namespace: istioinaction
spec:
  profile: empty
  values:
    gateways:
      istio-ingressgateway:
        autoscaleEnabled: false
  components:
    ingressGateways:
    - name: istio-ingressgateway
      enabled: false
    - name: my-user-gateway
      namespace: istioinaction
      enabled: true
      label:
        istio: my-user-gateway
```

> This would install *a new gateway* just
  for the *istioinaction* namespace.

* **Gateway injection**
  - With *Gateway injection*, you deploy a
    stubbed-out gateway deployment and
    Istio fills in the rest similar to how
    sidecar injection is done. This way you can
    give a team a stubbed out gateway deployment
    resource and have Istio
    *auto-configure* the rest of it.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-user-gateway-injected
  namespace: istioinaction
spec:
  selector:
    matchLabels:
      ingress: my-user-gateway-injected
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: "true"
        inject.istio.io/templates: gateway
      labels:
        ingress: my-user-gateway-injected
    spec:
      containers:
      - name: istio-proxy
        image: auto
```

* The **Sidecar** resource, however,
  does not apply to gateways.
  When you deploy a new gateway
  (ingress gateway for example),
  the proxy will get configured with all of
  the services available for routing in the mesh.
  The trick is to trim out any of these additional
  configurations for the proxy by including only
  configuration that's relevant to the gateway.

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: control-plane
spec:
  profile: minimal
  components:
    pilot:
      k8s:
        env:
        - name: PILOT_FILTER_GATEWAY_CLUSTER_CONFIG
          value: "true"
  meshConfig:
    defaultConfig:
      proxyMetadata:
        ISTIO_META_DNS_CAPTURE: "true"
    enablePrometheusMerge: true
```

* `PILOT_FILTER_GATEWAY_CLUSTER_CONFIG`
  - This will trimmed down all of the clusters
    in the gateway's proxy configuration to only
    those that are actually referenced in a
    *VirtualService* that applies to the particular gateway.

## Traffic control: fine-grained traffic routing

* Doing a **deployment** to production
  should not impact users running in production
  because it doesn't take any user requests.
* Once we have code **deployed** into production,
  we can make a business decision about
  how to **release** it to our users.
* **Releasing** our code means bringing live
  traffic over to our new deployment.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: catalog
spec:
  host: catalog
  subsets:
  - name: version-v1
    labels:
      version: v1
  - name: version-v2
    labels:
      version: v2
```

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: catalog-vs-from-gw
spec:
  hosts:
  - "catalog.istioinaction.io"
  gateways:
  - catalog-gateway
  http:
  - match:
    - headers:
        x-istio-cohort:
          exact: "internal"
    route:
    - destination:
        host: catalog
        subset: version-v2
  - route:
    - destination:
        host: catalog
        subset: version-v1
```

* Traffic shifting

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: catalog
spec:
  hosts:
  - catalog
  gateways:
  - mesh
  http:
  - route:
    - destination:
        host: catalog
        subset: version-v1
      weight: 90
    - destination:
        host: catalog
        subset: version-v2
      weight: 10
```

* [Argo Rollouts - Progressive Delivery for Kubernetes](https://github.com/argoproj/argo-rollouts)

* Traffic mirroring

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: catalog
spec:
  hosts:
  - catalog
  gateways:
  - mesh
  http:
  - route:
    - destination:
        host: catalog
        subset: version-v1
      weight: 100
    mirror:
      host: catalog
      subset: version-v2
```

* change Istio's default from `"ALLOW_ANY"`
  to `"REGISTRY_ONLY"`. This means,
  we'll only allow traffic to leave the mesh
  if it's explicitly whitelisted
  in the service-mesh registry.

* ***ServiceEntry***
  - The Istio **ServiceEntry** encapsulates
    registry metadata that we can use to insert
    an *entry* into Istio's *service registry*

## Resilience: solving application-networking challenges

* Istio's service proxy implements these
  basic **resiliency patterns** out of the box:
  - Client-side load balancing
  - Locality aware load balancing
  - Timeouts / Retries
  - Circuit breaking

* Client-side load balancing
  - Service operators and developers can configure
    what *load-balancing algorithm* a client uses
    by defining a **DestinationRule**.
  - *Round robin* (default)
  - *Random*
  - *Weighted least request*

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: simple-backend-dr
spec:
  host: simple-backend.istioinaction.svc.cluster.local
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
```

* Istio's ability to load balance across
  locality includes *region*, *zone* and
  even a more fine-grained "subzone".
* Istio's *locality-aware* load balancing
  is enabled by default.
  If you wish to disable it, you can configure
  the `meshConfig.localityLbSetting.enabled`
  setting to be `false`.
* For *locality-aware* load balancing to
  work in Istio, we need to
  configure **health checking**.
  Without *health checking*, Istio does not know
  which endpoints in the load balancing pool
  are unhealthy and what heuristics to use
  to spill over into the next locality.

* By default, Istio will try a call and if it fails,
  *will try 2 more times*.
  This **default retry** will only apply to certain situations.
  These default situations are typically safe
  to retry a request because the indicate network
  connectivity could not be established and that a request
  could not have been sent on first try:
  - *connect-failure*
  - *refused-stream*
  - *unavailable* (gRPC status code `14`)
  - *cancelled* (gRPC status code `1`)
  - *retriable-status-codes* (default to HTTP `503` in Istio)

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: simple-backend-vs
spec:
  hosts:
  - simple-backend
  http:
  - route:
    - destination:
        host: simple-backend
    retries:
      attempts: 2
      retryOn: gateway-error,connect-failure,retriable-4xx
      perTryTimeout: 300ms
      retryRemoteLocalities: true
```

* One thing to note about this setting is that
  the **perTryTimeout** value multiplied by
  the *total attempts* must be lower than
  the *overall request timeout*.

* Naive retry settings (like the default) can
  lead to significant retry "thundering herd" problem.
  For example if a service chain is *5 calls deep* and
  *each* step can retry a request *2 times*,
  we could end up with *32x requests* for
  each incoming request.

* To limit *max number of parallel retries*
  to a fixed number, we can configure
  *`maxRetries`* in our *`DestinationRule`*

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: simple-backend-dr
spec:
  host: simple-backend.istioinaction.svc.cluster.local
  trafficPolicy:
    connectionPool:
      http:
        maxRetries: 3
        http2MaxRequests: 10
        maxRequestsPerConnection: 10
```

* By default, Istio will set *`maxRetries`* to a
  very high number (Max value of unsigned integer)

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: simple-backend-retry-status-codes
  namespace: istioinaction
spec:
  workloadSelector:
    labels:
      app: simple-web
  configPatches:
  - applyTo: CLUSTER
    match:
      context: SIDECAR_OUTBOUND
      cluster:
        portNumber: 80
        service: simple-backend.istioinaction.svc.cluster.local
    patch:
      operation: MERGE
      value:
        circuit_breakers:
          thresholds:
          - retry_budget:
              budget_percent: 20.0
              min_retry_concurrency: 5
```

* In Istio we will use the *`connectionPool`*
  settings in a *`DestinationRule`* to limit
  the number of connections and requests that
  may be piling up when calling a service.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: simple-backend-dr
spec:
  host: simple-backend.istioinaction.svc.cluster.local
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1
      http:
        http1MaxPendingRequests: 1
        maxRequestsPerConnection: 1
        maxRetries: 1
        http2MaxRequests: 1
```

* *Outlier detection*

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: simple-backend-dr
spec:
  host: simple-backend.istioinaction.svc.cluster.local
  trafficPolicy:
    outlierDetection:
      consecutive5xxErrors: 1
      interval: 5s
      baseEjectionTime: 5s
      maxEjectionPercent: 100
```

## Observability

## Securing microservice communication

## Troubleshooting the data plane

## Performance tuning the control plane

## Scaling Istio in your organization

## Extending Istio on the request path

------------------

* [Istio 服务网格技术解析与实践](https://book.douban.com/subject/35001667/)
  - 微信读书, 免费阅读 :)

* Container: 隔离
* Kubernetes: 编排, 调度
* Istio: 流量
  - 控制面
  - 数据面

* 控制面
  - Pilot   流量
  - Mixer   监控
  - Citadel 安全
  - Galley

* **xDS**
  - Envoy 的各种服务发现协议

* `南北向`: 入口请求到集群服务的流量管理
* `东西向`: 集群内服务网格之间的流量管理

* Virtual service
  - Rules

* Service Entry
  - 用于把一个服务添加到 Istio 抽象模型或服务注册表中.
  - 添加服务条目后, Envoy 代理可以将流量发送到服务,
    如同这个添加的服务条目是网格中的其他服务一样.
    使用服务条目有很多方便之处,
    可以管理在网格外部运行的服务的流量.

* Istio 提供两种设置负载均衡的方式
  - 标准负载均衡
  - 会话保持

* SDS (秘钥发现服务)
  - `Envoy 1.8.0` 版本开始引入

* Knative
  - [Serving](https://github.com/knative/serving)
  - [Eventing](https://github.com/knative/eventing)

> * [Build: Tekton Pipelines](https://github.com/tektoncd/pipeline)
