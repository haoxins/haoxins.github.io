---
title: Linux
description: 万言已默馀心知, 一杯浊酒尽欢意, 秋风万里一明月, 屈指西风寄归期
date: 2021-02-17
---

* [Makefile](https://makefiletutorial.com)
  - Learn Makefile with the tastiest examples

### Observability

* `uptime`
  - `cat /proc/loadavg`
* `sudo dmesg --human | less`
  - Think of it as kernel and driver logs.
* `df -h`
  - capacity
* `iostat -x`
  - throughput
  - `sudo apt-get install sysstat`
* `sudo biotop-bpfcc`
  - `sudo apt-get install bpfcc-tools linux-headers-$(uname -r)`
  - https://github.com/iovisor/bcc
* `sar -n DEV 1 1`
* `sar -n EDEV 1 1`
* `sar -n TCP,ETCP 1 1`
  - `/etc/default/sysstat`, `ENABLED="true"`
  - `sudo service sysstat restart`
* `sudo tcptop-bpfcc 1 1`
* `free -h`
  - `df` for RAM
  - https://www.linuxatemyram.com
  - If the `available` column is showing a
    reasonable amount left, you're all right.
* `top`
  - `?`
* `vmstat -s`
* `sudo oomkill-bpfcc`
* `mpstat -P ALL 1`
  - `cat /proc/cpuinfo`
* `sudo opensnoop-bpfcc`
* `sudo execsnoop-bpfcc`

### Memory

* The **OOM Killer** is one of the more interesting (and controversial)
  memory management features in the Linux kernel.
  - Under low-memory conditions, the **OOM Killer** kicks in and
    tries to figure out which processes to kill in order to
    reclaim some memory and for the system to regain some stability.
  - It uses heuristics (including niceness, how recent the process is
    and how much memory it uses) to score each process
    and pick the unlucky winner.
  - The **OOM Killer** behavior can be tweaked
    via flags exposed by the kernel.

### Others

* [Users and groups](https://wiki.archlinux.org/title/users_and_groups)

* [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)

```zsh
# -S, --show-error
#   Show error even when -s is used
# -v, --verbose
#   Make the operation more talkative
# -k, --insecure
#   Allow insecure server connections when using SSL

curl https://dashboard.awx.im \
  --resolve dashboard.awx.im:443:127.0.0.1

curl -H "Host: dashboard.awx.im" \
  https://localhost:8443
```

```zsh
nc -zv -w 3 dashboard.awx.im 443

netstat -tulpn | grep LISTEN

dig +short dashboard.awx.im
```

------------------

# Events

------------------

## 2022

* Ubuntu `22.04` LTS (Jammy Jellyfish)
  - `GCC` was updated to the `11.2.0` release
  - `Python` now ships at version `3.10.4`
  - `LLVM` now defaults to version `14`
  - `Golang` defaults to version `1.18`
  - `rustc` defaults to version `1.58`
  - `containerd` was updated to version `1.5.9`
  - `runc` was updated to version `1.1.0`

* 2022-01-27
  - 由于 `License` 的原因, 卸载了 **Docker Desktop**, 一个短暂的技术时代结束了.
  - 因 `Docker` 起, 由 `Kubernetes` 发展壮大, `Docker` 卒.

* Linux `5.17` kernel is introducing mainline support for
  the StarFive JH7100, which has been trying to make its
  debut as the first usable and low-cost **RISC-V** platform.

## 2021

* Linux kernel **5.15**
  - **ntfs3**: new `NTFS` driver for `5.15`

| Version |  Released  | Projected EOL |
| ------- |:----------:|:-------------:|
|  5.15   | 2021-10-31 |   Oct, 2023   |

* [Debian 11 **bullseye** released](https://www.debian.org/News/2021/20210814)
  - **bullseye**
  - *August 14th, 2021*
  - Linux kernel `5.10` series
  - Python 3, `3.9.1`
  - Rustc `1.48`

* [Debian 11](https://www.debian.org/releases/bullseye/releasenotes)

* [Facebook, Google, Isovalent, Microsoft, and Netflix announce eBPF Foundation](https://isovalent.com/blog/post/2021-08-ebpf-foundation-announcement)

```
Think of eBPF as making the operating system programmable
in the same way as JavaScript and other languages
have done this to the web browser.
We are therefore looking into an exciting future of innovation ahead of us.
```

* [eBPF](https://ebpf.io)
  - [eBPF Summit 2021](https://ebpf.io/summit-2021/)

* RFC: Add the stateless AV1 uAPI and the VIVPU virtual driver to showcase it.

* [Supporting Linux kernel development in Rust](https://lwn.net/Articles/829858/)
  - https://github.com/Rust-for-Linux/linux

* 2021-06-27
  - Linux **5.13**
  - By: Linus Torvalds

* 2021-06-19
  - Debian 10: **10.10** released

* Long-term release kernels

| Version |  Released  | Projected EOL |
| ------- |:----------:|:-------------:|
|  4.19   | 2018-10-22 |   Dec, 2024   |

* Ubuntu **21.04**
  - 集成用于 **Flutter** 应用开发的 SDK
  - 默认启用 **Wayland** 替换了 X Window System
