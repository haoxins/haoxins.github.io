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

* You might have noticed that a common theme to
  network analysis is to translate indirect graph
  patterns and relationships to direct ones.
* Another frequent scenario is translating a
  bipartite network to a monopartite network.

## Your first steps with the Cypher query

* Using the `WITH` clause, you can manipulate the
  data as an intermediate step before passing the
  results to the next part of the Cypher query.

```sql
WITH 'Tomaz' AS first_name
WITH 'Bratanic' AS last_name, first_name
RETURN first_name + ' ' + last_name AS result
```

* The `WITH` clause affects the variables in scope.
  - Any variables not included in the `WITH` clause
    are not carried over to the next part of the query.

```sql
WITH 'Elon' AS first_name, 'Musk' as last_name
WHERE first_name = 'Elon'
RETURN *
```

* An important thing to note is that a `WHERE` clause
  only looks at and filters the output of the `WITH`
  statement and cannot stand on its own.

```sql
CREATE (elaine:Person{name:'Elaine'}), (michael:Person {name: 'Michael'})
CREATE (elaine)-[f:FRIEND]->(michael)
RETURN *
```

* I can safely say that if you have nodes without
  a label in your graph, something is wrong with
  either your model or your import process.

```sql
MATCH (p:Person {name:'Satish'})
RETURN p
```

* *Inline pattern matching* uses Cypher pattern syntax
  to describe a node or relationship pattern with its
  labels and properties.
* The opposite of inline pattern matching is using a
  `WHERE` clause to describe a graph pattern.

```sql
MATCH (p)
WHERE p:Person AND p.name = 'Satish'
RETURN p
```

* You can always have multiple `MATCH` clauses in a sequence.
  Similar to the `WITH` clause, the `WHERE` clause only
  applies to the previous `MATCH` clause.
* If you use many `MATCH` clauses in a sequence, make sure
  to append a `WHERE` clause to each `MATCH` clause where needed.
* A `WHERE` clause can only exist when it follows a
  `WITH`, `MATCH`, or an `OPTIONAL MATCH` clause.

```sql
MATCH (from:Person), (to:Person)
WHERE from.name = 'Satish' AND to.name = 'Elaine'
CREATE (from)-[:FRIEND]->(to)
RETURN *
```

* If only a single `MATCH` clause in the query
  retrieves no pattern from the database, the
  result of the query will be empty.
* If you do not want your query to stop when a
  single `MATCH` clause finds no existing graph
  patterns in the database, you can use the
  `OPTIONAL MATCH` clause.
