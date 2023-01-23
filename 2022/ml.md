---
title: 机器学习 - 西瓜, 南瓜
description: 晚年惟好静, 万事不关心. 自顾无长策, 空知返旧林.
date: 2022-07-31
---

- [机器学习](https://book.douban.com/subject/26708119/)
- [机器学习公式详解](https://book.douban.com/subject/35381195/)

- 任意实矩阵
  $$ A \in \mathbb{R}^{m \times n} $$
  都可分解为
  - $$ A = U \Sigma V^{T} $$,
    (`A.33`)
  - 其中,
    $$ U \in \mathbb{R}^{m \times m} $$
    是满足
    $$ U^{T} U = I $$
    的 `m` 阶酉矩阵;
  - $$ V \in \mathbb{R}^{n \times n} $$
    是满足
    $$ V^{T} V = I $$
    的 `n` 阶酉矩阵;
  - $$ \Sigma \in \mathbb{R}^{m \times n}
    是
    $$ m \times n $$
    的矩阵,
  - 其中
    $$ (\Sigma)_{ii} = \sigma_{i} $$
    且其他位置的元素均为 `0`,
    $$ \sigma_{i} $$
    为非负实数且满足
    $$ \sigma_1 \ge \sigma_2 \ge ... \ge 0 $$.
- 式 (`A.33`) 中的分解称为奇异值分解 (简称 `SVD`), 其中 `U` 的列向量
  $$ u_{i} \in \mathbb{R}^{m} $$
  称为 `A` 的左奇异向量, `V` 的列向量
  $$ v_{i} \in \mathbb{R}^{n} $$
  称为 `A` 的右奇异向量,
  $$ \sigma_{i} $$
  称为奇异值.
  - 矩阵 `A` 的秩 (`rank`) 就等于非零奇异值的个数.

## 模型评估与选择

## 线性模型

## 决策树

## 神经网络

## 支持向量机

## 贝叶斯分类器

## 集成学习

## 聚类

## 降维与度量学习

## 特征选择与稀疏学习

## 计算学习理论

## 半监督学习

## 概率图模型

## 规则学习

## 强化学习
