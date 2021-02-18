---
title: Algorithms
description: 西当太白有鸟道, 可以横绝峨眉巅
date: 2020-11-09
---

## Common

* [Common used path planning algorithms with animations](https://github.com/zhm-real/PathPlanning)
* 贪心
* 分治
* 回溯
* 动态规划

## Graph

### 中心性算法

* 度中心性算法
  - 节点的连接数量最高
  - 应用: 受欢迎程度
* 接近中心性算法
  - Wasserman & Faust
  - 调和中心性算法
  - 更容易到达其他节点
  - 应用: 最佳位置
* 中间中心性算法
  - RA-Brandes
  - 哪个节点更能控制节点与群组之间的流
  - 应用: 控制关键点, 致病基因
* PageRank
  - 最重要节点

### 社团发现算法

* 度量算法
  - 三角形计数
  - 聚类系数
  - 应用: 群组稳定性
* 分量算法
  - 连通分量算法
    * 应用: 分组
  - 强连通分量算法 SCC
    * 应用: 推荐
* 标签传播算法 LPA
  - 应用: 挖掘共识
* Louvain 模块度算法
  - 应用: Fraud

------------------

## Distributed

* [The Raft Consensus Algorithm](https://raft.github.io)
* PBFT

------------------

## Quantum

------------------

## Websites

* [Algorithms, 4th Edition](https://algs4.cs.princeton.edu)
