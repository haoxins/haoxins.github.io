---
title: Modern network
description: 会挽雕弓如满月, 西北望, 射天狼
date: 2019-06-30
---

## HTTP/3 & QUIC

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

### IPv6

* ICMP
* ARP - IP -> MAC
* MTU
* netstat
* 以太网 (MAC)
* NAT & IPv6

```
Peer A -> OS Process A -> ip:port

Package = head:data
  head = mac:ip
    mac 一跳一跳又一跳, 一变一变又一变

Peer B -> OS Process B -> ip:port
```
