---
title: The learning roadmap about the backend
description: 持续更新
date: 2018-07-27
---

## Service design

- [The twelve-factor app - building software-as-a-service apps](https://12factor.net)
- [Concurrent Programming for Scalable Web Architectures](http://berb.github.io/diploma-thesis/community/index.html)
- [10 modern software engineering mistakes](https://medium.com/@rdsubhas/10-modern-software-engineering-mistakes-bc67fbef4fc8)
- [log: what every software engineer should know about real time datas unifying](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)

## Docker, Kubernetes, Service Mesh

* keywords: `Kubernetes`, `Istio`, `Docker`

> 毫不夸张, 未来 service 的唯一主流 runtime.

### 一些官方博客

* [envoy proxy](https://blog.envoyproxy.io)

### 一些资源

* [play with docker](https://training.play-with-docker.com)
* [kubernetes bootcamp](https://kubernetesbootcamp.github.io/kubernetes-bootcamp)
* [docker curriculum](https://docker-curriculum.com)
* [feiskyer / kubernetes handbook](https://github.com/feiskyer/kubernetes-handbook)
* [rootsongjc / kubernetes handbook](https://github.com/rootsongjc/kubernetes-handbook)
* [Understanding CNI - Container Networking Interface](http://www.dasblinkenlichten.com/understanding-cni-container-networking-interface)
* [kubernetes 101 networking](http://www.dasblinkenlichten.com/kubernetes-101-networking)

### 有趣的开源项目

* [knative/serving](https://github.com/knative/serving)

## Cloud Native

### 一些知名站点

* [Azure - Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns)
* [AWS - Cloud Design Patterns](http://en.clouddesignpattern.org/index.php/Main_Page)

### 有趣的开源项目

* [google/go-cloud](https://github.com/google/go-cloud)

## MicroServices

> 无法绕过的存在

### 一些知名站点

- [Microservice Architecture](http://microservices.io)
- [AWS microservices](https://aws.amazon.com/microservices)
- [Azure microservices](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices)

### 一些经典文章

- [microservice architecture best practices](https://codingsans.com/blog/microservice-architecture-best-practices)
- [A pattern language for microservices](http://microservices.io/patterns/index.html)

### 一些开源项目

- [Golang gokit](https://gokit.io)

## 网络

> 网络知识 == cloud APIs

* [Computer Network Tutorials](https://www.geeksforgeeks.org/computer-network-tutorials)
* [QUIC: A UDP-Based Multiplexed and Secure Transport](https://datatracker.ietf.org/doc/draft-ietf-quic-transport)
* [HPACK: Header Compression for HTTP/2](https://httpwg.org/specs/rfc7541.html)
* [7 Tips for Faster HTTP/2 Performance](https://www.nginx.com/blog/7-tips-for-faster-http2-performance)
* [http2 explained](https://daniel.haxx.se/http2)

## 数据库

* [MySQL索引背后的数据结构及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)
* [Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/mysql-migration)
* [Consistent Hashing in Cassandra](https://blog.imaginea.com/consistent-hashing-in-cassandra)
* [Graph Database](http://graphdatabases.com)
* [NoSQL Databases: a Survey and Decision Guidance](https://medium.baqend.com/nosql-databases-a-survey-and-decision-guidance-ea7823a822d)
* [Understanding When to use RabbitMQ or Apache Kafka](https://content.pivotal.io/blog/understanding-when-to-use-rabbitmq-or-apache-kafka)

## 分布式

* [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods)
* [system design primer](https://github.com/donnemartin/system-design-primer)
* [CAP Twelve Years Later: How the Rules Have Changed](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed)
* [Base: An Acid Alternative](https://queue.acm.org/detail.cfm?id=1394128)
* [Eventually Consistent](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
* [Distributed Systems for fun and profit](http://book.mixu.net/distsys/single-page.html)
* [Scalable Web Architecture and Distributed Systems](http://www.aosabook.org/en/distsys.html)
* [Neat Algorithms - Paxos](http://harry.me/blog/2014/12/27/neat-algorithms-paxos)
* [Raft 一致性算法论文译文](http://www.infoq.com/cn/articles/raft-paper)
* [Raft - The Secret Lives of Data](http://thesecretlivesofdata.com/raft)
* [Raft Consensus Algorithm](https://raft.github.io)
* [Raft Distributed Consensus Algorithm Visualization](http://kanaka.github.io/raft.js)
* [Gossip Visualization](https://rrmoelker.github.io/gossip-visualization)
* [Scaling Stateful Objects](http://ithare.com/scaling-stateful-objects)
* [How we built rate limiting capable of scaling to millions of domains](https://blog.cloudflare.com/counting-things-a-lot-of-different-things)

## async, non blocking

* [libuv - design overview](http://docs.libuv.org/en/v1.x/design.html)
* [The reactor pattern and non blocking IO](https://www.celum.com/en/blog/technology/the-reactor-pattern-and-non-blocking-io)

## 安全

* [A lesson in timing attacks](https://codahale.com/a-lesson-in-timing-attacks)
* [How to safely store a password](https://codahale.com/how-to-safely-store-a-password)
