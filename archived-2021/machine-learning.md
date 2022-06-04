---
title: Machine learning
description: 逝者如斯, 而未尝往也; 盈虚者如彼, 而卒莫消长也.
date: 2021-03-21
---

## Deploying Machine Learning Models in Production

* After deploying to the production environment,
  the ML model remains constant until it's
  retrained because the model will see a lot of
  real life data and then it becomes
  stale quite quickly. This phenomenon is called
  **model decay**, and it's something that
  *should be carefully monitored*.

* Depending on the use case, you need to decide
  on two metrics. There's the **model's optimizing metric**
  which reflects the model's predictive effectiveness
  and this includes things like *accuracy*, *precision*,
  *recall*, and so on. Good values in these metrics is
  a strong signal about the *quality of your model*.
* And then there's the models **gating metric** and
  this reflects an operational constraint that
  the model has to satisfy, such as *prediction latency*.

* Google Cloud Firestore
  - https://cloud.google.com/firestore
  - Serverless

* Your *model* is typically saved to the *file system*.
* The *model server* receives these data formats
  it into the required shape, passes it to the
  model file and gets the inference back.
  - TensorFlow serving
  - Torch Serve
  - Kubeflow Serving

* **TorchServe** is an initiative by
  *AWS and Facebook* to build a model serving
  framework for PyTorch models.
  - With *TorchServe*, you can deploy *PyTorch*
    models in either *eager* or *graph* mode.

* Unlike a pure software system, there are
  two additional components to consider in
  an ML system, the *data* and the *model*.
  Unlike in traditional software systems,
  the accuracy of an ML system depends on
  how well the model reflects the world
  it is meant to model which in turn
  depends on the data used for training
  and on the data that it receives
  while serving requests.

* So there are two main causes of model drift.
  **Data drift** and **concept drift**.
  - *Data drift* occurs when statistical
    properties of the input, the features, changes.
    As the input changes, the prediction requests,
    the input moves farther away from the data
    that the model was trained with,
    and model accuracy suffers.
  - *Concept drift* occurs when the relationship
    between the features and the labels changes.

* If you can automate the process of detecting
  the conditions which require model retraining,
  that's ideal. That includes being able to
  detect model performance degradation and
  triggering retraining, or when you detect
  significant data drift.

* You should consider privacy enhancing technologies
  such as *Secure Multi-Party Computation*, or **SMPC**,
  or *Fully Homomorphic Encryption*, or **FHE**,
  when training and serving your models.

* *Differentially-Private Stochastic Gradient Descent*,
  or **DP-SGD**,
* *Private Aggregation of Teacher Ensembles*
  or **PATE**,
* and *Confidential and Private Collaborative learning*,
  or **CaPC**.

* In many ways, machine learning can be
  considered an experimental science since
  experimenting and analyzing results is
  at the heart of ML development.

* Even small changes like changing the width
  of a layer or the learning rate can make a
  big difference in both the model's performance
  and the resources required to train the model.

* In these cases, you probably want to keep
  experiments separate if you're using a shared
  monorepo with your team so that your commits
  don't version the rest of the team's repo.

* So if you're going to be able to track,
  understand, compare and duplicate your
  experimental results you need to
  *version your data*.

* Changes in the data as the world
  around them changes, are not typically a
  primary concern when simply
  doing software development.

* Like DevOps, MLOps is an ML engineering
  *culture and practice* that aims at unifying
  *ML system development or dev*
  and *ML system operation or ops*. Unlike DevOps,
  ML systems present unique challenges to core
  DeVOps principles like continuous integration
  which for ML means that you not only just
  test and validate code and components but also
  do the same for data schemas and models.

* A *level 0 process* is concerned only with
  deploying the trained model as a prediction service.
* One of the *key goals* of **level one** is to
  perform *continuous training of the model*,
  by *automating the training pipeline*.
* The truth is that the current stage are at
  the current stage of the development of
  MLOps best practices, **level two** is still
  somewhat *speculative*.

* To construct *ML pipelines components* need to be
  *reusable*, *composable*, and potentially
  *shareable* across pipelines.
  - In addition, components should
    ideally be *containerized*.

