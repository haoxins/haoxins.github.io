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

## Running basic and recursive traversals

## Pathfinding traversals and mutating graphs

## Formatting results

## Developing an application

## Advanced data modeling techniques

## Building traversals using known walks

## Working with subgraphs

## Performance, pitfalls, and anti-patterns

## Graph analytics, machine learning, and resources
