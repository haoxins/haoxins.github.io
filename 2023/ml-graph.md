---
title: Graph Algorithms for Data Science
description: 东城渐觉风光好, 縠皱波纹迎客棹. 绿杨烟外晓寒轻, 红杏枝头春意闹.
date: 2022-01-02
---

- [Graph Algorithms for Data Science](https://www.manning.com/books/graph-algorithms-for-data-science)

> 一般般, 不推荐

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

## Projecting monopartite networks with Cypher Projection

> Due to worse performance, Cypher Projection is __not__
  recommended for larger graphs or the production phase.

## Inferring co-occurrence networks based off bipartite networks

- A bipartite network contains two sets or types of nodes.
  - The relationships always points from
    one type of nodes to another.
- The term co-occurrence network refers to a network
  construction method that analyzes relationships
  between various entities in a text.
- Co-occurrence networks are constructed by
  connecting pairs of entities in the text
  using a set of criteria defining co-occurrence.
  - The co-occurrence definition can
    vary from scenario to scenario.

```
Jaccard similarity coefficient ranges from values 0 to 1.
When there is no intersection of members between two sets,
the Jaccard similarity coefficient equals 0.
```

```
In graph context, a typical input to the Jaccard similarity
algorithm is a bipartite network consisting of two types
or sets of nodes. The idea behind using the Jaccard similarity
algorithm is to project a monopartite graph
based on the bipartite input graph.
```

## Constructing a nearest neighbor similarity network

- The most common metric to evaluate the similarity
  between two vectors is `cosine similarity`.
  - `Cosine similarity` is defined as the `cosine`
    of the angle between two vectors.

## Node embeddings and classification

> Node embedding models fall under the
  dimensionality reduction category.

- Every graph can be represented as an adjacency matrix.
  - An adjacency matrix is a square matrix where the elements
    indicate whether pairs of nodes are connected.
  - An adjacency matrix is regarded as a high-dimensional
    network representation as it grows with the
    number of nodes in the graph.

- The node embedding step is a unsupervised process since
  it has no training examples to learn from.
  - Node embedding models use techniques based on
    deep learning and nonlinear dimensionality
    reduction to achieve this.

---

- When dealing with a __transductive__ node embedding algorithm,
  you cannot calculate embeddings for nodes not seen during
  the initial embedding calculation.
  - You can think that transductive models create a vocabulary
    during initial computation, where the key of the vocabulary
    represents a node, and its value represents the embedding.
- On the other hand, __inductive__ node embedding models can
  calculate embeddings for unseen nodes
  during the initial computation.
  - For example, you can train a model based on the initial
    computation of node embeddings.
  - When a new node is introduced, you can calculate the
    embedding for the new node without re-calculating
    embeddings for the whole graph.

> One of the most simple and broadly used node
  embedding models is the `node2vec`.

-  Most node embedding models encode isolated nodes identically.

### Node2vec algorithm

- The `node2vec` algorithm is transductive and can be
  fine-tuned to capture either homophily
  or role-based embeddings.
  - The `node2vec` algorithm is heavily inspired by
    the `word2vec` skip-gram model.
- `Word2Vec` is a shallow, two-layer neural network
  that is trained to reconstruct linguistic
  contexts of words.
  - The objective of the `word2vec` model is to
    produce word representation (vectors)
    given a text corpus.
  - Word representations are positioned in the
    embedding space such that words that share
    common contexts in the text corpus are located
    close to one another in the embedding space.
- There are two main models used within
  the context of `word2vec`.
  - `Continuous Bag-of-Words (CBOW)`
  - `Skip-gram model`
- `Node2vec` is inspired by the skip-gram model.
  - The skip-gram model predicts the
    context for a given word.
  - The context is defined as the adjacent
    words to the input term.

---

- `Node2vec` uses random walks to generate a corpus
  of "sentences" from a given network.
  - The `node2vec` algorithm uses random walks to
    produce the sentences, which can be used as
    input to the `word2vec` model.
  - Each node in the random walk is treated as a
    word in the sentence, where the size of the sentence
    is defined with the walk length parameter.
  - Random walks start from all the nodes in the graph
    to make sure to capture all the nodes in the sentences.
  - These sentences are then passed to the `word2vec`
    skip-gram model as training examples.

---

- The `node2vec` algorithm implements
  second-order biased random walks.
  - The second-order walks take into account both the
    current as well as the previous state.
  - To put it simply, when the algorithm calculates the
    traversal probabilities, it also considers where
    it was at the previous step.
- Authors of the `node2vec` algorithm claim that
  approximating depth-first search will produce more
  community or homophily-based node embeddings.
  - On the other hand, the breadth-first search
    strategy for random walks encourages
    structural role embeddings.

## Link prediction

- You might run into data leakage problems if you
  used the same relationships to generate the
  network features and train the classification model.
- Data leakage occurs when your training data contains
  information about the output, but similar data will
  not be available when the model is used for predictions.
  - Leakage frequently leads to high performance during
    the training and possibly evaluation of the model,
    but unfortunately doesn't perform well for new predictions.
  - If you are using any graph features with the link
    prediction model, you have to take extra care to
    prevent any feature leakage.
  - Leakage in features refers to when a feature contains
    the same or comparable information as the output.

```
Remember, when a feature contains the same or comparable
information as the output variable but is unavailable
when making predictions, you have introduced
data leakage into the workflow.
The most obvious example is the network distance
between nodes in the graph. If the network features
and training examples are calculated on the same set
of relationships, then the model would simply learn that
relationships exist between nodes that are only one hop away.
However, none of the pairs of nodes without a link in the
network will be classified as probable to form a connection,
as none are one hop away. Even node embeddings based on the
homophily principle, could be problematic if you didn't
perform a proper dataset split.
```

- Overall, most of the graph-based features might
  introduce some data leakage issues. It is common
  to split the relationships into three sets
  to avoid data leakage problems.
  - Relationship set used to generate features
  - Relationship set used to train the model
  - Relationship set used to evaluate the model

> Therefore, it is common to subsample the negative
  examples and use about the same number of positive
  and negative samples in most link prediction workflows.

### Network feature engineering

> Remember, all the graph-based features for the
  train and test sets will be calculated strictly
  only on the feature set of relationships
  to prevent any data leakage.

1. The __network distance__ is calculated by finding
  the shortest path between the pair of nodes and then
  counting the number of relationships in the shortest path.
2. Another popular metric used in link prediction is the
  so-called __preferential attachment__.
  - Preferential attachment is an underlying organizing
    principle occurring in real-world networks where
    nodes with a higher number of relationships are
    more likely to make new relationships.
  - In the social network example, people with more friends
    are more likely to make new connections.
3. The next metric you will calculate as a link
  prediction feature is the __common neighbors__ metric.
  - The intuition behind the common neighbor metric is simple.
  - The more common neighbors two nodes have,
    the higher the chance of a link forming in the future.
4. The idea behind the __Adamic-Adar__ index is that the
  smaller degree the common neighbors between
  a pair of nodes have, the more likely that they will
  form a connection in the future.
5. The last link prediction that you will calculate is the
  __clustering coefficient__ of common neighbors.
  - A clustering coefficient measures the connectedness
    of the neighbors of a particular node.
  - The value ranges from `zero` to `one`.
  - A value of `zero` indicates that the neighboring nodes
    have no connections with each other.
  - On the other hand, the value of `1` indicates that the
    network of neighbors forms a complete graph where all
    the neighbors are connected.

## Knowledge graph completion

- Knowledge graph embedding models use triples to
  describe graphs. A triple consists of two nodes
  known as head `(h)` and tail `(t)`, and a
  labeled directed relationship `(r)`.
- `TransE` is one of the earliest and most intuitive
  knowledge graph embedding models. The objective of
  the `TransE` method is to calculate low-dimensional
  vector representations, also known as embeddings,
  for all the nodes and relationships in the graph.
