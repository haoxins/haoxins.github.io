---
title: (2021) 初识 Kubeflow, Components~
description: 行到水穷处, 坐看云起时. 偶然值林叟, 谈笑无还期.
date: 2021-07-23
---

## Kubeflow Pipelines

* UI 简陋, 远不如 [Airflow](https://github.com/apache/airflow)
* A pipeline component is a self-contained set of user code,
  packaged as a Docker image,
  that performs one step in the pipeline.
  - 虽然 Airflow 也有 Docker Operator
  - 但是 KFP 明显更加范式统一
* Kubeflow Pipelines SDK v2
