---
title: Beyond Kubeflow, Cloud Native MLOps
description: 白发渔樵江渚上, 惯看秋月春风. 一壶浊酒喜相逢. 古今多少事, 都付笑谈中.
date: 2021-09-13
---

## Argoflow

* [argoflow/argoflow-gcp](https://github.com/argoflow/argoflow-gcp)

## Auth

* *OpenID Connect* (**OIDC**)
* **`OIDC`** is a common way of delegating the
  responsibility of managing user credentials
  to another service and a powerful feature of
  *Istio* is that it can be leveraged to manage
  this flow without your backend service needing
  to be aware of `OIDC` is even being used.
* **`Scopes`** are space-separated lists of
  identifiers used to specify what access
  privileges are being requested.
  Valid scope identifiers are specified in `RFC 6749`.
* **`OIDC`** has a number of built in scope identifiers.
  `openid` is a *required* scope. All others –
  including custom scopes – are *optional*.
* The *built-in* scopes are:
  - `profile`: requests access to default profile claims
  - `email`: requests access to email
    and `email_verified` claims
  - `address`: requests access to address claim
  - `phone`: requests access to `phone_number` and
    `phone_number_verified` claims
* **`claims`** are `name/value` pairs that contain
  information about a user, as well `meta-information`
  about the `OIDC` service. The official definition
  from the spec is a
  "piece of information asserted about an Entity."
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
## Storage Backend

* katib-mysql
* kube-prometheus-stack-grafana
* minio-pvc
* mysql-pv-claim
* kube-prometheus-stack-prometheus-0
* storage-loki-stack-0
