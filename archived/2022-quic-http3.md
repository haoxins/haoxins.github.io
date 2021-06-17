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

# Timeline

## 2021

* [RFC 9000 - IETF](https://datatracker.ietf.org/doc/html/rfc9000)
  - [RFC 9000 - RFC Editor](https://www.rfc-editor.org/rfc/rfc9000)
  - **QUIC**: A UDP-Based Multiplexed and Secure Transport
  - **May 2021**
  - 目测, **HTTP/3** 也快了

* [WebRTC is now a W3C and IETF standard](https://web.dev/webrtc-standard-announcement/)

* 未来, **UDP** 比 **TCP** 发挥更大价值
  - 过去, **TCP** 比 **UDP** 发挥更大价值

* [IETF Last Call - (QUIC) to Proposed Standard](https://mailarchive.ietf.org/arch/msg/quic/ye1LeRl7oEz898RxjE6D3koWhn0/)
