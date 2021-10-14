---
title: Graph-Powered Machine Learning
description: 三山半落青天外, 二水中分白鹭洲. 总为浮云能蔽日, 长安不见使人愁.
date: 2021-09-12
---

* [Graph-Powered Machine Learning](https://book.douban.com/subject/35135117/)
  - https://www.manning.com/books/graph-powered-machine-learning

## Machine learning and graphs: An introduction

* When you face new problems or tasks that you
  would like to solve with a computer program,
  the following questions can help you
  decide whether to use machine learning:
  - Is the specific task *too complex to be programmed*?
  - Does the task require any sort of
    *adaptivity throughout its life*?

* In *stream analytics*, in which it is necessary
  to process a stream of data to reveal short-term
  anomalies, storing data in the form
  of a graph could be useless.

* Even the *best learning algorithm* on the
  **wrong data** produces the **wrong results**.

* For complex problems, data often matters
  more than algorithms.
  - Increasing the amount of data available
    during the training phase improved the
    performance of all the learners.

* Data concerns can be summarized in four categories:
  - Insufficient quantity of data
  - Poor quality of data
  - Nonrepresentative data
  - Irrelevant features

* *Feature selection* and *feature extraction* represent
  two important tasks during the preparation of data.

* Data management constraints and requirements
  - Managing big data
  - Designing a flexible schema
  - Developing efficient access patterns

* Performance is a complex topic in machine learning
  because it can be related to multiple factors:
  - Predictive accuracy
  - Training performance
  - Prediction performance

* In this context, graphs could provide the proper
  storage mechanism for both source and model data,
  reducing the access time required to read data as
  well as offering multiple algorithmic techniques
  for improving the accuracy of the predictions.

* The model's structure is related directly to the
  specific algorithm or the algorithm class employed.

* In *directed* graphs, an edge $$ E_{ij} $$ can be
  traversed from $$ V_i $$ to $$ V_j $$ but not
  in the opposite direction; $$ V_i $$ is
  called the *tail*, or *start* node, and $$ V_j $$ is
  called the *head*, or *end* node.

* Two vertices `x` and `y` of `G` are defined as
  **adjacent**, or **neighbors**, if `{x, y}` is an
  edge of `G`. The edge $$ E_{ij} $$ connecting them
  is said to be **incident** on the
  two vertices $$ V_i $$ and $$ V_j $$.

* One of the most important properties of a vertex
  in a graph is its **degree**, defined as the total
  number of edges incident to that vertex, which is
  also equal to the number of neighbors of that vertex.

* In a *directed* graph, the degree of a vertex
  $$ V_i $$ is split into the *`in-degree`* of the vertex,
  defined as the number of edges for which $$ V_i $$ is
  their *end node* (the *head* of the arrow) and the
  *`out-degree`* of the vertex, which is the number of
  edges for which $$ V_i $$ is their *start node*
  (the *tail* of the arrow).

* A **path** with no repeating vertices is called a
  **simple path**. A **cycle** is a path in which the
  *first and the last vertex coincide*.

* We refer to these forces as **surrounding contexts**:
  factors that exist outside the vertices and edges
  of a network but nonetheless affect how the
  network's structure evolves over time.

* Understanding the **surrounding contexts** and the
  related forces that act on a network helps with
  machine learning tasks in multiple ways:
  - Networks are conduits for both wanted
    and unwanted flows.
  - Understanding such forces allows the prediction
    of how the network will evolve over time,
    and enables data scientists to proactively react
    to such changes or use them for
    specific business purposes.
  - Findings in sociological and psychological
    disciplines point to the relevance of a
    person's social network in
    determining their tastes, preferences,
    and activities. One of the problems related
    to recommendation engines is the *cold-start*
    problem: Social networks and the homophily
    principle can be used to make a recommendation
    based on the tastes of connected users.

* *Graph-powered* **data management** features include
  - **Connected sources of truth**: Graphs allow you
    to merge multiple data sources into a
    single uniform, connected dataset ready for
    the training phase.
  - This feature represents a great advantage by
    reducing *data sparsity*, increasing the amount
    of data available, and simplifying data management.
  - **Knowledge graphs**: Building on the previous
    idea, knowledge graphs provide a homogeneous
    data structure for combining not only data
    sources, but also prediction models, manually
    provided data, and external sources of knowledge.
  - The resulting data is machine ready and can
    be used during training, prediction,
    or visualization.
  - **Fast data access**: Tables provide a single
    access pattern related to row and column filters.
    *Graphs*, on the other hand, provide multiple
    access points to the same set of data.
  - This feature improves performance by reducing
    the amount of data to be accessed to the
    baseline minimum for the specific set of needs.
  - **Data enrichment**: In addition to making it
    easy to extend existing data with external
    sources, the schemaless nature of graphs
    and the access patterns provided within graph
    databases help with data cleaning and merging.
  - **Feature selection**: Identifying relevant
    features in a dataset is key in several
    machine learning tasks, such as classification.
  - By providing fast access to data and multiple
    query patterns, graphs speed feature
    identification and extraction.

* *Graph-powered* **data analysis** features include
  - **Graph algorithms**: Several types of graph
    algorithms, such as *clustering*, *page ranking*,
    and *link analysis* algorithms, are useful for
    identifying insights in the data and for
    analysis purposes.
  - Moreover, they can be used as a first data
    preprocessing step in a more
    complex analysis process.
  - **Graph-accelerated machine learning**: The
    graph-powered feature extraction discussed
    earlier is an example of how graphs can
    speed or improve the quality of the
    learning system. Graphs can help in
    *filtering*, *cleaning*, *enriching*, and
    *merging* data before or
    during training phases.
  - **Network dynamics**: Awareness of the
    surrounding contexts and related forces
    that act on networks allows you not only
    to understand network dynamics, but also
    to use them to improve the quality
    of the predictions.
  - **Mixing models**: Multiple models can
    coexist in the same graph, taking advantage
    of flexible and fast access patterns,
    provided that they can be merged during
    the prediction phase. This feature improves
    final accuracy. Moreover, the same model
    sometimes can be used in different ways.
  - **Fast model access**: Real-time use
    requires fast predictions, which implies
    a model that can be accessed as fast as
    possible. Graphs provide the right
    patterns for these scopes.

## Graph data engineering

* **Collect**: Data from multiple data
  sources is gathered and collected.
* **Store**: The data is stored in a
  proper way in a single
  (or occasionally more than one)
  easy-to-access data store so that
  it's ready for the next phases.
* **Clean**: The data is merged, cleaned,
  and (whenever possible) normalized by
  using a unified and homogeneous schema.
* **Access**: The data is available. Multiple
  views or access patterns are provided to
  simplify and speed access to the dataset
  that will be used for training purposes.

* **Volume**
  - Scalable storage
  - Scalable processing
* In a big data platform, graphs can help address
  volume issues by playing two roles:
  - Main data source
  - Materialized views
* **Velocity**
* **Variety**
* **Veracity**

> With a *feedback loop*, the system learns continuously
  by *monitoring* the effectiveness of predictions and
  *retraining* when needed. Monitoring and using the
  resulting feedback are at the
  core of machine learning.

* From the specific model, it is possible to abstract
  a more generic approach. The problem and process
  can be generalized as follows:
  - There is a lot of data in the form of events.
  - The data is distributed across
    multiple data sources.
  - The data needs to be aggregated and organized
    in a form that simplifies further
    processes and analysis.
  - From the first aggregation format, some
    views are created.
  - At the same time, some real-time view of
    the last events needs to be stored
    to react fast to those events.
* Some important and relevant aspects of this
  data flow affect the architecture
  of the machine learning project:
  - The events logged are raw, immutable, and true.
    They will not change because of the analysis
    performed; they just happen. It is necessary to
    store the events one time and in a raw format.
  - Multiple views are created as functions
    (aggregation is one example) on this data, and
    they can change according to the
    algorithms used for the analysis.
  - The view-building process generally operates on
    the entire set of data, and this process can
    take time, especially when it operates on a
    large amount of data, as in our specific use case.
    The time required to process the data creates
    a gap between the view of current events
    and previous events.
  - To have a real-time view of the data, it is
    necessary to fill this gap. The real-time view
    requires a kind of streaming process that reads
    the events and appends information to the views.

* The primary concept of the *Lambda Architecture*
  is to build big data systems as a series of
  three layers: `batch`, `serving`, and `speed`.

## Graphs in machine learning applications

## Content-based recommendations

## Collaborative filtering

## Session-based recommendations

## Context-aware and hybrid recommendations

## Basic approaches to graph-powered fraud detection

## Proximity-based algorithms

## Social network analysis against fraud

## Graph-based natural language processing

## Knowledge graphs
