---
title: MLOps
description: 昨夜闲潭梦落花, 可怜春半不还家. 江水流春去欲尽, 江潭落月复西斜.
date: 2021-07-21
---

### pip

* `~/.config/pip/pip.conf`

### Jupyter

```py
# %env GOOGLE_APPLICATION_CREDENTIALS="/home/jovyan/abc.json"
# Not works, the error is:
# File "/home/jovyan/abc.json" not found
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/jovyan/abc.json"
# This works
```

------------------

# Events

------------------

* [KServe: The next generation of KFServing](https://blog.kubeflow.org/release/official/2021/09/27/kfserving-transition.html)
  - *KFServing* is now *KServe*
  - The project has been rebranded from
    *KFServing* to *KServe*, and we are planning
    to *graduate* the project from
    *Kubeflow Project* later this year.

* [How We Used PyTorch Lightning to Make Our Deep Learning Pipeline 10x Faster](https://devblog.pytorchlightning.ai/how-we-used-pytorch-lightning-to-make-our-deep-learning-pipeline-10x-faster-731bd7ad318a)
  - Parallel data loading
  - Multi-GPU training
  - Mixed precision training
  - Sharded training
  - Early stopping
  - Optimizations during model evaluation & inference

* 2021~2022 才是 ML 真正飞入寻常百姓家 的时候
  - K8s Operator ready!
  - 学术界的输出趋于稳定, 工程界开始代码工程化
