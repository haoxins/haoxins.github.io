---
title: Cloud notes
description: Cloud is future ~
date: 2019-06-28
---

### Cloud native

* `Region`, `Time Zone`

### Functions

* Everything in Git
  - codes
  - shell, gcloud deploy ...
  - ENV vars, `.env.yml`
* Use StackDriver to view logs, ...

* AWS - Snowflake

### Google cloud data

* DataFlow:
  - MapReduce (Batch), Side inputs, Streaming
  - Automatic provisioning of clusters
  - With Pub/Sub, BigTable, Cloud functions, BigQuery

* Machine Learning

BigQuery, TensorFlow, Cloud ML Engine

* Dataprep (by Trifacta, base on DataFlow)

### GCP BigQuery

* 尽量使 `Scheduled queries` 越简单越好, 把复杂逻辑保存为 `Views`
  - 当 `DEBUG` 或 `change` 逻辑时, 变更 `Views` 不需要变更 `Scheduled queries`
  - `风险`: 被别人 误改 (泪)

### Data studio
  - https://developers.google.com/datastudio/visualization/

### GCP tools

GCP Role -> Team

https://cloud.google.com/apigee/
https://cloud.google.com/endpoints/

## Deprecated

* DataProc:
  - Manual provisioning of clusters
  - Hadoop, Hive, Spark, BigQuery, Cloud Storage
  - Directed Acyclic Graph (DAG)
  - Cloud Composer (Apache Airflow)
  - create a cluster specifically for one job
  - use Cloud Storage instead of HDFS
  - on non-critical jobs requiring huge clusters, use preemptible VMs

* DataStore is a `toy`
