---
title: Paper & Blog - 机器学习
description: 惊起却回头, 有恨无人省. 拣尽寒枝不肯栖, 寂寞沙洲冷.
date: 2023-09-07
---

### 图
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
