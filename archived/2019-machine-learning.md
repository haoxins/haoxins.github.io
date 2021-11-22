---
title: Machine learning
description: 念去去, 千里烟波, 暮霭沉沉楚天阔
date: 2019-06-30
---

### TensorFlow

* TFX (TensorFlow Extended)
* TF Record
  - protobuf
* Functional APIs
* Lambda Layers
* Layer: State + Computation
* Subclassing Models
* Built-in Callbacks
* Custom Callbacks
* Gradient Tape
* Eager Mode & Graph Mode
* Auto Graph
* Distributed Strategies

### Cases

* Sigmoid - 逻辑回归
* Softmax - 多元逻辑回归

### 通用算法

* SVM
  - 中小型复杂数据集
  - 对特征缩放敏感
* 决策树
  - 无需特征缩放 (feature scaling)
  - CART
  - 白盒
  - 对训练集旋转敏感
* 随机森林
  - 集成学习
  - 便于快速了解 特征重要度
* DNN
  - 梯度消失
  - 梯度爆炸
  - 过拟合
* CNN
  - Inception Network
  - GoogLeNet (Inception v1)
  - Inception-ResNet
  - Siamese Network
* 降维
  - 训练集维度越高, 越容易过拟合
  - PCA
* K-Means
  - 可用于降维
  - 可能收敛于局部最优解, 而非正确解
* DBSCAN
  - 对异常值具有鲁棒性
* GMM 高斯混合模型
  - 异常值检测

## Structuring Deep Learning Projects

* Orthogonalization
  - Happy cost function
  - Performs well in real world
* Single number evaluation metric
  - Combine metrics
* Satisficing and Optimizing metric
  - Optimizing metric: want to do as well as possible
  - Satisficing metrics: you'll be satisfice
* Train/dev/test distributions
  - Dev Test sets really come from the same distribution
  - Choose dev/test sets reflect data you expect to get in future
  - Set your test set to big enough to give high confidence in the overall performance of your system
* When to change dev/test sets and metrics
* Comparing to human-level performance
  - Whether bias avoidance tactics or variance avoidance tactics
  - Human-level error (Bias -> 0%) Training error (Variance) Dev error
* Reducing bias
  - bigger model
  - longer/better optimization algorithm
* Reducing variance
  - more data
  - regularization
* Error analysis
  - find a set of mislabeled examples
  - look at the mislabeled examples for false positives and false negatives
  - count up the number of errors that fall into various different categories

## DNN

* Activation function
* Forward and Backward propagation
  - https://en.wikipedia.org/wiki/Backpropagation
* Parameters vs Hyper parameters

* Train, Dev, Test sets
  - make sure that the dev and test sets come from the same distribution
  - it might be okay to not have a test set
* Bias, Variance
  - underfitting (bias), overfitting (variance)
  - high variance: (maybe) train set error 1%, dev set error 11%
  - high bias: (maybe) train set error 15%, dev set error 16%, human error 1%
* Regularization
  - prevent overfitting
  - L1/L2 regularization
* Dropout Regularization
  - drop out is very frequently used by computer vision
* Other regularization methods
  - data augmentation
  - early stopping
* Vanishing / Exploding gradients
* Gradient checking
* Mini-batch gradient descent
  - choosing mini-batch size
  - Exponentially weighted averages
  - Gradient descent with momentum
  - RMSprop (root mean square prop)
  - Adam optimization algorithm
  - Learning rate decay
* Hyperparameter tuning process
  - choose the hyperparameters at random
  - coarse to fine
  - Using an appropriate scale to pick hyperparameters
* Batch normalization
  - covariate shift
* Multi-class classification
  - Softmax Regression & Softmax classifier

## Convolutional Neural Networks (CNN)

* Example: edge detection, object detection, object localization
* Input (n*n), Filter (f*f), Output ((n-f+1)*(n-f+1))
* Padding input, make output size = input size
* Strided Convolutions:
  - Input (n*n)
  - Filter (f*f)
  - Padding (p)
  - Stride s
  - Output (((n+2p-f)/s+1)*((n+2p-f)/s+1))
* Convolutions Over Volume
* Pooling Layers
  - Max pooling
  - Avg pooling
* Fully connected layers (FC)
* ResNets (residual network)
* 1*1 convolution filter (network in network)
* Inception Network
* Convolutional Implementation of Sliding Windows
  - turn fully connected layers into convolutional layers
* YOLO algorithm (You Only Look Once)
  - Bounding Box Predictions
  - Intersection Over Union
  - Non-max Suppression
  - Anchor Boxes
* Transfer Learning
  - Download open source ways and use that as initialization for your problem
  - Add your own stuff
* One-shot Learning
  - similarity function
* Siamese Network
* Triplet Loss
  - Anchor, Positive, Negative
* Why Convolutions
  - parameter sharing
  - sparsity of connections
* R-CNN: Regions with convolutional networks or regions with CNNs
  - region proposals by segmentation algorithm

## Recurrent Neural Networks (RNN)

* Example: Natural Language Processing (NLP)
* Vanishing gradients with RNNs
* Gated Recurrent Unit (GRU)
* Long Short Term Memory (LSTM)
* Bidirectional RNN
* Deep RNNs
* Word Representation
  - featurized representation: word embedding
  - `t-SNE`
  - transfer learning
  - analogie using word vectors
  - cosine similarity
* Word2Vec algorithm
  - skip-gram model
  - hierarchical softmax classifier
* Negative Sampling algorithm
* GloVe (global vectors for word representation) algorithm
* Sentiment Classification
* Debiasing word embeddings
* Sequence-to-Sequence models
* Beam Search algorithm
* Bleu Score
* Attention Model

---

* 马尔可夫假设 -> 贝叶斯网络
* 贝叶斯网络 vs 条件随机场
* 期望最大化算法
* 最大熵模型
* 最小二乘法
* 在线学习
* EM 算法

## Linear-regression

### Gradient descent algorithm

```
1. scale the features, for example: [-1, 1]
2. mean normalization
```

```
debugging: by plotting the cost function

if your learning rate alpha is small enough,
then J(theta) should decrease on every iteration

learning rate is too small -> slow convergence

learning rate is too large, J(theta) may not decrease
on every iteration and it may not even converge
```

```
how to choose features:

1. maybe generate new features
2. polynomial regression
```

### Normal equation

* advantages
  - no need to iterate

* disadvantages
  - slow if features number is very large

### Large Scale Machine Learning

* Stochastic Gradient Descent
* Ceiling Analysis

------------------

## 特征工程

------------------

# History

------------------

## 2021

* [CS 329S: Machine Learning Systems Design](https://stanford-cs329s.github.io)

* [What are the most important statistical ideas of the past 50 years?](https://arxiv.org/pdf/2012.00174.pdf)

* [CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/)
