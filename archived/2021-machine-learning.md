---
title: (2021) Machine learning
description: 逝者如斯, 而未尝往也; 盈虚者如彼, 而卒莫消长也.
date: 2021-03-21
---

## Machine Learning Data Lifecycle in Production

------------------

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


------------------

# Timeline

------------------

## 2021

### Kubeflow

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
