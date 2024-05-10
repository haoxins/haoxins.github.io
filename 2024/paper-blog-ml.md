---
title: Paper & Blog - 数据, 模型
description: 惊起却回头, 有恨无人省. 拣尽寒枝不肯栖, 寂寞沙洲冷.
date: 2023-09-07
---


```

```

---

  - Submitted on 11 Feb 2024 (v1),
    last revised 28 Feb 2024 (this version, v4)
  - [GitHub](https://github.com/alibaba/GraphTranslator)

---

- [Multimodal Foundation Models: From Specialists to General-Purpose Assistants](https://arxiv.org/abs/2309.10020)

```
In a nutshell, all the image-only contrastive learning methods,
share the same high-level framework, detailed below.
1. Given one image, two separate data augmentations are applied;
2. A base encoder is followed by a project head,
which is trained to maximize agreement using a contrastive loss
(i.e., they are from the same image or not);
3. The project head is thrown away for downstream tasks.
```

```
For dual encoders such as CLIP, image and text are encoded separately,
and modality interaction is only handled via a simple dot product of
image and text feature vectors. This can be very effective for
zero-shot image classification and image-text retrieval.
However, due to the lack of deep multimodal fusion,
CLIP alone performs poorly on the image captioning and
visual question answering tasks.
This requires the pre-training of a fusion encoder,
where additional transformer layers are typically employed to
model the deep interaction between image and text representations.
```

```
Stable Diffusion (SD), and its academic version latent diffusion,
contains mainly three modules, i.e.,
an image VAE, a denoising U-Net, and a condition encoder.

The denoising U-Net is the core module for the
diffusion image generation process. The module is trained to
predict the noise to subtract in the latent space at
each denoising timestep, such that it can step-by-step evolve
the initial random noise into a meaningful image latent.
The module is trained with the L2 loss between the
predicted noise and the target noise, which is added to the
target image latent encoded by the VAE encoder.

At inference, the iteratively denoised latent started
from the random noise, is sent through the
VAE decoder for the final generated image.

The denoising U-Net, similar to a classic U-Net,
consists of a series of spatial downsampling and upsampling
blocks with skip connections in between.
In SD's U-Net, each down/upsampling block has a cross-attention
layer and a 2D convolutional down/upsampling layer.
Each block takes the visual latent feature, text feature,
and denoising step as input and
generates the next visual latent feature.
The image-text interaction happens in the
image-text cross-attention layer.
```

---

- [OpenELM: An Efficient Language Model Family with Open-source Training and Inference Framework](https://arxiv.org/abs/2404.14619)
  - Submitted on 22 Apr 2024
  - [CoreNet](https://github.com/apple/corenet)

```
At the core of OpenELM lies layer-wise scaling,
enabling more efficient parameter allocation across layers.
This method utilizes smaller latent dimensions in the attention
and feed-forward modules of the transformer layers closer to the input,
and gradually widens the layers as they approach the output.
```

```
We adopt the decoder-only transformer-based architecture.
Following state-of-the-art LLMs, we:
(1) do not use learnable bias parameters in any fully-connected
(a.k.a., linear) layers,
(2) apply pre-normalization using RMSNorm and also,
use rotatory positional embedding (ROPE)
for encoding positional information,
(3) use grouped query attention (GQA)
instead of multi-head attention (MHA),
(4) replace the feed-forward network (FFN) with SwiGLU FFN,
(5) use flash attention for computing the scaled
dot-product attention, and
(6) use the same tokenizer as LLama.
```

```
Existing LLMs use the same configuration for each
transformer layer in the model, resulting in a uniform
allocation of parameters across layers.
Unlike these models, each transformer layer in OpenELM
has a different configuration
(e.g., number of heads and feed-forward network dimension),
resulting in a variable number of parameters in each layer of the model.
This lets OpenELM to better utilize the available parameter budget
for achieving higher accuracies. We implement this non-uniform
allocation of parameters across layers using layer-wise scaling.
```

```
Layer-wise scaling.
A standard transformer layer is composed of
multi-head attention (MHA) and feed-forward network (FFN).
For non-uniform allocation of parameters in the
transformer layer, we adjust the number of attention heads
and the FFN multiplier in each transformer layer.
```

> 其实没啥内容! 大体上就是项目介绍;
  然后就是宣布 Apple 入场了.

> 急急忙忙地拼凑个成果出来的感觉~

---

- [Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/)
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
  - [Benchmarking nearest neighbors](https://github.com/erikbern/ann-benchmarks)

---

- [Graph Pattern Matching in GQL and SQL/PGQ](https://arxiv.org/abs/2112.06217)

```
The identical core of both PGQ and GQL is a graph
pattern matching sub-language, here termed GPML.
```

```
In contrast, property graphs are multigraphs
(there can be multiple edges between two endpoint nodes);
pseudo-graphs (there can be an edge looping from a node to itself);
they are mixed, or partially directed:
an edge can be undirected,
or can have source and target nodes,
in which case it is directed from the source to the target.

They are also attributed: graph elements can have attributes
(a disjoint union of labels and properties).
```

> 为啥要回顾过去种种? 哈哈

```sql
-- label expressions

MATCH (x:Account)
```

```
label expressions allow
conjunctions (&),
disjunctions (|),
negations (!),
and grouping of individual labels by using parentheses.
```

```sql
-- all undirected edges can be recovered by

MATCH ~[e]~

-- if we want edges that are either undirected,
-- or directed from right to left, we could write

<~[e]~
```

```
Similarly to node patterns, edge patterns
need not specify an element variable.
```

```
Orientation               Edge pattern

Pointing left              <−[ spec ]−
Undirected                 ~[ spec ]~
Pointing right             −[ spec ]−>
Left or undirected         <~[ spec ]~
Undirected or right        ~[ spec ]~>
Left or right              <−[ spec ]−>
Left, undirected or right  −[ spec ]−
```

```
If we do not specify direction and write
(x)−[e]−(y),
then each edge will be returned twice,
once for each direction in which it is traversed.
```

```sql
-- the reuse of variable s ensures that one
-- starts and ends in the same node:

MATCH (s)−[:Transfer]−>(s1)−[:Transfer]−>(s2)−[:Transfer]−>(s)
```

```sql
-- Path patterns permit the use of path variables:
-- in the returned bindings,
-- such a path variable is bound to a whole path. In

MATCH p = (s)−[:Transfer]−>(s1)−[:Transfer]−>(s2)−[:Transfer]−>(s)

-- the variable p will be bound to paths of length three of
-- Transfer edges that start and end in the same node.
```

```sql
-- In general, we can put arbitrarily many path patterns together.
-- For example, we can modify the above query by adding a
-- condition that another login attempt into an account
-- was made that did not use a phone:

MATCH (s:Account)−[:SignInWithIP]−(),
      (s)−[t:Transfer WHERE t.amount > 1M]−>(),
      (s)~[:hasPhone]~(p:Phone WHERE p.isBlocked = 'yes')
```

```
Quantifier  Description
{m, n}      between m and n repetitions
{m,}        m or more repetitions
*           equivalent to{0,}
+           equivalent to{1,}
```

```sql
-- a path of length 2 to 5 of Transfer edges
-- can be sought as follows:

MATCH (a:Account)−[:Transfer]−>{2, 5}(b:Account)
```

```
Keyword  Description

TRAIL    No repeated edges.
ACYCLIC  No repeated nodes.
SIMPLE   No repeated nodes,
         except that the first and last nodes may be the same.
```

```
Keyword           Description

ANY SHORTEST      Selects one path with shortest length
                  from each partition. Non-deterministic.
ALL SHORTEST      Selects all paths in each partition that
                  have the minimal length in the partition.
                  Deterministic.
ANY               Selects one path in each partition arbitrarily.
                  Non-deterministic.
ANY 𝑘             Selects arbitrary 𝑘 paths in each partition
                  (if fewer than 𝑘, then all are re- tained).
                  Non-deterministic.
SHORTEST 𝑘        Selects the shortest 𝑘 paths
                  (if fewer than 𝑘, then all are retained).
                  Non-deterministic.
SHORTEST 𝑘 GROUP  Partitions by endpoints, sorts each partition
                  by path length, groups paths with the same length,
                  then selects all paths in the first 𝑘 groups
                  from each partition (if fewer than 𝑘,
                  then all are retained). Deterministic.
```

```
The key steps in the pattern-matching execution model,
as reflected in the forthcoming standard, are as follows.

Normalization
GPML provides syntactic sugar to help write patterns;
this step puts patterns in a canonical form.

Expansion
The pattern is expanded into a set of rigid patterns
without any kind of disjunction. Intuitively,
a rigid pattern is one that could be expressed by an
SQL equi-join query. Formally, it is a pattern without
quantifiers, union, or multiset alternation.
The expansion also annotates each rigid pattern to enable
tracking the provenance of the syntax constructs.

Rigid-pattern matching
For each rigid pattern, one computes a set of path bindings.
Each elementary construct of the rigid pattern is computed
independently and then the results are joined together
on variables with the same name.

Reduction and deduplication
The path bindings matched by the rigid patterns are reduced
by removing annotations. The reduced path bindings are then
collected into a set. This implies a deduplication step
since different path bindings might become equal
after reduction, and only one copy is kept.
```

---

- [Enhancing Data Lakes with GraphAr: Efficient Graph Data Management with a Specialized Storage Scheme](https://arxiv.org/abs/2312.09577)
  - [GitHub](https://github.com/apache/incubator-graphar)

```
However, integrating LPGs into data lakes
introduces unique challenges:

Firstly, there is no standardized way to encapsulate
an LPG within the existing data lake architecture.

Secondly, executing graph-specific operations,
particularly neighbor retrieval, and label filtering,
can be highly inefficient in this setup.
```

```
Firstly, Parquet provides flexible and efficient
support for various datatypes, including atomic
types (e.g., bools and integers), and nested
and/or repeated structures (e.g., arrays and maps).
Using Parquet as the fundamental building block,
GraphAr further introduces standardized YAML files
to represent the schema metadata for LPGs.
This combination of data organization and metadata
management enables the complete expression of LPG
semantics while ensuring compatibility with both
data lakes and graph-related systems.

Secondly, GraphAr incorporates specialized
optimization techniques to improve the performance
of two critical graph operations:
neighbor retrieval and label filtering,
which are not inherently optimized in existing formats.

GraphAr facilitates neighbor retrieval by organizing
edges as sorted tables in Parquet to enable an efficient
CSR/CSC-like representation and leveraging Parquet's delta
encoding to reduce overhead in data storage and loading.
GraphAr also introduces a novel decoding algorithm that
utilizes BMI and SIMD instructions, along with a unique
structure named PAC (page-aligned collections), to further
accelerate the neighbor retrieval process.
In addressing another critical aspect of LPGs, GraphAr
adapts the run-length encoding (RLE) technique from Parquet
and introduces a unique merge-based decoding algorithm.
This tailored approach significantly improves label filtering
performance, whether it involves simple or complex conditions.
```

> 至此, 已可确认值得一读!

```
Parquet files contain three layers of metadata:
file metadata, column metadata, and page header metadata.
The file metadata directs to the starting points of each
column's metadata. Inside the column chunks and pages,
the respective column and page header metadata are stored,
offering a detailed description of the data. This includes
data types, encoding, and compression schemes, facilitating
efficient and selective access to data pages within columns.
```

> 花了过多的篇幅去描述: Why GraphAr?

```
Parquet is utilized as the payload file format for
storing the data in the physical storage,
while YAML files are used to capture schema metadata.
```

```
Edges are sorted first by source vertex IDs
and then by destination vertice IDs.

An auxiliary index table, denoted as <offset>, is introduced
to enable more efficient vertex-centric operations.
The <offset> table aligns with the partitions in the
vertex table, and when applied to the source vertices,
facilitates retrieval patterns similar
to Compressed Sparse Row (CSR).

GraphAr allows for efficient retrieval of neighbors
in both outgoing and incoming directions,
through two sorted tables for the same edge type.
CSR, CSC, and COO are widely adopted for representing graphs,
by emulating these formats, GraphAr ensures
compatibility with existing graph systems.
```

```
Delta encoding works by representing the gaps (deltas) between
consecutive values instead of storing each value individually.
The deltas, which often have small values,
can be stored more compactly, requiring fewer bits.

However, delta encoding involves data dependencies that make
vectorization challenging. The decoding of the (i + 1)-th
neighbor depends on the prior decoding of the i-th neighbor.
```

```
Therefore, we utilize this BMI-based approach for miniblocks
with a bit width of 1 to 4 bits, while resorting to the default
delta decoding of Parquet for larger bit widths.
The combination of data layout, delta encoding, and this
adaptive decoding strategy results in an advanced topology
management paradigm, enabling efficient neighbor retrieval.
```

```
This run-length format naturally transforms the binary
representation of a label into an interval-based structure.
We then adopt a list P to define the positions of intervals.
The i-th interval is represented by [P[i], P[i + 1]),
where P[i] refers to the i-th element within P.
Besides, it is required to record whether the vertices of
the first interval [P[0], P[1]) contain the label or not,
i.e., the first value.
```

> Arrow, Parquet, 要是 Rust 重写就好了~ 哈哈哈

```
Since graphs generally have significantly more edges than
vertices and GraphAr employs CSR/CSC-like layouts requiring
edge sorting, generating topological data becomes
the most time-intensive part.
```

```
We can generate topological data for over
3.9 million edges per second.
The process involves three steps:
1) sorting the edges using Arrow/Acero's
   internal order_by operator, labeled as "sort";
2) generating vertex offsets, labeled as "offset"; and
3) writing the sorted and offset data into Parquet files
   with a specific encoding, labeled as "output".

Generally, this process has a time complexity of
O(|E| log|E|) sequentially.
Considering this transformation is a one-time, offline operation
that substantially reduces future data retrieval times,
the associated overhead is acceptable.
```

> benchmarks 蛮务实~

```
Storage efficiency: GraphAr remarkably reduces storage requirements,
using only 27.3% of the storage compared to baseline methods for
storing topology, and as low as 2.9% for label storage on average.
```

```
Graph databases: There are also graph databases that are designed
to store and manage graph data. While they offer various features
that are tailored for LPGs, they primarily focus on in-memory
mutable data management, operating at a higher level compared to
GraphAr. GraphAr, with its format compatible with the LPG model,
can be utilized as an archival format for graph databases.
```

---

- [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687)
  - Submitted on 18 Aug 2023 (v1)
  - [GitHub](https://github.com/spcl/graph-of-thoughts)

```
Overall, we observe that GoT is particularly
well-suited for tasks that can be naturally
decomposed into smaller subtasks that are solved
individually and then merged for a final solution.
```

```
The GoT architecture consists of a set of interacting modules.
These modules are the Prompter
(which prepares the messages for the LLM),
the Parser (extracts information from LLM thoughts),
the Scoring module (verifies and scores the LLM thoughts),
and the Controller
(coordinates the entire reasoning process,
and decides on how to progress it).

The Controller contains two further important elements:
the Graph of Operations (GoO) and the Graph Reasoning State (GRS).
GoO is a static structure that specifies the graph decomposition
of a given task, i.e., it prescribes transformations to be
applied to LLM thoughts, together with their order & dependencies.
GRS is a dynamic structure that maintains the state of the ongoing
LLM reasoning process (the history of its thoughts and their states).
```

> 举的例子`不具有`代表性,
  Analysis results 也就参考价值不大.
  所以通篇的说服力不足~

> 总的来说, __阅读价值不大__!

---

- [Monte-Carlo Graph Search from First Principles](https://github.com/lightvector/KataGo/blob/master/docs/GraphSearch.md)

```
All else equal, under this naive way of extending MCTS from
trees to graphs, if a node's top-preferred moves are visited
a lot by transposing lines, the node will tend to favor
exploring other moves that didn't receive as many visits instead,
leading to artificial biases in the utilities of the playouts
being averaged at different nodes.

Our algorithm is unsound to the point where even with
unbounded amounts of search, it's not obvious that we
will converge to the optimal move.
```

```
Overall, this gives us an equivalent but different
perspective on how MCTS works. MCTS is continuously
optimizing a policy at every node to maximize the
Q utility values that child nodes are reporting,
while continuously updating the node's own Q to be
the latest best guess of the expected utility
achievable by that policy.

In the limit of infinite search, if the child node Q
values converge to game-theoretic optimal, then the
node's policy converges to optimal, so the node's Q
converges to the game-theoretic optimal value too,
and so by recursion/induction we can
see easily that MCTS is sound.
```

```
All of the problems when extending MCTS naively to graphs
are a result of implicitly assuming that the only visits
to children of a parent node come from the parent.
When a child node can instead also receive visits from a
transposing path, we have problems:

The visit counts of the child nodes can deviate arbitrarily
much from what PUCT would have wanted to allocate, and so the
child visits distribution can no longer be interpreted as a
reasonable posterior policy.

The Q values of parent and child nodes are updated in inconsistent
ways, such that the Q value can no longer be interpreted as the
expected value of the posterior policy either.
```

---

- [GraphRAG: Unlocking LLM discovery on narrative private data](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)
  - [graspologic](https://github.com/microsoft/graspologic)

```
Baseline RAG struggles to connect the dots.
This happens when answering a question requires traversing
disparate pieces of information through their shared
attributes in order to provide new synthesized insights.

Baseline RAG performs poorly when being asked to holistically
understand summarized semantic concepts over large data
collections or even singular large documents.
```

```
Creating LLM-generated knowledge graphs

The LLM processes the entire private dataset,
creating references to all entities and relationships
within the source data, which are then used to create
an LLM-generated knowledge graph.

This graph is then used to create a bottom-up clustering
that organizes the data hierarchically into semantic clusters.
This partitioning allows for pre-summarization of semantic
concepts and themes, which aids in holistic
understanding of the dataset.

At query time, both of these structures are used to provide
materials for the LLM context window when answering a question.
```

```
Looking forward, we plan to work closely with customers on
a variety of new domains as we continue to apply this
technology while working on metrics and robust evaluation.
```

---

- [A Review on Graph Neural Network Methods in Financial Applications](https://arxiv.org/abs/2111.15367)
  - 2021 (v1), 2022 (v2)
  - [GitHub](https://github.com/ProsusAI/finBERT)

```
While GCN equally treats the neighbors of the target node,
it often occurs that some neighbors may be
more influential than others.

It is also worth mentioning that since GAT can learn
the weights of the neighboring node, we could interpret
the learned attention weights as a relative
importance measure, to better understand the model.
```

```
An undirected graph has a symmetric adjacency matrix that
guarantees a semi-definite Laplacian matrix, which lays
the foundation for applying GCN.
The directed graph, on the other hand, may have an
asymmetric adjacency matrix and could be handled by
spatial-based GNN methods, such as GAT.

In practice, there is not much work developing methodologies
for directed graphs, since they could be processed by
spatial-based GNN methods or
making the adjacency matrix symmetric.
However, there is also a line of work developing GNN
methodology to predict sequences of events
represented as a directed graph.
```

```
To capture the sequential pattern in the dynamic graph,
a common approach is to train a GNN to generate the
node embedding at each time stamp and then utilize a
recurrent neural network to aggregate the information.
```

```
How to improve the scalability of GNNs is vital but challenging.
Computing the Laplacian matrix becomes hard with millions of
nodes and for a graph of irregular Euclidean space,
optimizing the algorithm is also difficult.
Sampling techniques may partially solve the problem with
the cost of losing structural information.
Thus, how to maintain the graph structure and improve the
efficiency of GNN algorithms is worth further exploration.
```

---

- [Relational Deep Learning: Graph Representation Learning on Relational Databases](https://arxiv.org/abs/2312.04615)
  - [GitHub](https://github.com/snap-stanford/relbench)
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
