---
title: (2022) QUIC & HTTP/3
description: 会挽雕弓如满月, 西北望, 射天狼
date: 2019-06-30
---

* [RFC 9000 - QUIC](https://www.rfc-editor.org/rfc/rfc9000)
* [RFC xxxx - HTTP/3]()

### Overview

* Connection Id
* Independent streams

* QPACK
* Connection -> Secure Connection -> Streams
* Stream
  - Flow control
  - Back pressure

* Frame
  - Headers frame
  - Data frame

* [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol)

* [gRPC over HTTP2](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md)
  - [ ] TODO: HTTP3

### QUIC-LB: Generating Routable QUIC Connection IDs

* [QUIC-LB: Generating Routable QUIC Connection IDs](https://quicwg.org/load-balancers/draft-ietf-quic-load-balancers.html)

### Applicability of the QUIC Transport Protocol

* [Applicability of the QUIC Transport Protocol](https://quicwg.org/ops-drafts/draft-ietf-quic-applicability.html)

### Problem Details for HTTP APIs

* [RFC 7807: Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)

------------------

# 网络基础

## Layers

### 应用层

* DNS, HTTP, QUIC?

### 传输层

* UDP

```
UDP Header

| Source port | Destination port | Length | Checksum |
```

### 网络层/路由层

* ping: ICMP

* IP, IPSec, GRE

```
Handle IP

| IP header | TCP header | data ... |
```

* 网关: 路由器
  - 转发网关: 不改变 IP
  - NAT: 改变 IP
  - MAC 地址过网关 (换局域网) 则变

```
每到一个新的局域网, 包的 MAC 地址都是要变的, 但是 IP 地址都不变.
在 IP 头里面, 不会保存任何网关的 IP 地址.
所谓的下一跳是某个 IP 地址,
意思是要将这个 IP 地址转换为 MAC 地址放入 MAC 头中.
```

* 路由器
  - 多张网卡
  - 路由表

```
ip rule add from 192.168.1.0/24 table 10
ip rule add from 192.168.2.0/24 table 20
```

* 动态路由协议
  - OSPF
  - BGP


------------------

# Events

------------------

## 2021

* [RFC 9000 - IETF](https://datatracker.ietf.org/doc/html/rfc9000)
  - [RFC 9000 - RFC Editor](https://www.rfc-editor.org/rfc/rfc9000)
  - **QUIC**: A UDP-Based Multiplexed and Secure Transport
  - **May 2021**
  - 目测, **HTTP/3** 也快了

* 截至2021年4月

```
中国 IPv6 活跃用户数已达 5.15 亿,占网民总数的 52.1%.

全球的 IPv4 地址早在 2019 年底就分配完了,
大部分被美国占据,
而在 IPv6 地址分配上,
中美一直竞争激烈, 目前我国暂居第一.
```

* [WebRTC is now a W3C and IETF standard](https://web.dev/webrtc-standard-announcement/)

* 未来, **UDP** 比 **TCP** 发挥更大价值
  - 过去, **TCP** 比 **UDP** 发挥更大价值

* [IETF Last Call - (QUIC) to Proposed Standard](https://mailarchive.ietf.org/arch/msg/quic/ye1LeRl7oEz898RxjE6D3koWhn0/)