* A **feature store** is a centralized repository
  where you standardize the *definition*, *storage*,
  and access of features for training and serving.
  Ideally, a feature store will provide an API
  for both high throughput *batch serving* and
  low latency, *real-time serving* for the feature values,
  and support both training and serving workloads.

* Another key component is the **metadata store**,
  where information about each execution of the
  pipeline is recorded in order to help with
  data and artifact lineage,
  reproducibility, and comparisons.
  It also helps you debug errors and anomalies.

* The **major version** will increment when
  you have an incompatible data change,
  such as a schema change or target variable
  change that can render the modeling compatible
  with it's prior versions when it's
  used for predictions.
* The **minor version** will increment when
  you believe that you've improved or
  enhanced the model's output.
* Finally, the pipeline version will correspond
  to an update in the training pipeline,
  but it need not improve or
  even change the model itself.

* **Model lineage** is a set of relationships
  among the artifacts that resulted in the
  trained model. To build model artifacts,
  you have to be able to track the code
  that builds them and the data,
  including pre-processing operations that
  the model was trained and tested with.

* A **model registry** is a central repository
  for storing trained models. Model registries
  provide an API for managing train models
  throughout the model development lifecycle.

* **Progressive Delivery**

## Machine Learning Modeling Pipelines in Production

### Neural Architecture Search

* Neural Architecture Search (NAS)
  - search space
  - search strategy
  - performance estimation strategy

### Dimensionality Reduction

```
But as you add more features,
you reach a certain point where your model's performance degrades.

The challenge is to keep as much of the predictive information
as possible using as few features as possible.
```

* Tuner -> Trainer

```
A poor model fed with important features will
perform better than a fantastic model fed
with low quality or bad features.
```

* Principal component analysis, or **PCA**
* Linear discriminant analysis, or **LDA**
* Partial least squares, or **PLS**

* Principal Components Analysis
  - Starting with decorrelation

```
You can reduce dimensionality by limiting the number of
principal components to keep based on the
cumulative explained variance.

In addition, PCA offers several variations and extensions.
For example, kernel PCA or sparse PCA, etc.

Other than this, PCA is especially useful when visually
studying clusters of observations in high dimensions.
```

* Unsupervised approaches
  - single value decomposition, or SVD
  - independent component analysis, or ICA
* Matrix factorization techniques
  - non-negative matrix factorization
* Latent dimensionality reduction methods
  - latent dirichlet allocation, or LDA

* SVD

```
SVD decomposes our original dataset into its constituents,
resulting in a reduction of dimensionality.
```

* PCA vs ICA

```
PCAs and ICAs's significant difference is that
PCA looks for uncorrelated factors, while
ICA looks for independent factors.

If two factors are uncorrelated,
it means that there is no linear relation between them.
If they're independent, it means that they are not
dependent on other variables.

ICA is an algorithm that finds directions in the
feature space corresponding to projections
which are highly non-Gaussian.

Unlike PCA, these directions need not be orthogonal
in the original feature space,
but they are orthogonal in the whitened feature space,
in which all directions correspond to the same variance.

PCA, on the other hand, finds orthogonal directions
in the raw feature space that corresponded
directions accounting for maximum variance.

When it comes to the importance of components,
PCA, considers some of them to be more important than others.
ICA, on the other hand,
considers all components to be equally important.
```

* NMF and PCA

```
NMF, like PCA, is a dimensionality reduction technique,
in contrast to PCA, however,
NMF models are interpretable.
NMF can produce a parts-based representation of the dataset,
resulting in interpretable models.
```

### Quantization and Pruning

* Quantization

```
Quantization involves transforming a model into
an equivalent representation that uses
parameters and computations at a lower precision.

Quantization, in essence, lessens or reduces
the number of bits needed to represent information.

You can do quantization during training or
after the model has been trained.

The simplest approach to quantize a neural network
is to first train it in full precision and then
simply quantize the weights to fixed point.

This is post-training quantization.
By contrast, quantization aware training
applies quantization to the model while it is being trained.
The core idea is that quantization aware training simulates
low precision inference time computation in the forward pass
of the training process.

By inserting fake quantization nodes,
the rounding effects of quantization
are assimilated in the forward pass,
as it would normally occur in actual inference.
The goal is to fine-tune the weights
to adjust for the precision loss.
```

