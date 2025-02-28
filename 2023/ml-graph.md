---
title: Graph Algorithms, 图表征学习, 扩散模型
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

- Most node embedding models encode isolated nodes identically.

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

## Construct a graph using NLP techniques

```
Large Language Models, such as the GPT-4 from OpenAI [2023],
have been a game-changing introduction to the world of
natural language procesing. Their ability to understand
human-like text has presented remarkable opportunities in
the field of information extraction. With a model trained on
diverse internet text, they can sift through massive amounts
of data, understanding the context, and pull out relevant details,
making the information extraction pipelines more accessible.
Their ability to generalize allows them to be applied to a
variety of domains, from academic research to business analytics,
extracting valuable insights from unstructured data.
```

------------------

- [图表征学习](https://book.douban.com/subject/36477924/)
  - 干货不多, 勉强算个入门书籍~

### 图嵌入

- 若游走中的边不存在重复, 则该游走也称为`迹`;
  此外, 若游走中的节点和边均不存在重复,
  则该游走称为一条`路径`.

```
DeepWalk 的核心思想是通过类比图上的随机游走和自然语言, 即每个节点相当于一个单词,
并将图中每个采样得到的游走视为自然语言中的一个句子.
DeepWalk 作者发现, 短距离随机游走中节点的概率分布与自然语言中的单词概率分布十分相似.
基于这一观察, DeepWalk 提出借鉴自然语言处理的单词嵌入来学习图的节点嵌入.
具体来说, DeepWalk 采用单词嵌入的 SkipGram 模型.
```

- 具体来说, Node2vec 采用的有偏随机游走为一个二阶马尔可夫过程,
  即随机游走的下一个节点概率取决于之前的两个节点.
  - 总而言之, 通过调整 `p` 和 `q` 的取值,
    Node2vec 可以获得不同特性的有偏随机游走,
    因此更具有灵活性.

```
由于 AROPE 仅需要在原始的稀疏邻接矩阵 A 上计算一次特征分解,
其时间复杂度与图规模呈线性关系, 可以扩展到大规模图. 此外,
在保持不同阶邻近度时, AROPE
仅需计算对应的变换而无须重新计算特征值分解或奇异值分解,
因此该算法可以在不同阶邻近度间快速切换,
以支持高效并有效地保持不同阶邻近度.
```

```
因此, 基于随机游走的图嵌入方法等价为构造特殊的相似度矩阵并计算矩阵分解.
一方面由于随机游走过程不需要显式地构造相似度并计算其矩阵分解,
因此随机游走方法的计算效率往往较高; 另一方面,
由于现实中随机游走的数量是有限的,
因此随机游走方法相当于在优化过程中进行了近似,
而直接采用矩阵分解方法可以更有效地优化目标函数.
```

### 图神经网络

```
概括来说, 卷积定理证明, 函数卷积的傅里叶变换是函数傅里叶变换的乘积.
因此, 利用谱图理论可以将该定理扩展到图数据上,
即两个图信号的卷积是其图傅里叶变换的乘积.
所以, 图卷积操作等价为如下过程:
首先利用图傅里叶变换将图上节点特征 (即若干图信号) 从空域转换到谱域,
在谱域与可学习的滤波器进行乘积操作, 然后再将处理后的特征通过图傅里叶逆变换转换回空域,
即得到处理后的图信号. 其中, 谱域图神经网络的可学习参数与谱域滤波器相关.
类比图像上的卷积神经网络, 上述过程均是可微分的,
因此谱域图神经网络可以实现图数据上端到端的学习.
```

```
谱域图卷积定义为三个步骤:
(1) 通过图傅里叶变换将两组图信号从空域转换到谱域;
(2) 在谱域上计算向量点乘;
(3) 将处理后的图信号经过图傅里叶逆变换转换回空域上.
```

```
与切比雪夫图卷积神经网络类似, 图卷积神经网络不需要显式地计算拉普拉斯矩阵的特征分解,
也无须切比雪夫图卷积神经网络中的递归计算, 因此图卷积神经网络的计算效率很高.
从图卷积神经网络的计算公式可以看出, 其计算复杂度与图中边的数量呈线性关系.
此外, 由于图卷积神经网络可被写为简单的矩阵形式, 其编程实现也非常便捷.

在每一层图卷积中, 每个节点的表征仅与其邻居节点相关,
因此图卷积神经网络有很强的空间局部性. 事实上,
图卷积神经网络也可从空域图神经网络角度理解,
从而将谱域图神经网络与空域图神经网络有效地联系到了一起.
```

```
由于消息传递图神经网络的所有操作都是连续可微分的,
因此消息传递图神经网络可以进行端到端的学习.
不难看出, 与前文介绍的空域图神经网络类似,
消息传递图神经网络也是通过在图的邻居结构上定义函数,
聚合邻居信息以更新节点表征的.
```

```
层次图池化模型的核心思想是逐步"粗化"处理图,
即有序减小图的规模, 并保留图的层次结构信息,
直至学习到所需要颗粒度的图表征.
```

### 图表征学习理论分析


------------------

- [深度生成模型](https://book.douban.com/subject/36503836/)

```
DDGM 和分层 VAE 之间的区别在于变分后验的定义和隐变量的维度,
但它们的整个构造是基本相同的. 我们可以联想到其学习目标是什么 --
是的, 是 ELBO!
```

------------------

- [扩散模型](https://book.douban.com/subject/36489324/)
  - 比下面那本同名书籍好一些

```
具体来说, VAE 通过在潜在变量空间中引入一个先验分布来确保模型可以生成具有多样性的样本.
这个先验分布通常是高斯分布或者混合高斯分布. 在训练过程中,
VAE 尝试最大化重建数据的对数似然, 同时最小化模型学习到的潜在变量与先验分布之间的差异.
这个差异可以使用 KL 散度来度量, KL 散度是一种用于衡量两个分布之间差异的度量.
```

```
Transformer 模型 (2018 年):
它使用自注意力机制来捕捉输入序列中不同位置之间的依赖关系, 从而更好地处理长文本序列.
Transformer 模型在机器翻译和文本生成等任务中取得了非常好的效果, 是预训练技术的一个重要里程碑.

大规模预训练模型 (2018 年至今):
例如, BERT, GPT 等. 这些模型使用更大规模的数据集进行训练,
并且使用更复杂的网络结构和训练策略来提高效果和泛化能力.
这些大规模预训练模型在自然语言处理领域取得了非常显著的成果,
并且成为当前自然语言处理研究的一个重要方向.
```

------------------

- [扩散模型](https://book.douban.com/subject/36482946/)
  - 一般般

------------------

- [这就是 ChatGPT](https://book.douban.com/subject/36449803/)
  - 一般般
