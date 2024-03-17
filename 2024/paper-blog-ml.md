---
title: Paper & Blog - 机器学习
description: 惊起却回头, 有恨无人省. 拣尽寒枝不肯栖, 寂寞沙洲冷.
date: 2023-09-07
---


---

  - [OasysDB](https://github.com/oasysai/oasysdb)
  - OasysDB is an embeddable, efficient, and
    easy to use vector database. It is designed to be used
    as a library and embedded inside your AI application.
  - It is written in Rust and uses
    [Sled](https://github.com/spacejam/sled)
    as its persistence storage engine to save
    vector collections to the disk.
  - OasysDB implements __HNSW__
    (Hierachical Navigable Small World)
    as its indexing algorithm.

### 图

---

- [Relational Deep Learning: Graph Representation Learning on Relational Databases](https://arxiv.org/abs/2312.04615)
  - https://github.com/snap-stanford/relbench
  - 其实这里上下文中的 Databases 是 Datasets

```
Crucially, RDL models natively integrate temporality by
only allowing entities to receive messages from
other entities with earlier timestamps.
```

```
Dimension tables tend to have relatively few rows,
as it is limited to one per real-world object.

Typically, features in dimension tables are static
over their whole lifetime, while fact tables usually
contain temporal information with a dedicated time
column that denotes the time of appearance.
```

```
In practice, training tables can be computed using
time-conditioned SQL queries from
historic data in the database.
```

```
Given a relational entity graph and a training table,
we need to be able to query the graph at specific points
in time which then serve as explicit training examples
used as input to the model.

The computational graphs obtained via neighbor sampling
allow the scalability of our proposed approach to modern
large-scale relational data with billions of table rows,
while ensuring the temporal constraints.
```

```
Heterogeneous Message Passing -> Temporal Message Passing
```

```
The model described so far is task-agnostic and simply
propagates information through the relational entity graph
to produce generic node embeddings.
We obtain a task-specific model by combining our graph with a
training table, leading to specific model heads and loss functions.
We distinguish between (but are not limited to) two types of tasks:
node-level prediction and link-level prediction.
```

```
In practice, we rely on PyTorch Frame that supports a variety of
modality-specific encoders, such as pre-trained text embedding models,
and as well as state-of-the-art deep learning models on tabular data.
```

```
In other words, the GNN is an exact neural version of SQL
JOIN+AGGREGATE operations. We believe this is another important
reason why message passing-based architectures are a natural learned
replacement for hand-engineered features on relational tables.
```

```
Unfortunately, recent studies find that many GNN architectures
fail to distinguish biconnected graphs.
Further work is needed to design expressive n-partite graph models.
```

> Query Language Inspired Models. 不敢苟同~

```
Because of this, Relational Deep Learning seeks to
leverage relations to learn entity representations,
but does not need to learn an embedding space that
perfectly preserves all relation semantics.
This gives more freedom and flexibility to our models,
which may discard certain relational information
it finds unhelpful.
Nonetheless, adopting ideas from knowledge graph
embedding may yet be fruitful.
```

---

- [GraphScope Flex: LEGO-like Graph Computing Stack](https://arxiv.org/abs/2312.12107)
  - [GART](https://github.com/GraphScope/GART)
  - [GRIN](https://github.com/GraphScope/GRIN)
  - 一晃两年过去了, GraphScope 也改架构了~
  - [Vineyard](https://github.com/v6d-io/v6d)

```
Resource Description Framework (RDF):
RDFs sconsist of triples-subject, predicate, and object -
that denote relationships (predicates) between
two entities or nodes (subject and object).
This model facilitates the representation and
integration of data from disparate sources,
commonly used in knowledge bases.
```

```
As a query or algorithm is received, GraphScope Flex
compiles it into a distributed execution plan,
which is partitioned across multiple compute nodes
for parallel processing. Each partition independently
operates on its own compute node and synchronizes
with other partitions via a coordinator.

Upon receiving a query from the application layer,
the query is parsed into a unified intermediate representation.
This is followed by optimization through a universal
Query Optimizer and catalog module.
The optimized logical plan employs code generation modules
to produce the corresponding physical plan.
```

```
In GraphScope Flex, Vineyard serves as the backend storage
for in-memory graphs. It adopts the property graph data model
and handles graph partitioning using edge-cut partitioning.

GraphScope Flex has incorporated a mutable in-memory graph storage,
GART, which supports multi-version concurrency control
(MVCC) for dynamic graph data.
Specifically, GART always provides consistent snapshots of
graph data (identified by a version), and it updates the graph
with the version number write_version.
```

```
GraphAr serves as the default persistent format for GraphScope Flex.
Additionally, it can be directly used as a data source
for applications by integrating GRIN.
One of the key features of GraphAr is its ability to efficiently
partition graph data into multiple data chunks,
using the columnar storage feature and chunking mechanisms
of ORC and Parquet.
This unique design enables it to retrieve
only the relevant data chunks, potentially in parallel,
eliminating the need to load the entire graph
into memory before processing.
Furthermore, GraphAr empowers certain graph-related operations
to be executed directly at the storage layer,
such as retrieving vertices with a specific label or
fetching the neighbors of a given vertex,
using the built-in indexes of GraphAr.
```

> 看下来, 感觉 GraphScope 想要做成似乎不太容易.
  __愿景过大__!