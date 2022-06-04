---
title: Istio in Action
description: 白云一片去悠悠, 青枫浦上不胜愁. 谁家今夜扁舟子? 何处相思明月楼?
date: 2021-08-04
---

* [Service Mesh Comparison](https://servicemesh.es)
  - Istio: Proxy sidecar
  - Dapr: Service sidecar

------------------

* [Istio in Action](https://book.douban.com/subject/33406485/)
  - https://www.manning.com/books/istio-in-action
  - 开篇先说, 要解决的**问题**, 赞
  - 新技术(在早期)有可能是毒药, 过了早期阶段, 大部分就消失了 :)

* Istio **1.10**
* Kubernetes **1.18**

* Although unit tests are critical, a strong focus for
  automated testing should be **scenario or feature tests**.
  - 赞同, 也是我的个人习惯
  - 不能**单纯**面向数字 (`Coverage`) 写 tests

* Lastly, as implementation details change because of
  refactoring, paying down technical debt, maintenance, etc.
  our *feature tests should rarely have to change*.
  - 从个人角度来讲, 单测*早期*针对 *feature tests* 难以覆盖的 codes
  - *后期*则是针对 *hot/key codes*

> - With Istio we can finely control traffic to
    new deployments and reduce the risk of doing deployments.
> - As we aspire to do deployments quickly we should also
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
  - For someone unfamiliar with operating Envoy,
    this could look very complex and
    inhibit existing debugging practices.
  - Another drawback of using a service mesh
    is in terms of *tenancy*.
    A mesh is as valuable as there are services
    running in the mesh. That is, the more services
    in the mesh the more valuable the mesh becomes
    to operating those services.
  - However, without *proper policy*, *automation*,
    and *forethought* going into the tenancy and
    isolation models of the physical mesh deployment,
    you could end up in a situation where
    mis-configuring the mesh impacts many services.

## First steps with Istio

* **istioctl**

* Kubernetes is conceptually implemented as
  a set of *reconciliation controllers*.
  - An `operator` is just a user (or in this case, Istio)
    supplied controller.

* The **istio-system** namespace is special in that
  the *control plane* is deployed into it and is able to
  act as a cluster-wide *control plane* for Istio.

* For Istio, the control plane provides the following functions:
  - APIs for operators to specify
    `desired routing`/`resilience behavior`
  - APIs for the data plane to consume localized configuration
  - Service discovery abstraction for the data plane
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
* These discovery APIs, like those for
  - service discovery (*Listener Discovery Service* - **LDS**),
  - endpoints (*Endpoint Discovery Service* - **EDS**), or
  - routing rules (*Route Discovery Service* - **RDS**)
  - are known as the **xDS APIs**.

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
    - webapp.istioinaction.io
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
  - webapp.istioinaction.io
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
    - webapp.istioinaction.io
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
    - webapp.istioinaction.io
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
    - webapp.istioinaction.io
  - port:
      number: 443
      name: https
      protocol: HTTPS
    tls:
      mode: MUTUAL
      credentialName: webapp-credential-mtls
    hosts:
    - webapp.istioinaction.io
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
    - webapp.istioinaction.io
  - port:
      number: 443
      name: https-catalog
      protocol: HTTPS
    tls:
      mode: SIMPLE
      credentialName: catalog-credential
    hosts:
    - catalog.istioinaction.io
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
  - The connection will *"pass through"* the gateway
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
    - simple-sni-1.istioinaction.io
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
    sidecar injection is done.
  - This way you can give a team a stubbed out
    gateway deployment resource and have Istio
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
* When you deploy a new gateway
  (ingress gateway for example),
  the proxy will get configured with all of
  the services available for routing in the mesh.
* The trick is to trim out any of these additional
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
  - catalog.istioinaction.io
  gateways:
  - catalog-gateway
  http:
  - match:
    - headers:
        x-istio-cohort:
          exact: internal
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

* **ServiceEntry**
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
* Without *health checking*, Istio does not know
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

* Mean Time To Recovery (MTTR)

* This definition is based on the study of
  **control theory** first introduced in a paper from
  **"On the General Theory of Control Systems"** in 1960.
  - 一下子, *段位*就上来了, 哈哈哈

* Istio helps with one part of observability:
  *application-level network* instrumentation.

* Monitoring is a subset of observability.
* **Observability** supposes our systems are
  highly unpredictable and we cannot know
  all of the possible failure modes in advance.

```yaml
metadata:
  annotations:
    sidecar.istio.io/statsInclusionPrefixes: \
      "cluster.outbound|80||catalog.istioinaction.svc.cluster.local"
```

* Envoy has a notion of `"internal origin"`
  vs `"external origin"` when identifying traffic.

* To view the **control plane metrics**,
  run the following command:

```zsh
kubectl exec -it -n istio-system deploy/istiod \
  -- curl localhost:15014/metrics
```

* *Istio Metrics* with **Prometheus**
  - *Prometheus* is slightly different from other telemetry
    or metrics collection systems in that it **"pulls" metrics**
    from its targets rather than expects agents
    to "push" metrics to it.
  - In fact, this is how *Prometheus* can be configured to be
    highly available: we can just run *multiple* Prometheus
    servers scraping the same targets.

* All of our applications that have the *Istio service proxy*
  injected will automatically expose these *Prometheus metrics*.

* To configure *Prometheus* to do collect metrics
  from *Istio*, we will use the *Prometheus Operator CRs*
  **ServiceMonitor** and **PodMonitor**.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-component-monitor
  namespace: prometheus
  labels:
    monitoring: istio-components
    release: prom
spec:
  jobLabel: istio
  targetLabels: [app]
  selector:
    matchExpressions:
    - {key: istio, operator: In, values: [pilot]}
  namespaceSelector:
    any: true
  endpoints:
  - port: http-monitoring
    interval: 15s
```

```zsh
kubectl -n prometheus port-forward \
  statefulset/prometheus-prom-kube-prometheus-stack-prometheus 9090
```

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: envoy-stats-monitor
  namespace: prometheus
  labels:
    monitoring: istio-proxies
    release: prom
spec:
  selector:
    matchExpressions:
    - {key: istio-prometheus-ignore, operator: DoesNotExist}
  namespaceSelector:
    any: true
  jobLabel: envoy-stats
  podMetricsEndpoints:
  - path: /stats/prometheus
    interval: 15s
    relabelings:
    - action: keep
      sourceLabels: [__meta_kubernetes_pod_container_name]
      regex: istio-proxy
    - action: keep
      sourceLabels: [
        __meta_kubernetes_pod_annotationpresent_prometheus_io_scrape]
    - sourceLabels: [
        __address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: $1:$2
      targetLabel: __address__
    - action: labeldrop
      regex: "__meta_kubernetes_pod_label_(.+)"
    - sourceLabels: [__meta_kubernetes_namespace]
      action: replace
      targetLabel: namespace
    - sourceLabels: [__meta_kubernetes_pod_name]
      action: replace
      targetLabel: pod_name
```

* A **metric** is a *counter*, *gauge*, or
  *histogram/distribution* of telemetry
  between service calls (inbound/outbound).
* A **metric** can contain many *dimensions*
* We see two *different entries* for
  `istio_requests_total` if the *dimensions differ*.
* **Attributes** are used to define
  the *value of a dimension*.

```zsh
kubectl get envoyfilter -n istio-system
```

```yaml
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      annotations:
        sidecar.istio.io/extraStatTags: \
          upstream_proxy_version,source_mesh_id
      labels:
        app: webapp
```

* *Common Expression Language* (**CEL**)

```zsh
kubectl -n istioinaction exec -it deploy/webapp -c istio-proxy \
  -- curl localhost:15000/stats/prometheus
```

```zsh
kubectl get po -n prometheus
```

```zsh
kubectl -n prometheus port-forward svc/prom-grafana 3000:80

# Username: admin
# Password: prom-operator
```

* *Open Telemetry* is a community-driven framework
  that includes *Open Tracing* which is a specification that
  captures concepts and APIs related to *distributed tracing*.

* A **Span** is a collection of data about a request
  representing a *"unit of work"* within a service or component.
  This data including things like the *"start time"*
  of the operation, the *"end time"*, the *operation name*,
  and a set of tags and logs.
* **Spans** have their own *ID* and
  a *parent ID* which is the *Trace ID*.
* *Istio* can handle *sending the Spans* to
  the distributed tracing engine.
* Istio appends *HTTP headers*, commonly known as the
  *Zipkin tracing headers*, to the request that can be used
  to *correlate subsequent Span objects* to the overall Trace.
* The following *Zipkin tracing headers* are used by
  Istio and the *distributed-tracing* functionality:
  - `x-request-id`
  - `x-b3-traceid`
  - `x-b3-spanid`
  - `x-b3-parentspanid`
  - `x-b3-sampled`
  - `x-b3-flags`
  - `x-ot-span-context`

* We can configure Istio for distributed tracing
  at the global level as well as each individual workload.

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  namespace: istio-system
spec:
  meshConfig:
    defaultConfig:
      tracing:
        zipkin:
          address: zipkin.istio-system:9411
```

```yaml
apiVersion: v1
data:
  mesh: |-
    defaultConfig:
      discoveryAddress: istiod.istio-system.svc:15012
      proxyMetadata: {}
      tracing:
        zipkin:
          address: zipkin.istio-system:9411
    enablePrometheusMerge: true
    rootNamespace: istio-system
    trustDomain: cluster.local
  meshNetworks: "networks: {}"
```

```zsh
istioctl dashboard jaeger --browser=false
# skipping opening a browser http://localhost:16686
```

* `kubectl edit -n istio-system cm istio`

```yaml
apiVersion: v1
data:
  mesh: |-
    accessLogFile: /dev/stdout
    defaultConfig:
      discoveryAddress: istiod.istio-system.svc:15012
      proxyMetadata: {}
      tracing:
        sampling: 10
        zipkin:
          address: zipkin.istio-system:9411
```

* In an application we can add the *`x-envoy-force-trace`*
  header to the request and this will trigger Istio
  to capture the spans and traces for a particular call
  graph generated by a request.

* Adding *tags* to a *span* is a way for an application
  to attach additional metadata to a trace.
* *Custom tags* can then be used for reporting, filtering,
  and otherwise exploring the tracing data.

```yaml
apiVersion: kiali.io/v1alpha1
kind: Kiali
metadata:
  namespace: istio-system
  name: kiali
spec:
  istio_namespace: "istio-system"
  istio_component_namespaces:
    prometheus: prometheus
  auth:
    strategy: anonymous
  deployment:
    accessible_namespaces:
    - "**"
    image_version: operator_version
  external_services:
    prometheus:
      cache_duration: 10
      cache_enabled: true
      cache_expiration: 300
      url: http://prom-kube-prometheus-stack-prometheus.prometheus:9090
```

* Kiali

```zsh
kubectl -n istio-system port-forward deploy/kiali 20001
```

* The last thing we'll point out about *Kiali*
  is it can discover **misconfigurations**
  in Istio resources.
* *Kiali* can also do the following
  Istio resource validations:
  - *VirtualService pointing to non-existant Gateway*
  - *Routing to destinations that do not exist*
  - *More than one VirtualService for the same host*
  - *Service subsets not found*

## Securing microservice communication

* What's *Authentication* and *Authorization*?
  - **Authentication** is the process by which
    a client or server proves its identity using
    *something they know* (a password),
    *something they have* (a device, a certificate),
    or *something they are* (a unique trait such as a fingerprint).
  - **Authorization** is the process of allowing
    or denying an already *authenticated* user to perform
    an operation such as *creating*, *reading*, *updating*,
    or *deleting* a resource.

* **SPIFFE**
  - *Secure Production Identity Framework For Everyone*
  - SPIFFE is a set of open source standards for
    providing identity to workloads in highly
    dynamic and heterogeneous environments.

* *SPIFFE Identity* is an `RFC 3986` compliant
  URI composed in the following format
  - `spiffe://trust-domain/path`, where:
  - The `trust-domain` represents the issuer
    of identity such as an individual or organization
  - The `path` uniquely identifies a workload
    within the trust domain
  - Istio populates this `path` using the
    *service account* under which a
    particular workload runs.
  - This *SPIFFE Identity* is encoded in
    `X509` certificates, also known as
    *SPIFFE Verifiable Identity Document*
    (abbreviated to **SVID**), which
    Istio's control plane mints for workloads.

* The `PeerAuthentication` resource configures
  the proxy to authenticate
  *service-to-service* traffic.
* The `RequestAuthentication` resource configures
  the proxy how to authenticate *end-user* credentials
  against the servers that issued those.
* The `AuthorizationPolicy` resource configures
  the proxy to authorize or reject requests by making
  decisions based on the extracted data,
  by the *former two resources*.

* When we say Istio is *"secure by default"*
  we actually mean *"almost secure by default"*,
  as there is still work on our side,
  to make the mesh even more secure.

* The *`PeerAuthentication`* resource enables configuration
  of workloads to either *strictly require mTLS*, or
  to be *permissive and accept clear-text traffic*,
  using *one of* the following authentication modes:
  **STRICT** or **PERMISSIVE**.
* The mutual authentication mode can be configured
  in different scopes:
  - *Mesh-wide PeerAuthentication* policies apply to
    all workloads of the service mesh
  - *Namespace-wide PeerAuthentication* policies apply
    to all workloads within a namespace
  - *Workload-specific PeerAuthentication* policies apply
    to all workloads that match the selector
    specified in the policy.

* To create a *mesh-wide PeerAuthentication* policy
  it must fullfill two conditions,
  - *firstly*, it must be applied in the Istio
    installation namespace and
  - *secondly*, it must be named *"default"*.

* Most of the time you will be using either
  the **STRICT** or **PERMISSIVE** modes.
  But there are an additional of two modes:
  * **UNSET** - *Inherit the PeerAuthentication*
    policy of the parent
  - **DISABLE** - Do not tunnel the traffic,
    send directly to the service.

* Istio provides the *`AuthorizationPolicy`*
  resource which is a declarative API to define
  *mesh-wide*, *namespace*, or *workload-specific*
  access policies within a service mesh.

* The *`AuthorizationPolicy`* resource specification
  provides three fields to configure and define a policy:
  - The **selector** field defines the subset
    of workloads to which the policy applies
  - The **action** specifies whether this is
    an `ALLOW`, `DENY`, or `CUSTOM` policy.
  - The **action** will only be applied if one of the
    rules matches the request
  - The **rules** field defines a list of rules
    that identify a request for which the policy
    will be activated
* *`AuthorizationPolicy`* enforcement is activated
  only if one of its rules matches the
  source and the operation.

* The fields of a single rule are:
  - The **`from`** field specifies the source of
    the request and it can be one of the following types:
  - *`principals`*: a list of source identities
    (i.e. SPIFFE ID as seen in the mTLS examples).
  - *`namespaces`*: a list of namespaces that
    matches the source namespace.
  - *`ipBlocks`*: a list of single IP addresses
    or CIDRs that match the source IP address.
  - The **`to`** field specifies the operations
    of the request, such as the host
    or method of the request, etc.
  - The **`when`** field specifies a list of
    conditions that need to be met
    after the rule has matched.

* If **one or more ALLOW** authorization policies
  are applied to a workload, access to that workload
  is denied by default and only allowed if
  *one of the ALLOW rules matches it*.
* This is the **deny-by-default** behavior that
  applies only when you have allow policies applied
  to a workload, in other words, if a workload has
  allow policies *one has to match for it to be allowed*.

* *Catch-all authorization policies*
  - Just as the lack of any rule is an indicator that
    no requests are allowed, the opposite, the presence
    of an empty rule means that all requests are allowed.
  - For an example the following will
    *allow all requests by default*:

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-all
  namespace: istio-system
spec:
  rules:
  - {}
```

* To allow requests from `non-authenticated` workloads
  we need to drop the **`from`** field *entirely*

* The difference between these two that
  *`principals`* is the peer from a mTLS connection
  configured by `PeerAuthentication`, and
  *`requestPrincipals`* is for end-user
  `RequestAuthentication` and comes from a JWT token.

* In other words one source defined in *`"from"`* is
  **AND-ed** with one of the operations
  defined in *`"to"`* and **both are `AND-ed`** with
  all the conditions specified in *`"when"`*.
* Meanwhile, it is different in the **`when`** property,
  where all conditions need to match
  because those are **`AND-ed`** together.

* Istio uses a different approach on
  *how policies are evaluated*:
  - The **CUSTOM** policies are evaluated first.
  - The **DENY** policies are evaluated and if
    no *`deny`* policy is matched then
  - The **ALLOW** policies are evaluated and if
    one matches then the request is allowed
  - Otherwise, according to the presence or absence
    of a `catch-all` policy we have two
  - When the `catch-all` policy is *present* it will
    determine the outcome whether
    the request is approved or not.
  - When the `catch-all` policy is *absent*,
    then the request:
  - Will be `allowed` if there are no **ALLOW** policies
  - Will be `rejected` when there are **ALLOW**
    policies but none matches

* *JSON Web Token (JWT)* is a compact claims
  representation that is used to transmit unmodified
  information between two parties as JSON objects.
* The unmodified part comes from the
  verifiable signature of the JWT Token.
* JWT Tokens consist of the following three parts:
  - *Header* - composed of the type and the
    hashing algorithm
  - *Payload* - contains the user claims
  - *Signature* - used to verify the authenticity
    of the JWT Token
* Those three parts, the `header`, `payload`, and `signature`
  are separated by dots (`.`) and stored *base64*
  URL encoded which makes it perfect for usage in HTTP requests.

* Istio workloads can be configured to authenticate
  and authorize end-user requests with JWT tokens.

* The main purpose of the *`RequestAuthentication`*
  resource is to validate JWT tokens and to extract
  and store the claims of valid tokens into
  filter metadata, which are used by authorization
  policies to take actions based on the data.
* An important implicit detail here is that
  *`RequestAuthentication`* resources by themselves
  do not enforce authorizations. You still need
  an *`AuthorizationPolicy`* for that.
* To deny requests *without a JWT token* we need
  to create an *`AuthorizationPolicy`* that
  explicitely denies those,
  *achieved with the definition below:*

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: app-gw-requires-jwt
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: DENY
  rules:
  - from:
    - source:
        notRequestPrincipals: ["*"]
    to:
    - operation:
        hosts: ["webapp.istioinaction.io"]
```

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-all-with-jwt-to-webapp
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        requestPrincipals: ["auth@istioinaction.io/*"]
    to:
    - operation:
        hosts: ["webapp.istioinaction.io"]
        methods: ["GET"]
---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-mesh-all-ops-admin
  namespace: istio-system
spec:
  rules:
  - from:
    - source:
        requestPrincipals: ["auth@istioinaction.io/*"]
    when:
    - key: request.auth.claims[group]
      values: ["admin"]
```

* Configuring Istio for ExtAuthz

```yaml
extensionProviders:
- name: sample-ext-authz-http
  envoyExtAuthzHttp:
    service: ext-authz.istioinaction.svc.cluster.local
    port: "8000"
    includeHeadersInCheck: ["x-ext-authz"]
---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: ext-authz
  namespace: istioinaction
spec:
  selector:
    matchLabels:
      app: webapp
  action: CUSTOM
  provider:
    name: sample-ext-authz-http
  rules:
  - to:
    - operation:
        paths: ["/"]
```

## Troubleshooting the data plane

* The most common mistake: *A misconfigured Data Plane*

* How to verify that the data plane is up to date?
  - Let's check whether the data plane is *synchronized*
    with the latest configuration, using the
    `istioctl proxy-status` command

* Using *`Kiali`* we can perform a quick
  *validation* of the configuration.

* The **Kiali validations** are helpful and should be
  one of the first steps when your workloads are not
  behaving according to your expectation.
  - **Kiali validations** 赞!
* The next step is to use *istioctl* which provides
  another set of validations.

* The *Envoy Administration dashboard* is accessible
  for every service proxy on port `15000`.

* The *`istioctl proxy-config`* command enables us
  to retrieve and filter the proxy configuration
  of a workload based on the *Envoy xDS APIs*,
  where each subcommand is appropriately named:
  - `cluster`: Retrieves cluster configuration
  - `endpoint`: Retrieves endpoint configuration
  - `listener`: Retrieves listener configuration
  - `route`: Retrieves route configuration
  - `secret`: Retrieves secret configuration

* Envoy **Listeners** define a networking
  configuration such as an *IP Address* and *Port*
  that allows downstream traffic into the proxy.
* Envoy **Routes** is a set of rules that match
  the *virtual hosts* to *clusters*. Routes are
  processed in the listed order. The first to match
  is used to route traffic to clusters of workloads.
* Envoy **Clusters** is a set of clusters where each
  cluster has a group of *endpoints* to similar workloads.
  **Subsets** are used to further divide workloads
  within a cluster, which enables
  fine-grained traffic management.
* Envoy **Endpoints** is a set of endpoints which
  represent the *IP Addresses* of the
  workloads that serve the requests.

* Admitting traffic is the responsibility of
  the *Envoy Listeners* which are configured
  in Istio using the *`Gateway`* resource.

```zsh
istioctl proxy-config listeners \
  deploy/istio-ingressgateway -n istio-system
```

* Be assured that port `8080` is the correct port
  as traffic from port `80` to `8080` is forwarded
  by the Kubernetes service named
  `istio-ingressgateway`, which can be seen
  when printing the service definition.

```zsh
kubectl -n istio-system get svc \
  istio-ingressgateway -o yaml
```

* Istio configures *Envoy Routes* using the
  *`VirtualService`* resource, meanwhile, *clusters*
  are either auto-discovered or defined using
  the *`DestinationRule`* resource.

```zsh
istioctl pc routes deploy/istio-ingressgateway \
  -n istio-system \
  --name http.80
```

* Whenever the *Grafana* dashboard doesn't provide
  enough details we can query *Prometheus* directly.

## Performance tuning the control plane

* Understanding the steps of data plane synchronization
  1. An incoming event *triggers* the
     synchronization process
  2. The *DiscoveryServer* is a component of istiod
     that listens for these events. In order to improve
     performance, it delays adding the event to the
     push queue for a defined period in order to batch
     and merge subsequent events for that period of time.
  3. After the delay period expires, the *DiscoveryServer*
     adds the merged events to the push queue which
     maintains a list of pushes pending to be processed
  4. The istiod server *throttles* (i.e. limits) the
     number of push requests that are processed concurrently,
     which ensures that faster progress is made on the pushed
     items and prevents CPU time from getting wasted
     context switching between the tasks
  5. The items that get pushed are converted to
    *envoy configuration* and pushed to the workloads

* Ignoring events:
  - Reducing the scope of discovery using discovery selectors

## Scaling Istio in your organization

* The benefits of a multi-cluster service mesh
  - Improved Isolation
  - Failure boundary
  - Regulatory and compliance
  - Increased availability and performance
  - Enable Multi and Hybrid-cloud

* [Gloo Mesh](https://github.com/solo-io/gloo-mesh)

* We distinguish between two types of clusters
  in multi-cluster service meshes:
  - *Primary Cluster*: the cluster in which
    Istio's control plane is installed
  - *Remote Cluster*: the cluster that is remote
    to the control plane installation

* The **multi-cluster** service mesh deployment
  models Istio supports:
  - the *single* control plane (**Primary-Remote**)
  - the *replicated* control planes (**Primary-Primary**)
  - the *external* control plane

## Extending Istio on the request path

* The following are examples of extension:
  - integrating with rate limiting or
    external authorization services
  - adding, removing, or modifying headers
  - calling out to other services to enrich a request payload
  - implement some custom protocols like
    `HMAC` signing/verification
  - non-standard security token handling

* A request comes in from a *downstream* system
  through the `listeners`, then goes through the
  `routing rules`, and ends up going to a `cluster`
  which sends to an *upstream* service.

* A `listener` in *Envoy* is a way to open a port
  on a networking interface and start listening
  to incoming traffic.
* *Envoy* is ultimately a level three and level four
  (L3/L4) proxy that takes bytes off a network
  connection and processes them in some way.
* A `listener` reads bytes off the networking
  stream and processes them through various
  `filters` or *stages* of functionality.
* Envoy's most basic filters are `network filters`
  which operate on a stream of bytes for either
  *encoding* or *decoding*.
* You can configure more than one filter to
  operate on the stream in sequence called a
  **filter chain** and these chains can be used
  to implement the functionality of the proxy.
* One of the most commonly used network filters
  is the *`HTTP connection manager`*. This filter
  is responsible for abstracting away the details
  of converting a stream of bytes into `HTTP`
  *headers*, *body*, and *trailers* for
  *HTTP based protocols*
  (ie, *HTTP 1.1*, *HTTP2*, *gRPC*, and *HTTP3*).
* The `HTTP connection manager` or sometimes
  referred to as **HCM**, handles HTTP requests
  as well as things like *access logging*,
  *request retry*, *header manipulation*, and
  *request routing* based on *headers*, *path-prefix*,
  and other *request attributes*.

* [HTTP filters](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/http_filters)

* The `HTTP filters` must end in a `terminal filter`
  which sends to request to an *upstream* cluster.
  The `HTTP filter` responsible for this
  is the `router filter`.

* There are ways to extend *Envoy's HTTP capabilities*,
  including writing filters, without compiling changes
  into the Envoy binary itself
  with the following HTTP filters:
  - External processing
  - Lua
  - **WebAssembly**

* **`EnvoyFilter`**

* Resources like `VirtualService`, `DestinationRule`, or
  `AuthorizationPolicy` all end up getting translated to
  *Envoy* configuration and potentially configure specific
  `HTTP filters` in a *filter chain*.
* The `EnvoyFilter` resource is intended for advanced usage
  of Istio and is a "break glass" solution. The underlying
  *Envoy API* may change at any time between releases of
  Istio so be sure to validate any `EnvoyFilter` you deploy.
* **Do not assume any backward compatibility here**.
* Bad configuration with this API can potentially
  **take down the entire Istio data plane**.

* The first thing to know about an `EnvoyFilter` resource
  is that it will apply to **all workloads** in the
  namespace for which it is declared unless
  you specify otherwise.
* If you create a `EnvoyFilter` resource in the
  `istio-system` namespace, it will be applied to
  *all workloads* in the mesh.
* If you want to be more specific about which
  workloads in a namespace to which the custom
  `EnvoyFilter` configuration applies, you can use
  a `workloadSelector`.
* The second thing to know about an `EnvoyFilter`
  resource is that it applies after all other Istio
  resources have been translated and configured.
* For example, if you have `VirtualService` or
  `DestinationRule` resources, those configurations
  will be applied to the data plane first.
* Lastly, you should **take great care** when
  configuring a workload with the `EnvoyFilter`
  resource.

```zsh
istioctl pc listener deploy/webapp.istioinaction \
  --port 15006 --address 0.0.0.0 -o yaml
```

* [envoyproxy/ratelimit](https://github.com/envoyproxy/ratelimit)

* Extending Istio's data plane with **Lua**

```lua
function envoy_on_request(request_handle)
  local headers, test_bucket = request_handle:httpCall(
  "bucket_tester",
  {
    [":method"] = "GET",
    [":path"] = "/",
    [":scheme"] = "http",
    [":authority"] = "bucket-tester.istioinaction.svc.cluster.local",
  }, "", 5000)

  request_handle:headers():add("x-test-cohort", test_bucket)
end
```

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: webapp-lua-extension
  namespace: istioinaction
spec:
  workloadSelector:
    labels:
      app: httpbin
  configPatches:
  - applyTo: HTTP_FILTER
    match:
      context: SIDECAR_INBOUND
      listener:
        portNumber: 80
        filterChain:
          filter:
            name: "envoy.filters.network.http_connection_manager"
            subFilter:
              name: "envoy.filters.http.router"
    patch:
      operation: INSERT_BEFORE
      value:
        name: envoy.lua
        typed_config:
          "@type": "type.googleapis.com/envoy.extensions.filters.http.lua.v3.Lua"
          inlineCode: |
            function envoy_on_request(request_handle)
              -- some code here
            end
            function envoy_on_response(response_handle)
              -- some code here
            end
```

* Extending Istio's data plane with **WebAssembly**

* [solo-io/wasm](https://github.com/solo-io/wasm)
  - WebAssembly (WASM) is the future of
    cloud-native infrastructure extensibility.

* [Istio Ecosystem Wasm Extensions](https://github.com/istio-ecosystem/wasm-extensions)

## Istio Pilot debug endpoints

```zsh
kubectl -n istio-system port-forward \
  `make istiod-pod` 8080
```

## Istio security: SPIFFE

* The client initiates the handshake
  with a `ClientHello`, containing the TLS
  version and the encryption methods
  supported by the client.
* The server responds with `ServerHello` and
  it's `X.509` certificate containing server
  identity data, and the public key
* The client verifies that the server's
  certificate data are not tampered with
  and validates the chain of trust
* On a successful validation the client
  sends the server a secret key which is
  a randomly generated string encrypted
  with the server's public key.
* The server uses it's private key to
  decrypt the secret key and uses it for
  encrypting a "finished" message sent as
  a response back to the client.
* The client sends the server an encrypted
  "finished" message using the secret key,
  and the TLS handshake is completed.

* SPIFFE is a set of open source standards for
  providing identity to workloads in highly
  dynamic and heterogeneous environments.
  To issue and bootstrap identity SPIFFE
  defines the following specifications:
  - The SPIFFE ID that uniquely identifies a
    service within a trust domain
  - The Workload Endpoint bootstraps the
    identity of a workload
  - The Workload API signs and issues the
    certificate containing the SPIFFE ID
  - The SPIFFE Verifiable Identity Document
    (SVID) is represented as the certificate
    issued by the Workload API

* SPIFFE Identity is an `RFC 3986` compliant
  URI composed in the following format
  `spiffe://trust-domain/path`.
  The two variables here are:
  - The trust-domain which represents the issuer
    of identity such as an individual or
    organization and
  - The path that uniquely identifies a workload
    within the trust domain.

* The Workload APIs two main functions are:
  - Issuing certificates to workloads, to do
    so it has the Certificate Authority private
    key for signing certificate signing requests
    made by the workloads and
  - Exposing an API to make its features
    available to Workload Endpoints

* The Workload Endpoint represents the data plane
  component of the SPIFFE specification.
  It is deployed alongside every workload and
  provides the following functionalities:
  - Workload Attestation is the process by which
    the workload endpoint verifies the identity
    of a workload. Using methods such as Kernel
    introspection or orchestrator interrogation
  - Workload API Exposure is the process by which
    the Workload Endpoint initiates and maintains
    a secure communication to the Workload API.
    This secure communication is used to
    fetch and rotate SVIDs

* We can see an overview of the steps needed to
  issue identity to workloads:
  - The Workload Endpoint verifies the identity
    of the workload (Workload Attestation)
    and forms the SPIFFE ID
  - The Workload Endpoint submits the SPIFFE ID
    (encoded in a Certificate Signing Request)
    to the Workload API
  - The Workload Endpoint receives the signed
    certificate which represents the SPIFFE
    Verifiable Identity Document and makes it
    available to the workload

* Mapping the SPIFFE components to Istio's implementation
  - The Workload Endpoint is implemented by the
    Pilot-Agent that performs identity bootstrapping
  - The Workload API is implemented by Istio CA
    that issues certificates
  - The Workload for whom the identity is issued in
    Istio is the service proxy

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

> - [Build: Tekton Pipelines](https://github.com/tektoncd/pipeline)

------------------

## Events

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