* Pruning

```
Pruning aims to reduce the number of parameters
and operations involved in generating a prediction
by removing network connections.

A sparse network is not only smaller,
but it is also faster to train and use.
Also, more complex models are more
prone to overfitting.
```

### High-Performance Modeling

* Distributed Training
  - data parallelism and model parallelism

```
In model parallelism, however,
you segment the model into different parts,
training concurrently on different workers.
Each model will train on the same piece of data.
```

```
There are two basic styles of distributed training
using data parallelism.

In synchronous training, each worker trains on its
current mini batch of data, applies its own updates,
communicates out its updates to the other workers.
And waits to receive and apply all of the updates
from the other workers before proceeding to the next mini batch.
And all-reduce algorithm is an example of this.

In asynchronous training, all workers are independently
training over their mini batch of data and
updating variables asynchronously.

Asynchronous training tends to be more efficient,
but can be more difficult to implement.
Parameter server algorithm is an example of this.
One major disadvantage of asynchronous training
is reduced accuracy and slower convergence,
which means that more steps are required to converge.
Slow convergence may not be a problem,
since the speed up in asynchronous training
may be enough to compensate.
However, the accuracy loss may be an issue
depending on how much accuracy is lost and
the requirements of the application.
```

* **High-Performance Ingestion**

```
One strategy that can overcome problems with
insufficient GPU memory is gradient accumulation.
Gradient accumulation is a mechanism to split
full batches into several mini-batches.

The second approach is swapping.
The problem here is that it's slow.
```

* **pipeline parallelism**

```
Pipeline parallelism frameworks integrate both
data and model parallelism to achieve high
efficiency and preserve model accuracy.

They do that by dividing mini-batches
into smaller micro-batches,
by allowing different workers to work on
different micro-batches in parallel.
```

### Knowledge Distillation

```
Knowledge distillation seeks to create
a more efficient model which captures
the same knowledge as a more complex model.

It starts, by first training a complex model or
model ensemble to achieve a high level of accuracy.
It then uses that model as a teacher
for a simpler student model.
Which will then be the actual model
that gets deployed to production.

This teacher network can be either fixed or jointly optimized.
Can even be used to train multiple student models
of different sizes simultaneously.
```

```
The teacher will be trained first using a
standard objective function that seeks to
maximize the accuracy or a similar metric of the model.
This is normal model training.

The student then seeks transferable knowledge.
It uses that objective function that seeks to
match the probability distribution of the
predictions of the teacher.

Notice that the student is not just learning
the teacher's predictions,
but the probabilities of the predictions.
```

```
These results show that knowledge distillation
isn't just limited to smaller models,
like to still bert.
But can also be used to increase the robustness
of an already great model using noisy student training.
```

### Model Analysis

* Model Performance Analysis

```
At a high level, there are two main ways to
analyze the performance of your model.
Black-box evaluation and model introspection.
```

* **TFMA**
  - TFMA uses Apache Beam to do a full pass over the evil dataset.

```
The metrics themselves will be the same types that
you use for training depending on the model type.
So things like RMSC for regression models
and AUC for classification.
```

* Sensitivity Analysis and Adversarial Attacks
* Residual Analysis
* Model Remediation
* Continuous Evaluation and Monitoring

```
Concept drift can happen even when
the rest of your data doesn't change.

An emerging concept refers to new patterns
in the data distribution that weren't
previously present in your dataset.

In covariate shift, the distribution of your
input data changes, but the conditional probability
of your output over the input remains the same.
The distribution of your labels doesn't change.

Prior probability shift is basically the
opposite of covariate shift.
The distribution of your labels changes,
but your input data stays the same.

Concept drift can be thought of as
a type of prior probability shift.
```

### Interpretability

