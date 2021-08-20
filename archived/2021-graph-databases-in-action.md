---
title: (2021) Graph Databases in Action
description: 此时相望不相闻, 愿逐月华流照君. 鸿雁长飞光不度, 鱼龙潜跃水成文.
date: 2021-08-08
---

* [Graph Databases in Action](https://book.douban.com/subject/34700758/)

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

```zsh
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

```zsh
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
  *"entity first"* mindset
  (or perhaps more accurately, an *"entity-only"* mindset) to an
  ***"entity and relationship"*** mindset.

* ***Entity***,
  ***Relationship***,
  ***Attribute***,
  ***Access pattern***
  - We usually make our choice based on
    the predominant *access patterns*.

* Four-step process for data modeling
  - Understand the problem (core access patterns)
  - Create a whiteboard or conceptual model
  - Create a logical data model
  - Test the model

> we have found that singular names tend to be
> a better fit for graph data modeling.

* Because *relationships* are *first-class*
  citizens in a graph data model,
  both *vertices* and *edges* can have
  *properties* associated with those.

* **Naming**
  - We could have gone with the name *User*,
    but this is specific to one type of
    potential person within the application.
  - While we currently do not have this requirement,
    we might need to represent other types of people,
    such as *employees* or *owners*, in the future.

* ***lower_snake_case***, ***singular***

> It is generally a safe bet that each vertex
> in a graph database can only be associated
> with a single label.
> That is the approach of Apache *TinkerPop*.

* *uniqueness*
  - single uniqueness edge
  - multiple uniqueness edge

> ***Incorrect edge uniqueness*** is one of the most
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

```sql
g.V()
  .has('person', 'first_name', 'Ted')
  .out('friends')
  .values('first_name')
```

* **`has`**
  - `hasLabel(label)`
  - `has(key, value)`
  - `has(label, key, value)`
* `out(label)`, `in(label)`
* `both(label)`

> **Remember**, an *outgoing vertex* is the vertex
> where an *edge starts*,
> and an *incoming vertex* is a vertex
> where an *edge ends*.

## Pathfinding traversals and mutating graphs

## Formatting results

## Developing an application

## Advanced data modeling techniques

## Building traversals using known walks

## Working with subgraphs

## Performance, pitfalls, and anti-patterns

## Graph analytics, machine learning, and resources
