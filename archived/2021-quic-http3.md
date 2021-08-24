---
title: QUIC & HTTP/3
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

## Apps

* iptables

```
Private IP -> SNAT -> Public IP

Netfilter, conntrack

SNAT (源地址转换)

iptables -t nat -A -s 私网IP地址 -j Snat --to-source 外网IP地址

DNAT (目标地址转换)

iptables -t nat -A -PREROUTING -d 外网IP地址 -j Dnat --to-destination 私网IP地址
```

* IPsec VPN

```
| 外层IP头 | IPsec 头 | 内层 IP 包 |
| 承载协议 | 隧道协议  | 乘客协议    |
```

* MPLS VPN

* GRE
  - IP-over-IP
  - 点对点隧道技术

* VXLAN

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
* NDP: 基于 ICMPv6

* IP

```
Handle IP

| IP header | UDP header | data ... |
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

### 链路层 (Mac 层)

* ARP
  - 广播, 由 IP 得 Mac

```
Handle Mac

| Mac header | IP header | UDP header | data ... |

| 目标 Mac 地址 | 源 Mac 地址 | Type (2 byte) | Data (46 - 1500 byte) | CRC (4 byte) |
```

* 局域网
  - Hub: 广播
  - Switch: Mac 学习能力

* VLAN

```
| 目标 Mac 地址 | 源 Mac 地址 | 802.1Q | Type (2 byte) | ...

802.1Q

Tag protocol identifier (TPID)
Tag control information (TCI)
  Priority code point (PCP)
  Drop eligible indicator (DEI)
  VLAN identifier (VID)

| TPID |       TCI       |
| TPID | PCP | DEI | VID |
```

### 物理层

------------------

# Events

------------------

## 2021

* [Braid: Synchronization for HTTP](https://braid.org)
  - The *Braid Protocol* is an extension to HTTP that
    generalizes it from a *state transfer*
    to a *state synchronization* protocol.

* ***Braid*** adds these features to HTTP:
  1. *Versioning* to HTTP resources
  2. *Subscriptions* to GET requests
  3. *Patches* to Range Requests
  4. *Merge-Types* to specify **OT** or **CRDT** behavior

* [Envoy: HTTP3 overview (v1.20)](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http3)
  - `HTTP/3` support is still in *Alpha*

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
