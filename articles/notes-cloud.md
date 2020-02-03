---
title: Cloud notes
description: Cloud is future ~
date: 2019-06-28
---

* `Region`, `Time Zone`
## 2020

### Functions

* Everything in Git
  - codes
  - shell, gcloud deploy ...
  - ENV vars, `.env.yml`
* Use StackDriver to view logs, ...

### Pub/Sub (Bus)

* A message persist for 7 days (max)
* At least once delivery guarantee
  - no order, maybe duplicated, stateless

### DataFlow

* MapReduce
  - ParDo (Map, FlatMap, Filter -> `<key, val>`)
  - Combine (perKey, globally) (Count, Sum, ...) `<key, val>`
  - GroupByKey (-> `<key, [val1, val2, val3, ...]>`)
  - Combine is more efficient than GroupByKey
  - Side inputs (ParDo.withSideInputs)
  - Window (Streaming)

* Automatic provisioning of clusters
* BigTable, Cloud functions, BigQuery
* Machine Learning

BigQuery, TensorFlow, Cloud ML Engine

* Dataprep (by Trifacta, base on DataFlow)

### GCP BigQuery

* 尽量使 `Scheduled queries` 越简单越好, 把复杂逻辑保存为 `Views`
  - 当 `DEBUG` 或 `change` 逻辑时, 变更 `Views` 不需要变更 `Scheduled queries`
  - `风险`: 被别人 误改 (泪)

### GCP tools

GCP Role -> Team

https://cloud.google.com/apigee/
https://cloud.google.com/endpoints/
