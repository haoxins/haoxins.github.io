---
title: 计算机体系结构 - 量化研究方法 - 第6版
description: 荷叶生时春恨生, 荷叶枯时秋恨成. 深知身在情长在, 怅望江头江水声.
date: 2022-10-27
---

- [计算机体系结构: 量化研究方法 (第6版)](https://book.douban.com/subject/36108789/)

> 没打算仔细看, 就是了解个大概~

- `MIPS` -> `RISC-V`

## 量化设计与分析基础

```
显然, 在这些技术的发展过程中, 带宽的改进速度超过延迟,
而且这一趋势很可能会持续下去. 一个简单的经验法则是:
带宽的增加速度至少是延迟改进速度的平方.
```

## 存储器层次结构设计

```
只从缓存中读取数据很容易, 因为缓存副本和存储器是相同的.
向缓存中写入数据难一些, 比如, 缓存副本和存储器怎样才能保持一致呢?

主要有两种策略. 一种是写直达 (又称"写穿透") 缓存, 当它更新缓存中的条目时,
会同时将数据写入主存储器中, 并对其进行更新.
另一种是写回 (又称"回写") 缓存, 仅更新缓存中的副本.
在要替换这个块时, 再将它复制回存储器.

这两种写入策略都可以使用写缓冲区, 这样将数据放入这个缓冲区之后,
马上就可以进行缓存操作, 而不需要等待将数据写入存储器.

衡量不同缓存组织方式的优劣的一个指标是缺失率.
缺失率是指那些未能找到预期目标的缓存访问所占的比例,
即未找到目标的访问数目除以总访问数目.
```

## 指令级并行及其开发

```
只要指令间存在名称依赖或数据依赖, 而且它们非常接近,
以至于执行期间的重叠能改变对应依赖中操作数的访问顺序,
就会存在冒险. 由于存在依赖, 所以必须保持程序顺序,
也就是按照原始源程序设定的顺序一次执行一个指令时,
指令的执行顺序.

软, 硬件技术的目的都是通过只在影响程序输出的地方保持程序顺序来利用并行性.
检测冒险和避免冒险可以确保不会打乱必要的程序顺序.

根据指令中读访问和写访问的顺序, 可以将数据冒险分为 3 类.
根据惯例, 一般按照流水线必须保持的程序顺序为这些冒险命名.

考虑两条指令 i 和 j, 根据程序顺序 i 排在 j 的前面.
可能的数据冒险如下所示.

RAW (read after write, 写后读)
j 试图在 i 写入一个源位置之前读取该源位置, 所以 j 会错误地获得旧值.
这一冒险是最常见的类型, 与真数据依赖相对应.
为了确保 j 会收到来自 i 的值, 必须保持程序顺序.

WAW (write after write, 写后写)
j 试图在 i 写一个操作数之前写该操作数.
这些写操作将以错误的顺序执行, 最后写入目标位置的是由 i 写入的值,
而不是由 j 写入的值. 这种冒险与输出依赖相对应.
只有在允许多个流水级进行写操作的流水线中,
或者在前一指令停顿时允许后一指令继续执行的流水线中,
才会发生 WAW 冒险.

WAR (write after read, 读后写)
j 尝试在 i 读取一个目标位置之前写入该位置, 所以 i 会错误地获取新值.
这一冒险源于反依赖 (或名称依赖). 对于大多数静态发射流水线
(即使是较深的流水线或者浮点流水线), 由于所有读操作都比所有写操作要早一些,
所以不会发生 WAR 冒险. 如果一些指令在指令流水线的早期写结果,
而其他指令在流水线的后期读取一个源位置, 或者如果对指令重新排序,
就会发生 WAR 冒险.

注意, RAR (read after read, 读后读) 情况不是冒险.
```

## 向量, SIMD 和 GPU 体系结构中的数据级并行

```
支持稀疏矩阵的主要机制是采用索引向量的 集中-分散 操作.
这种操作的目的是支持在稀疏矩阵的压缩表示 (即不包含零)
和正常表示 (即包含零) 之间进行转换. 集中操作取得索引向量,
并在此向量中提取元素, 元素位置等于基础地址加上索引向量中给定的偏移量.
其结果是向量寄存器中的一个密集向量.
在以密集形式对这些元素进行操作之后, 可以再使用同一索引向量,
通过分散存储操作, 以扩展方式存储该稀疏向量.
对此类操作的硬件支持称为 集中-分散, 几乎所有现代向量处理器都具备这一功能.
```

## 指令集基本原理

- `20` 世纪 `90` 年代, 指令集体系结构发生了以下变化.
  - __地址大小加倍__: 大多数桌面处理器与服务器处理器的
    `32` 位地址指令集被扩展到 `64` 位地址, 寄存器的宽度
    (及其他相关项目) 被扩展到 `64` 位.
  - __通过条件执行优化条件分支__: 条件分支可以限制优化得比较激进的计算机设计的性能.
    因此, 人们愿意将条件分支替换为操作的条件执行, 比如条件移动,
    大多数指令集中添加了这一指令.
  - __通过预取优化缓存性能__:
    由于一些计算机中发生缓存缺失时所消耗的指令时间与早期计算机上缺页错误所消耗的指令时间一样多,
    所以存储器层次结构在计算机性能中扮演着更为重要的角色. 因此添加了预取指令,
    以尝试通过预取来隐藏缓存缺失成本.
  - __支持多媒体__: 大多数桌面和嵌人式指令集进行了扩展, 为多媒体应用程序提供支持.
  - __浮点运算速度更快__: 为提高浮点性能所添加的操作,
    比如执行乘加和成对单次执行的操作, `RISC-V` 中包含了此类操作.

## 流水线: 基础与中级概念

```
简单流水线提取一条指令并发射它, 除非流水线中的已有指令和被提取的指令之间存在数据相关性,
并且不能通过旁路或前递来隐藏. 前递逻辑降低了实际流水线延迟, 使特定的相关性不会导致冒险.
如果存在不可避免的冒险, 则冒险检测硬件会使流水线停顿 (从使用该结构的指令开始).
在清除这种相关性之前, 不会提取或发射新指令. 为了弥补这些性能损失,
编译器可以尝试调度指令来避免冒险; 这种方法称为编译器调度或静态调度.
```
