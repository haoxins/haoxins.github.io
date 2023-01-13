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
  $$ V_i $$ is split into the `in-degree` of the vertex,
  defined as the number of edges for which $$ V_i $$ is
  their *end node* (the *head* of the arrow) and the
  `out-degree` of the vertex, which is the number of
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

* Such advantages can be summarized as follows:
  - Multiple data sources, such as geographical
    or GPS information, social network data,
    user personal profiles, family data, and
    the like, can be merged in a single
    connected source of truth.
  - Existing data can be extended with external
    sources of knowledge (shop locations,
    people's addresses, and so on) or with
    contextual information (a new shop, other
    complaints, and the like) that can be used
    to improve the analysis.
  - The same data model can support several
    analysis techniques.
  - Data can be visualized as a graph to
    speed the manual analysis.
  - The analysis can be extended to multiple
    levels of interaction, considering
    multiple hops.
  - The structure simplifies the merging and
    cleaning operation, thanks to the flexible
    access pattern provided by the graph model.

* The key concerns of MDM
  (*master data management *) include:
  - Managing changes over time as organizational
    structures change, businesses merge, and
    business rules evolve
  - Incorporating new sources of data
  - Supplementing existing data with
    external data sources
  - Addressing the needs of reporting, compliance,
    and business intelligence consumers
  - Versioning data as its values and schema change

* When done correctly, MDM has numerous advantages
  that can be summarized as follows:
  - Streamlining data sharing among
    personnel and departments
  - Facilitating computing in multiple system
    architectures, platforms, and applications
  - Removing inconsistencies and duplications from data
  - Reducing unnecessary frustration when
    searching for information
  - Simplifying business procedures
  - Improving communication throughout the organization

* Graph-based MDM has the following advantages:
  - *Flexibility*: The data captured can be easily
    changed to include additional attributes and objects.
  - *Extensibility*: The model allows the rapid evolution
    of the master data model in line
    with changing business needs.
  - *Search capability*: Each node, each relationship, and
    all their related properties are search entry points.
  - *Indexing capability*: Graph databases are naturally
    indexed by both relationships and nodes, providing
    faster access compared to relational data.

* A proper native graph database, on the other hand,
  uses a graph model for storing and processing the
  data, making graph manipulation straightforward,
  intuitive, and performant.
* An interesting way of classifying graph processing,
  organized along three dimensions:
  - graph dynamism,
  - algorithm types,
  - and workload types

* The graph data model, on the other hand, is
  highly relationship-oriented. Each node can be
  related to any other node, so a graph doesn't
  have predictable lookups. It also has a highly
  mutable structure: with few new links and
  few new nodes, the connection
  structure can change heavily.
* Moreover, due to the dynamic nature of the
  graphs, graphs and their access patterns can
  change rapidly and unpredictably at run time,
  making this solution inconvenient
  to implement in practice.
* With these challenges in mind, generally
  speaking, there are *three techniques* for
  *scaling a graph database*:
  - **Application-level sharding**
  - **Increasing the RAM or using cache sharding**
  - Cache sharding isn't sharding in the
    traditional sense, because we expect the
    full dataset to be present on each database
    instance. To implement cache sharing, we
    partition the workload undertaken by each
    database instance to increase the
    likelihood of hitting a warm cache for
    a given request. (Warm caches in graph
    databases like Neo4j are highly performant.)
  - **Replication**

* Data replication consists of maintaining
  multiple copies of data, called *replicas*,
  on separate computers.
  Replication has several purposes:
  - *System availability*
  - *Performance*
  - *Scalability*
  - *Application requirements*

> - Data replication has clear benefits,
    but keeping the different copies
    synchronized is a challenge.

* Due to the highly connected nature of graphs,
  implementing either a centralized primary copy
  protocol or a distributed protocol is a
  difficult task, one that has serious effects
  on performance and data consistency,
  to mention the most critical.
* Therefore, we will focus on the *centralized*
  approach with a single master, also described
  as `master/slave` replication.

* *Native* vs. *non-native* graph databases

* Native graph databases are designed to use
  the filesystem in a way that not only
  understands but also supports graphs, which
  means that they are both highly performant
  and safe for graph workloads.
* In more detail, a native graph DBMS exhibits
  a property called index-free adjacency, which
  means that each node maintains direct references
  to its adjacent nodes. The adjacency list
  representation is one of the most common ways
  to represent sparse graphs.

* The *adjacency list representation* can be
  similarly modified to support many other graph
  variants too. In such a representation, each
  node acts as a microindex of other nearby nodes,
  which is much cheaper than using global indexes.
* A traversal across a relationship in such a
  database has a constant cost, irrespective of
  the size of the graph. Also, the query times
  are independent of the total size of the graph;
  instead, they are proportional to the amount
  of the graph searched.

* A native graph architecture provides many
  advantages that make it generally superior to
  a nonnative approach to managing graph models.
  We can summarize these advantages as follows:
  - "Minutes-to-milliseconds" performance:
  - Read efficiency
  - Disk space optimization
  - Write efficiency

* Label property graphs

* A property graph has the following properties
  (defined here in a platform-agnostic way):
  - The graph consists of a set of entities.
    An entity represents either a
    node or a relationship.
  - Each entity has an identifier that uniquely
    identifies it across the entire graph.
  - Each relationship has a direction, a name
    that identifies the type of the relationship,
    a start node, and an end node.
  - An entity can have a set of properties, which
    are typically represented as `key/value` pairs.
  - Nodes can be tagged with one or more labels,
    which group nodes and indicate the roles
    they play within the dataset.

* As for relational databases, there are some
  best practices or style rules for defining
  a model for a graph. The labels for nodes
  *should be singular*, for example, because
  they represent a specific entity, whereas
  the names for the relationships
  *should reflect the direction*.

## Graphs in machine learning applications

* **Graph modeling**: Data is converted to some
  graph representation by means of a modeling
  pattern. The information is the same, only in
  a different format, or the data is aggregated
  to make it more suitable to feed
  into the learning process.
* **Graph construction**: A new graph is created,
  starting from the data available. The resulting
  graph contains more information than before.

* The graph representation is helpful for the following tasks:
  - *Feature selection*: Querying a relational database or
    extracting a key from a value in a NoSQL database is
    a complex undertaking. A graph is easy to query and
    can merge data from multiple sources, so finding and
    extracting the list of variables to use for training
    is made simpler by the graph approach.
  - *Data filtering*: The easy-to-navigate relationships
    among objects make it easy to filter out useless data
    before the training phase, which speeds the
    model-building process.
  - *Data preparation*: Graphs make it easy to clean the
    data, removing spurious entries, and to merge data
    from multiple sources.
  - *Data enrichment*: Extending the data with external
    sources of knowledge or looping back the result of
    the modeling phase to build a bigger knowledge base
    is straightforward with a graph.
  - *Data formatting*: It's easy to export the data in
    whichever format is necessary:
    vectors, documents, and so on.

* **Identify the data sources**. Identify the data
  available for algorithm training purposes, as well
  as the sources from which such data can be extracted.
* **Analyze the data available**. Analyze each data
  source available, and evaluate the content, in terms
  of quality and quantity.
* **Design the graph data model**. This step is twofold.
  According to the specific analytics requirements,
  you must
  - Identify the meaningful information to be
    extracted from the data sources.
  - Design a specific graph model, considering the
    data available, access patterns, and extensibility.
* **Define the data flow**. Design the architecture
  of the ingestion process (known as the ETL process)
  that extracts, transforms, and loads the data from
  the multiple sources into the graph database,
  using the schema designed.
* **Import data into the graph**.
* **Perform postimport tasks**. Before you start
  the analysis, the data in the graph might require
  some preprocessing. These tasks include
  - *Data cleaning*
  - *Data enrichment*
  - *Data merging*

* The resulting graph can be generalized
  as a **co-occurrence** graph.

* **PageRank** This algorithm works by
  counting the number and quality of edges
  to a node to arrive at a rough estimate
  of the node's importance. The basic idea
  implemented by the PageRank model, invented
  by the founders of Google for their
  search engine, is that of voting or
  recommendation. When a node is connected to
  another node by an edge, it is basically
  casting a vote for that node. The more votes
  a node receives, the more important it is
  but the importance of the "voters" matters too.
  Hence, the score associated with a node is
  computed based on the votes that are cast
  for it and the scores of the nodes casting those votes.
* **Betweenness centrality** This algorithm measures
  the importance of a node by considering how often
  it lies on the shortest paths between other nodes.
  It applies to a wide range of problems in
  network theory. In a supply chain network,
  for example, a node with higher betweenness
  centrality will have more control of the
  network because more goods will pass through that node.

## Basic approaches to graph-powered fraud detection

* This expert-based approach, even though it is
  useful and still common in many domains,
  suffers from several disadvantages:
  - Rule-based engines are typically complex
    and therefore expensive to build because
    they require advanced manual
    input by fraud experts.
  - This complexity makes them difficult
    to maintain and manage.
  - Rules must be kept up to date because
    fraudsters are continually evolving their
    approaches and coming up with new ones.
    As soon as they discover the rules behind
    the fraud reduction system, they change
    their behavior to avoid being recognized.
  - In most cases, these systems require
    further human follow-up, analysis,
    and investigation.

## Proximity-based algorithms

* The most common ways to define proximity
  for outlier analysis are
  - **Cluster-based** The data points are split
    into clusters, using whatever technique is
    most appropriate, considering how the elements
    are represented and how accurate the algorithm
    should be. The outlier score is computed by
    using the nonmembership of a data point in any
    of the clusters, its distance from other
    clusters, the size of the closest cluster,
    or a combination of these factors. Points
    belong to clusters or should be
    considered to be outliers.
  - **Density-based** A local region is defined
    for each data point
    (perhaps based on grid position), and the
    number of other points in that region is
    used to define a local density value. This
    value can be converted to an outlier score,
    with elements with higher scores considered
    to be outliers.
  - The basic assumption of density-based outlier
    detection methods is that the local density
    around a nonoutlier object is similar to the
    local density around its neighbors, whereas
    the local density around an outlier object
    is significantly different from the local
    density around its neighbors.
  - Whereas *cluster-based* methods partition
    the data points, density-based methods
    partition the data space.
  - **Distance-based** For each data point, the
    *k-nearest* neighbor (`k-NN`) network is
    computed. The outlier score is computed by
    using the distance of a data point to its
    *k-nearest* neighbors; the data points with
    the largest `k-NN` distances are marked as
    outliers. *Distance-based* algorithms
    typically perform better than the other
    methods presented here because they have
    higher granularity.
  - In both *clustering* and *density-based* methods,
    the data is aggregated before outlier analysis
    by partitioning the points or the data space,
    and the individual data points are compared
    with those distributions for analysis.
  - In *distance-based* methods, the outlier
    score is based on the `k-NN` distance to the
    original data points. This greater
    granularity often comes at a significant
    computational cost, but that cost can be
    mitigated by using graphs and
    some other techniques.