* [SHAP (SHapley Additive exPlanations)](https://github.com/slundberg/shap)
  - A game theoretic approach to explain
  - the output of any machine learning model.

* Shapley Values

```
Some feel that Shapley value might be the
only legally compliant method because
it's based on a solid theory and
distributes the effects fairly.
The Shapley value also allows contrastive explanations.

Like any method Shapley has some disadvantages.
Probably the most important is that
its computationally expensive,
which in a large percentage of real world cases
means that it's only feasible to
calculate at approximate solution.
```

* Intrinsically Interpretable Models

```
One key characteristic which helps improve
interpretability is when features are monotonic.
Monotonic means that the contribution of
the feature towards them all result,
either consistently increases or decreases or
stays even as the feature value changes.
```

* Partial Dependence Plots, or **PDP**
* Permutation Feature Importance
* Testing Concept Activation Vectors

------------------

## Machine Learning Data Lifecycle in Production

* ML: **data is a first class citizen**

* Data issues
  - Data drift
  - Concept drift
  - Schema skew
  - Distribution skew
  - Data shift
  - Covariate shift
  - Concept shift
  - [TFDV](https://github.com/tensorflow/data-validation)

* Feature Engineering
  - training vs serving
  - batch vs streaming

* Preprocessing Operations
  - Mapping raw data into features
  - Data cleansing
  - Feature tuning
  - Transformations
  - Feature construction

* Feature Engineering Techniques
  - Feature scaling
  - Normalization (Xnorm = (X - Xmin) / (Xmax - Xmin) ...)
  - Standardization (Z-Score ...)
  - Bucketizing, Binning
  - PCA, t-SNE, UMAP

* Feature crosses

* Encoding features

* Feature spaces
  - decision boundary
  - so feature space coverage is important

* Feature selection
  - Filter methods
  - (correlation matrix)
  - Wrapper methods
  - (forward selection, start with one feature)
  - (backward elimination, start with all features)
  - (recursive feature elimination, RFE)
  - Embedded methods
  - (L1 or L2 regularization)
  - (Feature importance)

* ML Metadata
  - https://github.com/google/ml-metadata

* [Data Version Control, DVC](https://github.com/iterative/dvc)
  - Data Version Control or DVC is an open-source tool for
  - data science and machine learning projects.

* Feature stores

* [Feast](https://github.com/feast-dev/feast)
  - Feast is an open source feature store for machine learning.

* Data warehouse & Data lakes

* Time series
  - windowing
  - sensors and signals
  - spectrogram

------------------

* [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)

* [Responsible Machine Learning with Error Analysis](https://techcommunity.microsoft.com/t5/azure-ai/responsible-machine-learning-with-error-analysis/ba-p/2141774)

* [Machine Learning in Production: Why You Should Care About Data and Concept Drift](https://towardsdatascience.com/machine-learning-in-production-why-you-should-care-about-data-and-concept-drift-d96d0bc907fb)

* [Challenges in Deploying Machine Learning: a Survey of Case Studies](https://arxiv.org/abs/2011.09926)

* [Towards ML Engineering: A Brief History Of TensorFlow Extended (TFX)](https://arxiv.org/abs/2010.02013)

* [Deep Double Descent: Where Bigger Models and More Data Hurt](https://arxiv.org/abs/1912.02292)

------------------

## Machine Learning in Production

* Data definition
  - high quality data
* Modeling
  - data, code
* Think of deployments as an iterative process

* Key challenges
  - Concept drift and, data drift
  - Software engineering issues
  - (cloud or edge, batch or realtime, TPU or GPU, latency, logging, QPS, ...)
  - Security and privacy

* Deployment patterns
  - Versioning and rollback
  - Shadow mode (Human and ML)
  - Canary deployment
  - Blue green deployment

* Monitoring
  - Software metrics
  - Input metrics
  - Output metrics
  - Only by monitoring the system that you can spot if there may be a problem

### Data definition

* consistently label the data with one convention

* Major types of data problems

```
          Unstructured     Structured
                        |
Small data              |                clean labels are critical
                        |
          ------------------------------
                        |
Big data                |                emphasis on data processes
                        |
```

* Improving label consistency
  - try to reach an agreement
  - create a new label to capture uncertainty

* Human level performance (HLP)

```
Measuring Human Level Performance is useful for
establishing a baseline using that to drive
error analysis and prioritization.

But using it to benchmark machines and humans sometimes
runs into problematic cases like this.
I found that when my goal is to build a useful application,
not publish a paper, you publish a paper,
let's prove we can outperform people that helps published paper.

But found that when my goal is to build a useful application
rather than trying to beat Human Level Performance,
I found it's often useful to instead try to
raise Human Level Performance because we raise
Human Level Performance by improving label consistency
and that ultimately results in better
learning outcomes performance as well.
```

```
How much bigger should you make your data set?
One tip I've given a lot of teams is
don't increase your data by more than 10x at a time.

I found this really hard to predict what will happen
when your data set size increases even beyond that.
```

* Meta-data, data provenance and lineage

* Balanced train/dev/test splits (Small data set)
  - makes your data set more representative of the true data distribution

### Modeling

* ML = Code (Model) + Data

* Key challenges
  - Establish a baseline
  - Baseline helps to indicate what might be possible.

* Tips
  - Start with a quick literature search to see what's possible
  - **Don't obsess about finding the latest, greatest algorithm**

```
A reasonable algorithm with good data will often do just fine
and will in fact outperform a great algorithm with not so good data
```

* **Error analysis**
  - error analysis is also an iterative process
  - skewed datastes, confusion matrix (precision and recall)

```
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1 Score = 2 / ((1 / Precision) + (1 / Recall))
```

### Data iteration

> Data-centric AI development

* Good data
  - covers the important cases
  - defined consistently
  - has timely feedback from production data
  - reasonable size

> Can adding data hurt? Yes!

* Data augmentation
  - GANs

* Versioning everything
  - Code
  - Datasets
  - Hyperparameters

------------------

# Timeline

------------------

## 2021

### GraphScope

> A One-Stop Large-Scale Graph Computing System from Alibaba

* [Release v0.6.0](https://github.com/alibaba/GraphScope/releases/tag/v0.6.0)
  - [Release Notes: v0.6.0](https://graphscope.io/blog/releasenotes/2021/08/08/release-notes-0.6.0.html)

```
This major release integrates a new graph interactive engine GAIA,
which supports efficient parallel execution and
bounded-memory execution for Gremlin queries.
```

### Kubeflow

* [Blog: Running Kubeflow at Intuit: Enmeshed in the service mesh](https://blog.kubeflow.org/running-kubeflow-at-intuit/)

```
Kubeflow 1.3, Istio, ArgoCD

Kubfelow uses Argo workflows internally to run the pipeline
in a workflow fashion.
```

* [The Kubeflow 1.3 software release streamlines ML workflows and simplifies ML platform operations](https://blog.kubeflow.org/kubeflow-1.3-release/)

```
The Kubeflow 1.3 release delivers simplified ML workflows
and additional Kubernetes integrated features to
optimize operational and infrastructure efficiencies.

In addition to new User Interfaces (UIs),
which improve ML workflows for pipeline building,
model tuning, serving and monitoring,
1.3 also enables "headless" GitOps-inspired installation patterns.
The latest version of Kubeflow provides users with a mature foundation
and delivers a modern ML platform with best-in-class
Key Performance Indicators (KPIs).
```

### Others

* [A Chat with Andrew on MLOps: From Model-centric to Data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo)
  - data quality systematic
  - code fixed, iteratively improve the data
  - MLOps

* [What are the most important statistical ideas of the past 50 years?](https://arxiv.org/pdf/2012.00174.pdf)

### 特征工程

* Data split
  - Train set, Test set
  - Train set, Dev set, Test set
  - Dev set (验证集) -> 验证 超参
  - Bias, Variance

* 归一化
  - 线性归一化
  - 零均值归一化 (均值为 0, 标准差为 1)

* 类别型数据
  - 序号编码
  - 独热编码
  - 二进制编码

* 文本数据
  - Word2Vec

* 组合特征
  - 提高复杂关系的拟合能力
  - 基于决策树寻找特征组合

### 模型评估

* 精确率 vs 召回率
  - P-R 曲线
  - ROC 曲线
  - F1 Score

* ROC 曲线 & AUC
* 余弦距离 vs 欧氏距离

### 经典算法

* SVM
* 逻辑回归
* 决策树
  - 特征选择
  - 树的构造
  - 树的剪枝

### 降维

* 数据集维度越高, 越稀疏, 越容易过拟合
* 投影 & 流形

* PCA 主成分分析
  - 最大化投影方差
  - 最小平方误差
* LLE 局部线性嵌入 (流形)
* LDA 线性判别分析
  - 最大化类间距离
  - 最小化类内距离

### 优化

* 凸优化
* 随机梯度下降法
  - Adam
* L1正则化
* L2正则化

* 正则化
  - 通过 **约束模型** 使其更简单, 降低 **过拟合** 风险
  - Dropout

* 模型集成 Dropout
* 批量归一化

### 采样

* 均匀分布随机数
  - 线性同余法

* 逆变换采样
* 拒绝采样
* 重要性采样
* 马尔可夫蒙特卡洛采样法

### 无监督学习

* 聚类
* 特征关联

* K-means
* GMM 高斯混合模型
* SOM 自组织映射

```
有监督 与 无监督 的结合

DBN (深度信念网络) 基于 无监督组件 RBM (受限玻尔兹曼机)
受限玻尔兹曼机 以无监督方式训练
然后有监督微调
```

### 集成学习

* Boosting
  - 降低偏差
* Bagging
  - (随机森林)
  - 降低方差

* 偏差 Bias
* 方差 Variance

* 最常用的基分类器 **决策树**

* GBDT 梯度提升决策树
  - 一般使用 CART 决策树

### 前向神经网络

* 神经网络训练过程的本质是学习数据分布

* 激活函数
  - 每一层线性变换后
  - 叠加一个非线性激活函数
  - 避免多层网络等效于单层线性函数

* 反向传播算法

* 深度残差网络 ResNet
  - 缓解深层神经网络的梯度消失问题

### 卷积神经网络

* 局部连接
* 权值(卷积核)共享
* 输入 -> 输出的结构保留

* 可变形卷积

* AlexNet
* VGGNet
* ResNet

* 批归一化 BN
* 全局平均池化

### 循环神经网络

* 对比传统: 隐马尔可夫模型 HMM, 条件随机场 CRF
* 对比卷积: 时间卷积网络, 因果卷积

* 难以 并行计算
* 容易 梯度消失或梯度爆炸

* LSTM 长短期记忆网络
  - 循环神经网络 最知名 & 最成功 的扩展
* GRU
* Seq2Seq

### 概率图模型

* 贝叶斯网络 有向图结构
* 马尔可夫网络 无向图网络结构

* 马尔可夫模型
* 隐马尔可夫模型

### 强化学习

* 状态转移概率已知 -> 马尔可夫决策过程
* 状态转移概率未知 -> 蒙特卡罗, 时序差分

* 基于策略迭代 vs 基于价值迭代
  - 基于价值迭代: Q-Learning, Sarsa
  - 基于策略迭代: 策略梯度

* 时序差分 -> Q-Learning
  - 只适用于处理离散状态空间
  - 不保证收敛性

* 策略梯度
  - 可以处理 离散 & 连续 状态空间
  - 保证至少收敛到一个局部最优解

* Q-Learning -> DQN

### 生成模型 & GANs

* 传统概率生成模型 vs GANs

* 可微生成网络
  - AE 自编码器
  - VAE 变分自编码器, 变分推断
  - GAN 生成式对抗网络

* GAN 的基础上引入 VAE -> ALI 对抗学习推断

### 元学习

* 适合: 小样本, 多任务, 快速学习, 快速适应
  - 需要多个不同但相关的任务支持

* LFT (Learning from Experiences): 从经验学习 (有监督学习, 强化学习)
* LTL (Learning to Learn): 学会学习
  - 训练集不同
  - 预测函数不同
  - 损失函数不同
  - 评价指标不同
  - 学习内涵不同
  - 泛化目标不同
