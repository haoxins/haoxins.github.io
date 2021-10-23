---
title: Raft
description: Consensus, Bridging Theory and Practice
date: 2021-09-20
---

* [Consensus: Bridging Theory and Practice](https://github.com/ongardie/dissertation)
  - https://raft.github.io

## Motivation

* *Replicated state machines* are typically implemented using
  a replicated log. Each server stores a log containing a
  series of commands, which its state machine executes in order.
* Each log contains the same commands in the same order,
  so each state machine processes the same sequence of commands.
  Since the state machines are deterministic, each computes the
  same state and the same sequence of outputs.
* Keeping the replicated log consistent is the job
  of the consensus algorithm.

* Consensus algorithms for practical systems
  typically have the following properties:
  - They ensure safety (never returning an incorrect result)
    under all non-Byzantine conditions, including network
    delays, partitions, and packet loss,
    duplication, and reordering.
  - They are fully functional (available) as long as
    any majority of the servers are operational and can
    communicate with each other and with clients. Thus,
    a typical cluster of **five** servers can tolerate
    the failure of any **two** servers.
  - They do not depend on timing to ensure the consistency
    of the logs: faulty clocks and extreme message delays
    can, at worst, cause availability problems.
    That is, they maintain safety under an asynchronous
    model, in which messages and processors proceed at
    arbitrary speeds.
  - In the common case, a command can complete as soon
    as a majority of the cluster has responded to a
    single round of remote procedure calls; a minority
    of slow servers need not impact
    overall system performance.

## Basic Raft algorithm

* But our most important goal and most
  difficult challenge was **understandability**.

* **Leader election**: a new leader must be chosen
  when starting the cluster and when
  an existing leader fails.
* **Log replication**: the leader must accept log
  entries from clients and replicate them across
  the cluster, forcing the other logs
  to agree with its own.
* **Safety**: the key safety property for Raft is
  the *State Machine Safety Property*: if any server
  has applied a particular log entry to its
  state machine, then no other server may apply a
  different command for the same log index.

## Cluster membership changes

## Log compaction

## Client interaction

## Raft user study

## Correctness

## Leader election evaluation

## Implementation and performance

## Related work

## Conclusion

## Safety proof and formal specification
