---
title: Graph Databases in Action
description: 此时相望不相闻, 愿逐月华流照君. 鸿雁长飞光不度, 鱼龙潜跃水成文.
date: 2021-08-08
---

* [Graph Databases in Action](https://book.douban.com/subject/34700758/)

* [GQL Standard](https://www.gqlstandards.org)

```
Key-value        (Redis)
  Wide-column    (Cassandra, HBase)
    Document     (MongoDB)
      Relational (MySQL, Postgres)
        Graph    (Dgraph, CosmosDB)

Simple -> Complex
```

> Our first decision was to pick the type of database.
> We decided to use a **labeled property graph** database,
> instead of, for example, an **RDF store** or **triplestore** database.

> In the end, we decided to use the
> Apache **TinkerPop** version 3.4.x framework

* **Gremlin**

## Graph data modeling

> entities and relationships are treated with
> equal importance in a graph database

* Why can't I use SQL?

> Relational databases (in a fit of naming irony)
> are rather poor at representing rich relationships.

### Cases study

* Recursive queries
  - unbounded recursive queries

> let's examine how we determine a person's reporting hierarchy.

```sql
CREATE TABLE org_chart (
  employee_id          SMALLINT NOT NULL,
  manager_employee_id  SMALLINT NULL,
  employee_name        VARCHAR(20) NOT NULL
);
```

```js
g.V().
  repeat(
    out('works_for')
  ).path().next()
```

* river crossing puzzle

```zsh
T (the boat and the farmer)
G (the goose)
F (the fox)
B (the barley)
_ (the river)
```

```js
g.V('TFGB_').
  repeat(
    out()
  ).until(hasId('_TGFB')).
  path().next()
```

```zsh
TFGB_ -take goose-> FB_TG
      -take empty-> TFB_G
      -take barley-> F_TGB
      -return goose-> TFG_B
      -take fox-> G_TBF
      -return empty-> TG_FB
      -take goose-> _TGFB

TFGB_ -take goose-> FB_TG
      -take empty-> TFB_G
      -take fox-> B_TFG
      -return goose-> TGB_F
      -take barley-> G_TBF
      -return empty-> TG_FB
      -take fox-> _TGFB
```

* Just because a problem can be represented as a graph
  doesn't necessarily mean that a graph database is
  the best technology to choose to solve that problem.

* Should use graph database
  - related or recursive data
  - pattern matching
  - centrality, clustering, and influence

```
Relational databases solve 88 out of 100 application issues well,
so feel free to use them for those problems.
```

* The main difference is that we must shift from an
  `"entity first"` mindset
  (or perhaps more accurately, an `"entity-only"` mindset)
  to an `"entity and relationship"` mindset.

* **Entity**,
  **Relationship**,
  **Attribute**,
  **Access pattern**
  - We usually make our choice based on
    the predominant `access patterns`.

* Four-step process for data modeling
  - Understand the problem (core access patterns)
  - Create a whiteboard or conceptual model
  - Create a logical data model
  - Test the model

> we have found that singular names tend to be
> a better fit for graph data modeling.

* Because relationships are first-class
  citizens in a graph data model,
  both vertices and edges can have
  properties associated with those.

* **Naming**
  - We could have gone with the name *User*,
    but this is specific to one type of
    potential person within the application.
  - While we currently do not have this requirement,
    we might need to represent other types of people,
    such as *employees* or *owners*, in the future.

* **lower_snake_case**, **singular**

> It is generally a safe bet that each vertex
> in a graph database can only be associated
> with a single label.
> That is the approach of Apache *TinkerPop*.

* *uniqueness*
  - single uniqueness edge
  - multiple uniqueness edge

> **Incorrect edge uniqueness** is one of the most
> common problems in graph data modeling,
> and it is frequently a root cause of query issues.

* Checklist
  - Do the vertices and edges *read like a sentence*? (**Yes**)
  - Do I have different vertex or edge labels
    with the same properties? (**No**)

## Running basic and recursive traversals

> The Gremlin Server is *in-memory* only

* Traversing
  - Traversing is *a series of steps*
  - Traversing requires knowing *where we are*
  - Edge *direction matters*
  - Traversals *don't have history*

```js
g.V()
  .has('person', 'first_name', 'Ted')
  .out('friends')
  .values('first_name')
```

* `hasLabel(label)`
* `has(key, value)`
* `has(label, key, value)`
* `out(label)`
* `in(label)`
* `both(label)`
* `repeat(traversal)`
* `times(integer)`
* `until(traversal)`

> - **Remember**, an *outgoing vertex* is the vertex
>   where an *edge starts*,
>   and an *incoming vertex* is a vertex
>   where an *edge ends*.

> - Traversal parameters are similar to lambda expressions in Java.

```js
g.V()
  .has('person', 'first_name', 'Ted')
  .repeat(out('friends'))
  .times(2)
  .values('first_name')
```

* **Unbounded traversal**
  - Queries that use the `until()` step can create
    performance issues because the traversal runs
    until the condition is met.
  - If the condition is never met, then it continues
    until it exhausts every potential path in the graph.
  - This scenario is known as an *unbounded traversal*.

```js
g.V()
  .has('person', 'first_name', 'Ted')
  .until(has('person', 'first_name', 'Hank'))
  .repeat(out('friends'))
  .emit()
  .values('first_name')
```

* The `emit()` step is similar to the `until()` step,
  whether it's placed before or after the `repeat()` step,
  that impacts how it behaves.
  - If the `emit()` is placed before the `repeat()`,
    it includes the starting vertex.
  - If it's placed after the `repeat()`,
    it only emits the vertices traversed as part of the loop.

## Pathfinding traversals and mutating graphs

* Creating new vertex entities involves
  adding the appropriate elements and properties.
* However, creating new edges is a bit more complicated
  because we need to specify the vertex
  that belongs at each end of the edge.

```js
g.addV('person')
  .property('first_name', 'Dave')
```

* `addV(label)`
* `property(key, value)`

```js
g.addE('friends')
  .from(V().has('person', 'first_name', 'Ted'))
  .to(V().has('person', 'first_name', 'Hank'))
```

* `addE(label)`
* `from(vertex)`
* `to(vertex)`

* *We can remove an edge from a graph in one of two ways.*
  - First, if we delete the starting or ending vertex,
    any edge associated with that vertex is also deleted;
    it's the graph database version of referential integrity.
  - The second way to remove edges from a graph is to
    explicitly remove or drop these,
    leaving the start and end vertices.

* The `iterate()` step and the similar `next()` step
  both cause the traversal to execute.
* The key *difference* between these is that the `iterate()` step
  does not return a result, while the `next()` step
  returns the result of the traversal.

```js
dave = g
  .addV('person')
  .property('first_name', 'Dave')
  .next()
```

* `next()`: A terminal step that takes the iterable
  traversal source composed from the previous steps,
  iterates it once, and returns the first or
  next item in the iterable.

* Because *Gremlin* is **lazily evaluated**,
  we need to iterate our traversal in order to get a result.
* Otherwise, all we have is an iterable that contains
  the desired result but isn't of any use until it iterates.

### Paths

* `path()`: Using the `path()` step in Gremlin requires
  additional resource overhead on the server
  because each traverser needs to maintain the
  entire history of the steps it visits.

* Cycles in graphs

* *Simple path*
  - A *simple path* is a path that doesn't *repeat* any vertices,
    meaning that we only get results that are not cyclical.
  - `simplePath()`

```js
g.V()
  .has('person', 'first_name', 'Ted')
  .until(has('person', 'first_name', 'Denise'))
  .repeat(
    both('friends').simplePath()
  )
  .path()
```

```js
g.V().has('person', 'first_name', 'Dave')
  .bothE('works_with')
  .has('end_year', lte(2018))
  .otherV()
  .values('first_name')
```

* `inE(label)`
* `outE(label)`
* `bothE(label)`, *regardless of direction*

* Filtering with edge properties
  - time-based filters
  - weight-based filters

```js
g.V().has('person', 'first_name', 'Dave')
  .bothE('works_with')
  .has('end_year', lte(2018))
  .otherV()
  .values('first_name')
```

* Include edges in path results

```js
g.V().has('person', 'first_name', 'Ted')
  .until(has('person', 'first_name', 'Denise'))
  .repeat(
    bothE('works_with').otherV().simplePath()
  )
  .path()
```

## Formatting results

> In a graph database, only the values of the current
  vertices or edges are retrieved.

* In a graph database, the output of any step of a traversal
  is the *current set of vertices or edges*.

* Aliasing elements mid-traversal using `as()`

> The more *aliases* we create,
  the more the traverser has to keep track
  of with each additional step.

* Returning aliased elements

* `select(string[])`
* `by(key)`
* `by(traversal)`

* There are two forms of `by()`.
  - The first form takes the *property key* and returns
    the corresponding property value from the labeled element.
  - The second form takes a *traversal* that allows us to
    perform additional steps on the labeled element,
    such as a `valueMap()` or `out().valueMap('key')`.

```js
g.V().has('person', 'first_name', 'Dave')
  .out()
  .as('f')
  .out()
  .as('foff')
  .select('f', 'foff')
  .by('first_name')
  .by('first_name')
```

> - The first `by()` performs actions on the elements labeled as `'f'`;
> - the second `by()` performs actions on the elements labeled as `'foff'`.

* Projecting results instead of aliasing
  - **Selection** is the process of working with vertices,
    properties, or additional traversal expressions to return results
    from *previously* labeled steps.
  - **Selection** always looks **back** to earlier parts of the traversal.
  - **Projection** is the process of working with vertices,
    properties, or additional traversal expressions to create results
    from the input to the current step.
  - **Projection** always moves **forward**, taking the incoming
    data as the starting point.
  - **Selection** is generally used to combine results
    from elements traversed earlier in the traversal.
  - **Projection** is generally used to group or aggregate
    data starting from the current location in the graph.

* `project(string[])`

```js
g.V().hasLabel('person')
  .project('name', 'degree')
  .by('first_name')
  .by(bothE().count())
```

* **Selection** uses the `select()` step to
  create a result set based on previously
  traversed elements of a graph.
  - To use the `select()` step, we alias each of the
    elements with the `as()` step for later use.
* **Projection** uses the `project()` step to
  branch from the current location within
  the graph and creates new objects.
* In our present example, we had one element remain static,
  the person's name, but we needed the other elements
  to be calculated through further traversing of
  the graph to return the number of friends.

* **Ordering** results returned from a graph traversal
  - `order()`

```js
g.V().hasLabel('person')
  .values('first_name')
  .order()
  .by(decr)
```

* **Grouping** results returned from a graph traversal
  - `group()`
  - `groupCount()`
  - `unfold()`

```js
g.V().has('person', 'first_name', 'Dave')
  .both()
  .both()
  .group()
  .by('first_name')
  .unfold()
```

```js
g.V().has('person', 'first_name', 'Dave')
  .both()
  .both()
  .groupCount()
  .by('first_name')
  .unfold()
// Equals to
g.V().has('person', 'first_name', 'Dave')
  .both()
  .both()
  .group()
  .by('first_name')
  .by(count())
  .unfold()
```

* **Limiting** results
  - `limit(number)`
  - `tail(number)`
  - `range(startNumber, endNumber)`

```js
g.V().hasLabel('person')
  .values('first_name')
  .order()
  .by()
  .limit(3)
```

```js
g.V().has('person', 'first_name', 'Dave')
  .both()
  .both()
  .groupCount()
  .by('first_name')
  .unfold()
  .order()
  .by(values, desc)
  .by(keys)
  .project('name', 'count')
  .by(keys)
  .by(values)
  .limit(3)
```

## Advanced data modeling techniques

* `union(traversal, traversal, ...)`
  - Processes each traversal separately and
    outputs the combined results as a single result set.
  - A `union()` step is a branching step that requires
    that the current traverser be copied to each branch
    of the `union()` step in order to run.

* **Denormalizing** graph data
  - **precalculated** fields and **duplicated** data
  - **copying** data into multiple locations at write time
    to increase performance at read time
  - In a graph database, denormalization is all about
    *reducing the length of the traversal* required to
    get from our starting point to the ending data.

* **Precalculated fields** are properties of a vertex or edge
  that store the result of performing a calculation
  at write time to allow quick retrieval
  of the data at read time.

* **Copying properties** into more than one location
  in our graph allows us to optimize for multiple,
  different traversal paths at the expense
  of keeping data in sync.

> Unlike relational data models, both technical and
  non-technical users can understand graph data models.

## Working with subgraphs

* **vertex-induced** and **edge-induced**

```js
g.V().has('person', 'person_id', 2)
  .bothE('friends')
  .subgraph('sg')
  .cap('sg')
  .next()
```

* `subgraph(sideEffectKey)`
  - Defines an `edge-induced` subgraph within a larger set of graph data.
  - The `sideEffectKey` is a reference to the full results of the side effect.

* `cap(sideEffectKey)`
  - Iterates the traversal up to itself and emits the results
    of the side effect referenced by the `sideEffectKey`.

## Performance, pitfalls, and anti-patterns

* **Indexes**
  - Properties frequently used for filtering on values or ranges.
  - Properties requiring a full-text search.
  - Spatial features needing to be searched if
    the database supports geospatial data.

* **Supernodes**
  - Monitoring
  - Mitigating

### anti-patterns

* **Using graphs for non-graph use cases**

* Traversal anti-patterns
  - *Not using parameterized traversals*
  - *Using unlabeled filtering steps*

## Graph analytics, machine learning, and resources

* Pathfinding
  - Direction finding
  - Optimization problems
  - Fraud detection
