---
title: Machine learning
description: ~
date: 2021-03-21
---

------------------

# Timeline

------------------

# 2021

* [What are the most important statistical ideas of the past 50 years?](https://arxiv.org/pdf/2012.00174.pdf)

## Overview

### 特征工程

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

### 降维

* 数据集维度越高, 越稀疏, 越容易过拟合
* 投影 & 流形

* PCA 主成分分析
* LLE 局部线性嵌入 (流形)

### 无监督学习

### 概率图模型

### 优化算法

### 采样

### 前向神经网络

### 强化学习

### 集成学习

### 正则化

* 防止 过拟合
  - Dropout

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

* LSTM
* GRU
* Seq2Seq

### 生成模型

### 元学习

### GANs

* 传统概率生成模型 vs GANs
