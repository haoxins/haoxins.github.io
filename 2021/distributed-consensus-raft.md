---
title: Raft
description: Consensus, Bridging Theory and Practice
date: 2021-09-20
---

* https://github.com/tikv/raft-rs

* https://raft.github.io/raft.pdf

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

* *Election Safety*: At most one leader can
  be elected in a given term.
* *Leader Append-Only*: A leader never
  overwrites or deletes entries in its log;
  it only appends new entries.
* *Log Matching*: If two logs contain an
  entry with the same index and term, then
  the logs are identical in all entries
  up through the given index.
* *Leader Completeness*: If a log entry is
  committed in a given term, then that entry
  will be present in the logs of the leaders
  for all higher-numbered terms.
* *State Machine Safety*: If a server has
  applied a log entry at a given index to
  its state machine, no other server will
  ever apply a different log entry
  for the same index.

### Raft basics

* At any given time each server is in one of three states:
  - leader,
  - follower,
  - or candidate.

* Raft ensures that there is at most
  one leader in a given term.

* **Followers** only respond to requests from other servers.
  If a follower receives no communication, it becomes a
  **candidate** and initiates an election. A **candidate**
  that receives votes from a majority of the full cluster
  becomes the new **leader**.
  - Leaders typically operate until they fail.
* Time is divided into **terms**, and each term begins with
  an **election**. After a successful election, a single
  leader manages the cluster until the end of the term.
* Some elections fail, in which case the term ends without
  choosing a leader. The transitions between terms may be
  observed at different times on different servers.

---

* **Terms** act as a *logical clock* in Raft, and they allow
  servers to detect obsolete information such as
  stale leaders.
* Each server stores a *current term number*, which
  increases monotonically over time.
* If a candidate or leader discovers that its term is
  *out of date*, it immediately **reverts** to follower state.
* If a server receives a request with a *stale term number*,
  it **rejects** the request.
* The basic consensus algorithm requires **only two** types
  of RPCs between servers.
  - `RequestVote` RPCs are initiated by *candidates* during
    elections,
  - and `AppendEntries` RPCs are initiated by *leaders* to
    replicate log entries and to provide a form of heartbeat.

### Leader election

* If a follower receives no communication over a period of
  time called the *election timeout*, then it assumes there
  is no viable leader and begins an
  election to choose a new leader.
* A candidate continues in this state until one of
  three things happens:
  - (a) it wins the election,
  - (b) another server establishes itself as leader, or
  - (c) another election timeout goes by with no winner.
* While waiting for votes, a *candidate* may receive an
  `AppendEntries` RPC from another server claiming to
  be leader.
  - If the leader's term (included in its RPC) is at
    least as large as the candidate's current term,
    then the candidate recognizes the leader as
    legitimate and returns to follower state.
  - If the term in the RPC is smaller than the
    candidate's current term, then the candidate
    *rejects* the RPC and continues
    in candidate state.
* Raft uses *randomized election timeouts* to ensure
  that split votes are rare and that they are
  resolved quickly. To prevent split votes in the
  first place, election timeouts are chosen randomly
  from a fixed interval (e.g., `150-300 ms`).
* The same mechanism is used to handle split votes.
  Each candidate restarts its randomized election
  timeout at the start of an election, and it waits
  for that timeout to elapse before starting the next
  election; this reduces the likelihood of another
  split vote in the new election.

### Log replication

* *Logs* are composed of *entries*, which are
  *numbered sequentially*. Each entry contains the
  `term` in which it was created
  (the number in each box) and a command for the
  state machine. An entry is considered committed
  if it is safe for that entry to be
  applied to state machines.
* The leader decides when it is safe to apply a
  log entry to the state machines; such an entry
  is called **committed**. Raft guarantees that
  committed entries are durable and will eventually
  be executed by all of the available state machines.
* A log entry is committed once the leader that
  created the entry has replicated it on a majority
  of the servers. This also commits all preceding
  entries in the leader's log, including entries
  created by previous leaders.
* Raft maintains the following properties, which
  together constitute the *Log Matching Property*:
  - If two entries in different logs have the
    *same index and term*, then they store
    the **same command**.
  - If two entries in different logs have the
    *same index and term*, then the logs are
    **identical in all** preceding entries.

* During normal operation, the logs of the leader
  and followers stay consistent, so the
  `AppendEntries` consistency check never fails.
* However, leader crashes can leave the logs
  inconsistent.
  - the old leader may not have fully replicated
    all of the entries in its log.
* In Raft, the leader handles inconsistencies by
  forcing the followers' logs to duplicate its own.
* This means that conflicting entries in follower
  logs will be overwritten with entries from
  the leader's log.

## Cluster membership changes

* RPCs used to change cluster membership.
  - The `AddServer` RPC is used to add a new server
    to the current configuration, and
  - the `RemoveServer` RPC is used to remove a server
    from the current configuration.

## Log compaction

* Snapshotting `memory-based` state machines
* Snapshotting `disk-based` state machines
* Incremental cleaning approaches
* Alternative: `leader-based` approaches
