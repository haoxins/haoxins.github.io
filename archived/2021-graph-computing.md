---
title: Graph Computing
description: 可怜楼上月裴回, 应照离人妆镜台. 玉户帘中卷不去, 捣衣砧上拂还来.
date: 2021-08-29
---

### GraphScope GAIA

* [GAIA](https://www.usenix.org/biblio-6260)
  - https://www.usenix.org/conference/nsdi21/presentation/qian-zhengping
  - GAIA: A System for *Interactive Analysis* on
    Distributed Graphs Using a High-Level Language

* In particular, *GAIA* makes the following
  technical contributions.
  - **Scope Abstraction**. We propose the
    *Scope abstraction* to allow GAIA to dynamically
    track fine-grained data dependencies in a
    Gremlin query. This enables Gremlin traversal to
    be modeled as a dataflow graph for efficient
    parallel execution with correctness guarantee.
  - **Bounded-Memory Execution**. Leveraging the
    Scope abstraction, we are able to devise
    advanced optimizations in parallel graph traversal,
    such as bounded-memory execution and early-stop
    optimization, which lead to further runtime
    improvement and memory saving.

* GAIA runs queries via a set of worker processors
  in a shared-nothing cluster, where each worker
  executes a fragment of the computation.
  - For each query, GAIA first compiles it into a
    dataflow graph, then it partitions the source
    operator in the dataflow according to the
    input graph partition, with the segment of
    operators that follow the source replicated
    across the set of workers.
    - A local executor manages the computation
      on each worker by scheduling the
      operators to run.
    - It starts from the source operator and
      repeatedly executes the following ready
      operators. Here, an operator is ready if
      all its inputs are available to consume.
* For now, GAIA requires the users to manually
  specify a degree of parallelism (DOP)
  for a query upon submission.
  - We leave it as an interesting future work to
    automatically derive the DOP.
* According to the DOP, the local executor
  parallelizes the operators to execute
  on the multiple CPU cores.

* **Dynamic Scheduling**. For each operator, GAIA
  packs a segment of consecutive traversers in a
  stream into a single batch, and such a batch
  constitutes the finest data granularity for
  communication and computation.
  - A task can be logically viewed as the combination
    of an operator and a batch of data to be computed.
  - GAIA dynamically creates tasks corresponding to
    each operator when there is one or more batches
    available from all its inputs.
  - The local executor maintains all the tasks in
    a same scheduling queue to share resources.

------------------

* [Graph Databases](https://book.douban.com/subject/26427118/)
  - 副标题: *New Opportunities for Connected Data*
  - [GQL Standard](https://www.gqlstandards.org)
  - *英文版同样不推荐*

> - 公司最近调研 **Neo4j** (结论: *不采用*)

* Labeled Property Graph Model

> - Relational Databases Lack Relationships

* Labels in the Graph
  - Using labels in this way, we can group nodes.
