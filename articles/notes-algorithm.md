---
title: Algorithm notes
description: 算法
date: 2020-11-09
---

* [Common used path planning algorithms with animations](https://github.com/zhm-real/PathPlanning)
* [The Raft Consensus Algorithm](https://raft.github.io)

## Graph

### 搜索/遍历

* 广度优先 BFS
  - 应用: 查找邻节点
* 深度优先 DFS
  - 应用: 最优路径

### 最短路径

* Dijkstra
* A*
* Yen
* 单源最短路径 SSSP

### 最小生成树

* 经过所有节点的最佳路径
* 应用: 垃圾回收

### 随机游走

* 应用: 扩充训练数据集

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
