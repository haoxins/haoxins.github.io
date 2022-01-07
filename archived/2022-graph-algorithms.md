---
title: Graph Algorithms for Data Science
description: 东城渐觉风光好, 縠皱波纹迎客棹. 绿杨烟外晓寒轻, 红杏枝头春意闹.
date: 2022-01-02
---

* [Graph Algorithms for Data Science](https://www.manning.com/books/graph-algorithms-for-data-science)

* Pathfinding algorithms
  - Dijkstra algorithm
  - Minimum weight spanning tree
  - Random walk
* Centrality algorithms
  - PageRank
  - Degree centrality
  - Betweenness centrality
  - Closeness centrality
* Community detection algorithms
  - Label propagation
  - Weakly connected components
  - Louvain modularity
  - Maximum k-Cut
* Similarity algorithms
  - Jaccard similarity algorithm
  - Euclidian similarity algorithm
  - Cosine similarity algorithm
* Node embedding algorithms
  - Node2Vec
  - GraphSAGE
  - TransE
  - DeepGL

## Representing network structure

> The most **basic** graph representation is the
  mathematical data structure **adjacency matrix**.

* An adjacency matrix is a **square matrix**, where
  the matrix elements indicate whether pairs of
  nodes are connected or not in the graph.
* The adjancency matrix **dimensions** are
  *equal to* the *number of nodes* in the graph.
* Another mathematical structure to represent
  networks is called the **edge list** data structure.
* An edge or relationship list is a simple
  data structure where each row represents a
  relationship of a given network.
  - Such as: `Source`, `Target`, `Weight`
  - One limitation of the edge list is that it does not
    allow isolated nodes to be present.
  - Isolated nodes are nodes without any relationships.
  - This limitation can be solved by introducing a
    **node list** next to the **edge list**.

```sql
(:Person {name: "Thomas"})
  -[:FRIEND {since: 2016}]
  ->(:Person {name: "Elaine"})
```

* From a performance perspective, the `index-free`
  adjacency versus a traditional join operation is
  the most important thing to consider when
  thinking about using a native graph database.
* As you can observe, the key **difference** from
  the RDF approach to graph modeling is that
  **labeled-property** graph (LPG) supports both
  node and relationship properties stored as
  **key-value pairs**.

* The graph model depends on your task, and with
  the **LPG** model, you can represent a literal
  value both as an internal node property
  (`key-value` pair) as well as a separate node.
  - Similarly, you have the option to represent
    the label as a separate node as well.

```sql
(:User)-[:PUBLISH]->(:Tweet)<-[:RETWEETS]-(:User)
```

> - With the LPG model, you can't create a relationship
    that is pointing to another relationship.
> - The beauty of the graph approach to data modeling
    is that you can always connect new
    information to an existing graph.

* When considering whether you want to store information
  **as separate nodes or node properties**, one thing
  to note is to examine if the **values are standardized**.
  - The whole point of using separate nodes to store
    information is to allow faster traversals at query runtime.

> One reason for that is that you **avoid** having nodes that
  can be connected to large parts of the graphs.

* An important consideration is that you want to
  **avoid generic relationship** types like `HAS`,
  where you could use it in many scenarios.
* What you don't want to end up is with
  a single relationship type that can lead to
  many different node types.
