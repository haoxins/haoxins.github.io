---
title: Graph Algorithms for Data Science
description: 东城渐觉风光好, 縠皱波纹迎客棹. 绿杨烟外晓寒轻, 红杏枝头春意闹.
date: 2022-01-02
---

- [Graph Algorithms for Data Science](https://www.manning.com/books/graph-algorithms-for-data-science)

- Pathfinding algorithms
  - Dijkstra algorithm
  - Minimum weight spanning tree
  - Random walk
- Centrality algorithms
  - PageRank
  - Degree centrality
  - Betweenness centrality
  - Closeness centrality
- Community detection algorithms
  - Label propagation
  - Weakly connected components
  - Louvain modularity
  - Maximum k-Cut
- Similarity algorithms
  - Jaccard similarity algorithm
  - Euclidian similarity algorithm
  - Cosine similarity algorithm
- Node embedding algorithms
  - Node2Vec
  - GraphSAGE
  - TransE
  - DeepGL

## Representing network structure

> The most basic graph representation is the
  mathematical data structure **adjacency matrix**.

- An adjacency matrix is a **square matrix**, where
  the matrix elements indicate whether pairs of
  nodes are connected or not in the graph.
- The adjancency matrix **dimensions** are
  `equal to` the `number of nodes` in the graph.
- Another mathematical structure to represent
  networks is called the **edge list** data structure.
- An edge or relationship list is a simple
  data structure where each row represents a
  relationship of a given network.
  - Such as: `Source`, `Target`, `Weight`
- One limitation of the edge list is that it does not
    allow isolated nodes to be present.
  - Isolated nodes are nodes without any relationships.
  - This limitation can be solved by introducing a
    node list next to the edge list.

```sql
(:Person {name: "Thomas"})
  -[:FRIEND {since: 2016}]
  ->(:Person {name: "Elaine"})
```

- From a performance perspective, the `index-free`
  adjacency versus a traditional join operation is
  the most important thing to consider when
  thinking about using a native graph database.
- As you can observe, the key difference from
  the RDF approach to graph modeling is that
  **labeled-property** graph (LPG) supports both
  node and relationship properties stored as
  **key-value pairs**.

- The graph model depends on your task, and with
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

- When considering whether you want to store information
  **as separate nodes or node properties**, one thing
  to note is to examine if the **values are standardized**.
  - The whole point of using separate nodes to store
    information is to allow faster traversals at query runtime.

> One reason for that is that you **avoid** having nodes that
  can be connected to large parts of the graphs.

- An important consideration is that you want to
  **avoid generic relationship** types like `HAS`,
  where you could use it in many scenarios.
- What you don't want to end up is with
  a single relationship type that can lead to
  many different node types.

- You might have noticed that a common theme to
  network analysis is to translate indirect graph
  patterns and relationships to direct ones.
- Another frequent scenario is translating a
  bipartite network to a monopartite network.

## Your first steps with the Cypher query

- Using the `WITH` clause, you can manipulate the
  data as an intermediate step before passing the
  results to the next part of the Cypher query.

```sql
WITH 'Tomaz' AS first_name
WITH 'Bratanic' AS last_name, first_name
RETURN first_name + ' ' + last_name AS result
```

- The `WITH` clause affects the variables in scope.
  - Any variables not included in the `WITH` clause
    are not carried over to the next part of the query.

```sql
WITH 'Elon' AS first_name, 'Musk' as last_name
WHERE first_name = 'Elon'
RETURN *
```

- An important thing to note is that a `WHERE` clause
  only looks at and filters the output of the `WITH`
  statement and cannot stand on its own.

```sql
CREATE (elaine:Person{name: 'Elaine'}), (michael:Person {name: 'Michael'})
CREATE (elaine)-[f:FRIEND]->(michael)
RETURN *
```

- I can safely say that if you have nodes without
  a label in your graph, something is wrong with
  either your model or your import process.

```sql
MATCH (p:Person {name: 'Satish'})
RETURN p
```

- `Inline pattern matching` uses Cypher pattern syntax
  to describe a node or relationship pattern with its
  labels and properties.
- The opposite of inline pattern matching is using a
  `WHERE` clause to describe a graph pattern.

```sql
MATCH (p)
WHERE p:Person AND p.name = 'Satish'
RETURN p
```

- You can always have multiple `MATCH` clauses in a sequence.
  Similar to the `WITH` clause, the `WHERE` clause only
  applies to the previous `MATCH` clause.
- If you use many `MATCH` clauses in a sequence, make sure
  to append a `WHERE` clause to each `MATCH` clause where needed.
- A `WHERE` clause can only exist when it follows a
  `WITH`, `MATCH`, or an `OPTIONAL MATCH` clause.

```sql
MATCH (from:Person), (to:Person)
WHERE from.name = 'Satish' AND to.name = 'Elaine'
CREATE (from)-[:FRIEND]->(to)
RETURN *
```

- If only a single `MATCH` clause in the query
  retrieves no pattern from the database, the
  result of the query will be empty.
- If you do not want your query to stop when a
  single `MATCH` clause finds no existing graph
  patterns in the database, you can use the
  `OPTIONAL MATCH` clause.
- The `OPTIONAL MATCH` clause would return a
  `null` value if no matching patterns were found
  in the database instead of returning no results,
  behaving similarly as an `OUTER JOIN` in SQL.

- A `SET` clause is used to update labels of nodes
  and properties of both nodes and relationships.

```sql
MATCH (t:Person)
WHERE t.name = 'Satish'
SET t.interest = 'Gardening',
    t.hungry = True
```

```sql
MATCH (e:Person)
WHERE e.name = 'Elaine'
SET e += {hungry: false, pet: 'dog'}
```

- Note that if the `+=` operator of the `SET` clause
  is replaced with only `=`, then it overrides all
  existing properties with only those provided in the map.

- A good guideline to follow when using `multiple node labels`
  is that node labels should be **semantically orthogonal**.
  - Semantically orthogonal means that node labels shouldn't
    hold the same or similar meaning and should have nothing
    to do with one another.
  - Seconodary node labels are used to group nodes into
    different buckets, so that each subset is easily accessible.

- The `REMOVE` clause is the opposite of the `SET` clause.
  It is used to remove node labels and node and
  relationship properties.
  - Removing a node property can also be understood as
    setting its value to `null`.
- The `DELETE` clause is used to delete nodes and
  relationships in the database.
  - You cannot delete a node that still has
    relationships attached to it.
- As deleting nodes with existing relationships is a
  frequent procedure, the Cypher query language provides
  a `DETACH DELETE` clause that first deletes all the
  relationships attached to a node and
  then deletes the node itself.

```sql
MATCH (n:Person)
WHERE n.name = 'Elaine'
DETACH DELETE n
```

- The `MERGE` clause can be understood as a combination
  of using both `MATCH` and `CREATE` clauses.
  - Using the `MERGE` clause, you instruct the query
    engine first to try to match a given graph pattern,
    and if it does not exist,
    it should then create this pattern.
- The `MERGE` clause only supports inline graph pattern
  description and cannot be used in
  combination with a `WHERE` clause.
- A `MERGE` clause can be followed by optional
  `ON CREATE SET` and `ON MATCH SET`.

- Handling **relationships** is a bit different.
  - If there can be at most a single relationship of
    one type between two nodes, then do not include
    any relationship properties in the `MERGE` clause.
  - Instead, use the `ON CREATE SET` or `ON MATCH SET`
    clauses to set any relationship properties.
  - However, if your graph model contains multiple
    relationships of the same type between a pair of nodes,
    then only use the unique identifier property of the
    relationship in the `MERGE` statement and set any
    additional properties the same as above.

```sql
CREATE CONSTRAINT IF NOT EXISTS ON (u:User) ASSERT u.id IS UNIQUE;
```

- There are, however, some **constraints** you can add
  to your graph model to ensure data integrity.
  - In my graph journey, I have only used the
    `unique node property constraint` so far.

```sql
LOAD CSV WITH HEADERS FROM
"https://raw.githubusercontent.com/a/b/main/users.csv" as row
WITH row
LIMIT 5
RETURN row
```

- One thing to note is that the `LOAD CSV` clause returns
  all values as `strings` and makes no
  attempt to identify data types.

```sql
LOAD CSV WITH HEADERS FROM
"https://raw.githubusercontent.com/a/b/main/users.csv" as row
MERGE (u:User{id:row.id})
ON CREATE SET u.name = row.name,
              u.username = row.username,
              u.registeredAt = datetime(row.createdAt)
```

- When dealing with larger CSV files, you can use the
  `USING PERIODIC COMMIT` clause to split the import
  into several transactions.
  - By default, `USING PERIODIC COMMIT` clause will
    split the transaction for every `1000` rows.

```sql
CALL db.schema.visualization()
```

## Cypher aggregations and social network analysis

```sql
MATCH (n:User)
WHERE (n)<-[:MENTIONS]-()
AND NOT EXISTS {
  MATCH (original)<-[:PUBLISH]-(n)<-[:MENTIONS]-()-[:RETWEETS]->(original)
}
RETURN count(*) AS countOfUsers
```

### Node degree distribution

- With a directed network, you can split the
  degree distribution into in-degree and
  out-degree distribution.
- The `apoc.agg.statistics` function returns
  statistical values such as `mean`, `max`, and
  `percentile` values of given values.

```sql
MATCH (u:User)
WITH u, size((u)-[:FOLLOWS]->()) as outDegree
RETURN apoc.agg.statistics(outDegree)
```

### Graph Catalog and Native projection

- Graph algorithms in the **GDS** library are
  executed on a projected in-memory graph structure
  separate from the graph stored in the database.

```sql
CALL gds.graph.create(
  graphName,
  nodeProjection,
  relationshipProjection,
  optional configuration
)
```

### Weakly Connected Component algorithm

- The first graph algorithm you will execute is the
  `Weakly Connected Component` algorithm, or **WCC**
  in short.
  - It is used to find disconnected parts or islands
    within a network.
  - The WCC algorithm is probably one graph algorithm
    that should be executed as the first step of any
    graph analysis to evaluate graph connectivity.

```sql
CALL gds.wcc.write('follower-network', {writeProperty: 'followerWcc'})
YIELD componentCount, componentDistribution
```

### Strongly Connected Components algorithm

- The only difference between the **Weakly** and
  `Strongly Connected Components` algorithm (**SCC**)
  is that the SCC algorithms considers
  relationship directions.
- The `Strongly Connected Component` algorithm
  is useful when directed paths and reachability
  plays an important role.

### Local clustering coefficient

- The `local clustering coefficient`,
  or **LCC** for short, is a **metric** that
  quantifies how connected or close the
  neighbors of a particular node are.
  - The LCC value ranges from `zero` to `one`.
  - The LCC value of `0` indicates that the
    neighboring nodes have no connections between
    each other.
  - On the other hand, the LCC value of `1` indicates
    that the network of neighbors forms a complete
    graph, where all the neighbors are connected.
- The LCC algorithm provides a metric to evaluate
  how strongly the neighbors of a node are connected.
  - You can calculate the LCC value of a single node
    by dividing the number of existing links between
    neighbor nodes with the number of possible links
    between neighbor nodes.
  - You can use this formula to calculate the LCC on
    a directed graph as well.

## Introduction to social network analysis

