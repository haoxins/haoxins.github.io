---
title: Network notes
description: We can do something
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

### IP

* ICMP
* ARP - IP -> MAC
* MTU
* netstat
* 以太网 (MAC)

```
Peer A -> OS Process A -> ip:port

Package = head:data
  head = mac:ip
    mac 一跳一跳又一跳, 一变一变又一变

Peer B -> OS Process B -> ip:port
```
