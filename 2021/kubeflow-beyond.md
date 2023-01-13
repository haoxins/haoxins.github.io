---
title: Beyond Kubeflow, Cloud Native MLOps
description: 白发渔樵江渚上, 惯看秋月春风. 一壶浊酒喜相逢. 古今多少事, 都付笑谈中.
date: 2021-09-13
---

## Argoflow

* [argoflow/argoflow-gcp](https://github.com/argoflow/argoflow-gcp)

## Auth

* *OpenID Connect* (**OIDC**)
* **OIDC** is a common way of delegating the
  responsibility of managing user credentials
  to another service and a powerful feature of
  *Istio* is that it can be leveraged to manage
  this flow without your backend service needing
  to be aware of *OIDC* is even being used.
* **Scopes** are space-separated lists of
  identifiers used to specify what access
  privileges are being requested.
  Valid scope identifiers are specified in **RFC 6749**.
* **OIDC** has a number of built in scope identifiers.
  `openid` is a *required* scope. All others
  (including custom scopes) are *optional*.
* The *built-in* scopes are:
  - `profile`: requests access to default profile claims
  - `email`: requests access to email
    and `email_verified` claims
  - `address`: requests access to address claim
  - `phone`: requests access to `phone_number` and
    `phone_number_verified` claims
* **claims** are `name/value` pairs that contain
  information about a user, as well `meta-information`
  about the `OIDC` service. The official definition
  from the spec is a
  - `"piece of information asserted about an Entity."`
* There are *three primary flows*: `Authorization Code`,
  `Implicit`, and `Hybrid`. These flows are controlled
  by the `response_type` query parameter in the
  `/authorization` request.
* `Authorization Code` flow uses `response_type=code`.
  After successful authentication, the response will
  contain a `code` value. This `code` can later be
  exchanged for an `access_token` and an `id_token`.
* There are *three types* of tokens in OIDC:
  `id_token`, `access_token` and `refresh_token`.

* OIDC auth from **external**
  - [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/openid-connect)
* OIDC auth on **cluster**
  - [Dex](https://github.com/dexidp/dex)
  - [Keycloak](https://github.com/keycloak/keycloak)
* [OIDC AuthService](https://github.com/arrikto/oidc-authservice)
  - OIDC AuthService stores *sessions* and other state
    in a local file using *BoltDB*.
  - *BoltDB* has been *archived*!
  - Kubeflow *built-in* solution, should be *deprecated*!
* [OAuth2 Proxy](https://github.com/oauth2-proxy/oauth2-proxy)
  - Going with the *WASM* extensibility in *Istio*,
    managing the *OIDC* flow may be a good candidate
    as a *WASM* extension in the future.
* Starting with *Envoy* `1.16` (*Istio* `>= 1.8`)
  there is a new filter called **OAuth2**.
  - It does a token request (exactly how *oauth2-proxy* does),
    but makes it internally
    (directly from the *Envoy* component),
    so no additional tooling is needed.

## Storage Backend

* katib-mysql
* kube-prometheus-stack-grafana
* minio-pvc
* mysql-pv-claim
* kube-prometheus-stack-prometheus-0
* storage-loki-stack-0

------------------

## Events

### 2021

* **Jaeger**: 2021-11
  - 把自己维护的 K8s clusters 上的 **Jaeger** *storage backend* 从
    **Cassandra** 切换到了 **Elasticsearch**
  - The Jaeger team recommends Elasticsearch
    as the storage backend over Cassandra

* [How We Used PyTorch Lightning to Make Our Deep Learning Pipeline 10x Faster](https://devblog.pytorchlightning.ai/how-we-used-pytorch-lightning-to-make-our-deep-learning-pipeline-10x-faster-731bd7ad318a)
  - Parallel data loading
  - Multi-GPU training
  - Mixed precision training
  - Sharded training
  - Early stopping
  - Optimizations during model evaluation & inference
