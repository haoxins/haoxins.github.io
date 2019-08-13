---
title: Cloud notes
description: Cloud is future ~
date: 2019-06-28
---

### Cloud native

* `Region`, `Time Zone`, `ENV vars`

### Functions

* How to edit code, version control, deploy?
* How to set & maintain ENV vars?
* How to centralize logs, metrics?


* AWS - Snowflake

### Google cloud data

* Dataprep:
  - by Trifacta

* Dataflow:
  - Apache Beam based jobs
  - Serverless
  - Automatic provisioning of clusters

* Dataproc:
  - Hadoop cluster
  - Manual provisioning of clusters

### GCP BigQuery

* 尽量使 `Scheduled queries` 越简单越好, 把复杂逻辑保存为 `Views`
  - 当 `DEBUG` 或 `change` 逻辑时, 变更 `Views` 不需要变更 `Scheduled queries`
  - `风险`: 被别人 误改 (泪)

### Data studio
  - https://developers.google.com/datastudio/visualization/

### GCP tools

https://cloud.google.com/apigee/
https://cloud.google.com/endpoints/
https://cloud.google.com/stackdriver/
