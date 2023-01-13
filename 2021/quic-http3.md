---
title: QUIC & HTTP/3
description: 会挽雕弓如满月, 西北望, 射天狼
date: 2019-06-30
---

* [RFC 9000 - QUIC](https://www.rfc-editor.org/rfc/rfc9000)
* [RFC 9114 - HTTP3](https://www.rfc-editor.org/rfc/rfc9114)

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

* [G2: gRPC over HTTP/3](https://github.com/grpc/proposal/blob/master/G2-http3-protocol.md)

* [QUIC-LB: Generating Routable QUIC Connection IDs](https://quicwg.org/load-balancers/draft-ietf-quic-load-balancers.html)

* [Applicability of the QUIC Transport Protocol](https://quicwg.org/ops-drafts/draft-ietf-quic-applicability.html)

* [RFC 7807: Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)

* [RFC 6749: The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)

------------------

# 网络基础

* [Variable Length Subnet Table For IPv4](https://datatracker.ietf.org/doc/html/rfc1878)

## Apps

* iptables

```
Private IP -> SNAT -> Public IP

Netfilter, conntrack
```

* SNAT (源地址转换)

```zsh
iptables -t nat -A -s 私网IP地址 \
  -j Snat --to-source 外网IP地址
```

* DNAT (目标地址转换)

```zsh
iptables -t nat -A -PREROUTING \
  -d 外网IP地址 -j Dnat \
  --to-destination 私网IP地址
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

* 每到一个新的局域网, 包的 `MAC` 地址都是要变的,
  但是 `IP` 地址都不变. 在 `IP` 头里面,
  不会保存任何网关的 `IP` 地址.
* 所谓的`下一跳`是某个 `IP` 地址,
  意思是要将这个 `IP` 地址转换为
  `MAC` 地址放入 `MAC` 头中.

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

| 目标 Mac 地址 | 源 Mac 地址 | Type (2 byte) |
  Data (46 - 1500 byte) | CRC (4 byte) |
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

## HTTP/3 explained

* [HTTP/3 explained](https://github.com/bagder/http3-explained)
  - A document describing the HTTP/3 and QUIC protocols
  - 一般, 可以随便看看

### TCP head of line blocking

* With `HTTP/2`, typical **browsers** do tens or hundreds
  of parallel transfers over a single TCP connection.
* If a single packet is dropped, or lost in the network
  somewhere between two endpoints that speak `HTTP/2`,
  it means the entire TCP connection is brought to a halt
  while the lost packet is re-transmitted and
  finds its way to the destination.
* As the packet loss rate increases, `HTTP/2` performs
  less and less well. At `2%` packet loss,
  tests have proven that `HTTP/1` users are usually better off
  - because they typically have up to six TCP connections to
    distribute lost packets over.
  - This means for every lost packet the other
    connections can still continue.

* HTTP-over-QUIC (`HTTP/3`) builds upon `HTTP/2` and follows
  many of the same concepts but moves some of the specifics
  from the HTTP layer as they are covered by QUIC.

* A QUIC **connection** is made to a UDP port and IP address,
  but once established the connection is
  associated by its `"connection ID"`.
* Over an established connection, either side can create
  streams and send data to the other end.
* Streams are delivered in-order and they are reliable,
  but different streams may be delivered out-of-order.
* QUIC offers flow control on both connection and streams.
* QUIC guarantees in-order delivery of streams,
  but not between streams.
  - This means that each stream will send data and
    maintain data order, but each stream may reach
    the destination in a different order
    than the application sent it!
  - In QUIC, a lost packet only affects the stream
    to which the lost packet belongs.

### Connections

* QUIC's connection establishment combines
  version negotiation with the cryptographic and
  transport handshakes to reduce
  connection establishment latency.
  - To actually send data over such a connection,
    one or more streams have to be created and used.
* Each connection possesses a set of connection identifiers,
  or connection IDs, each of which can be used to
  identify the connection.
  - Connection IDs are independently selected by endpoints;
    each endpoint selects the connection IDs that its peer uses.
* By taking advantage of the connection ID, connections can
  thus migrate between IP addresses and network interfaces
  in ways TCP never could.
* There is no way to opt-out or avoid using
  TLS for a QUIC connection.

### Streams

* Streams are individually flow controlled,
  allowing an endpoint to limit memory commitment
  and to apply back pressure.
* The creation of streams is also flow controlled,
  with each peer declaring the maximum stream ID
  it is willing to accept at a given time.

* Streams are identified by an unsigned `62-bit` integer,
  referred to as the Stream ID.
* The least significant **two bits** of the Stream ID are
  used to identify the type of stream
  (unidirectional or bidirectional) and
  the initiator of the stream.
* The **least** significant bit (`0x1`) of the Stream ID
  identifies the initiator of the stream.
  - Clients initiate even-numbered streams
    (those with the least significant bit set to `0`);
  - servers initiate odd-numbered streams
    (with the bit set to `1`).
* The **second least** significant bit (`0x2`) of the Stream ID
  differentiates between unidirectional streams and bidirectional streams.
  - Unidirectional streams always have this bit set to `1`
  - and bidirectional streams have this bit set to `0`.

* Streams are an ordered byte-stream abstraction.
  - Separate streams are however not necessarily
    delivered in the original order.

* QUIC itself does not provide frames for exchanging
  prioritization information. Instead it relies on
  receiving priority information from
  the application that uses QUIC.

### HTTP/3

* An HTTP server includes an `Alt-Svc:` header in its response:

```
Alt-Svc: h3=":50781"
```

* The client sends its HTTP request on a
  client-initiated bidirectional QUIC stream.
* A request consists of a single `HEADERS` frame and
  might optionally be followed by one or two other frames:
  - a series of `DATA` frames and possibly
    a final `HEADERS` frame for trailers.
* The server sends back its HTTP response
  on the bidirectional stream.
  - A `HEADERS` frame, a series of `DATA` frames and
    possibly a trailing `HEADERS` frame.

* **QPACK** headers
  - QPACK itself uses two additional unidirectional
    QUIC streams between the two end-points.
  - They are used to carry dynamic table
    information in either direction.

* **Server pushes** are only allowed to happen if the
  client side has agreed to them.
  - In `HTTP/3` the client even sets a limit for
    how many pushes it accepts by informing the server
    what the max push stream ID is.

------------------

# Events

------------------

## 2021

* [Quinn - 0.8.0](https://github.com/quinn-rs/quinn/releases/tag/0.8.0)
  - **Quinn** is a *pure-rust*, *async-compatible*
    implementation of the IETF QUIC transport protocol.
  - **期待**: `v1.0`

* [Braid: Synchronization for HTTP](https://braid.org)
  - The *Braid Protocol* is an extension to HTTP that
    generalizes it from a *state transfer*
    to a *state synchronization* protocol.
  - **十分有趣**

* **Braid** adds these features to HTTP:
  - `Versioning` to HTTP resources
  - `Subscriptions` to GET requests
  - `Patches` to Range Requests
  - `Merge-Types` to specify **OT**
    or **CRDT** behavior

* [Envoy: HTTP3 overview (v1.20)](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http3)
  - `HTTP/3` support is still in *Alpha*

* [RFC 9000 - IETF](https://datatracker.ietf.org/doc/html/rfc9000)
  - [RFC 9000 - RFC Editor](https://www.rfc-editor.org/rfc/rfc9000)
  - **QUIC**: A UDP-Based Multiplexed and Secure Transport
  - **May 2021**
  - 目测, **HTTP/3** 也快了

* 截至2021年4月

```
中国 IPv6 活跃用户数已达 5.15 亿, 占网民总数的 52.1%.

全球的 IPv4 地址早在 2019 年底就分配完了,
大部分被美国占据,
而在 IPv6 地址分配上,
中美一直竞争激烈, 目前我国暂居第一.
```

* [WebRTC is now a W3C and IETF standard](https://web.dev/webrtc-standard-announcement/)

* 未来, **UDP** 比 **TCP** 发挥更大价值
  - 过去, **TCP** 比 **UDP** 发挥更大价值

* [IETF Last Call - (QUIC) to Proposed Standard](https://mailarchive.ietf.org/arch/msg/quic/ye1LeRl7oEz898RxjE6D3koWhn0/)
