---
title: 阅读 经典书籍
description:
date: 2021-01-28
---

## 始于 2023

### 费曼物理学讲义

* [费曼物理学讲义: 新千年版](https://book.douban.com/subject/26662048/)

------------------

## 始于 2021

### TAOCP

* [Wiki - The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)

* [计算机程序设计艺术 MMIX增补](https://book.douban.com/subject/35170836/)
* [计算机程序设计艺术 卷4A](https://book.douban.com/subject/34452973/)
* [计算机程序设计艺术 卷3](https://book.douban.com/subject/26953756/)
* [计算机程序设计艺术 卷2](https://book.douban.com/subject/26850558/)
* [计算机程序设计艺术 卷1](https://book.douban.com/subject/26681685/)

### 哥德尔 艾舍尔 巴赫

* [哥德尔 艾舍尔 巴赫](https://book.douban.com/subject/1291204/)
  - 副标题: 集异璧之大成

### 计算机程序的构造和解释

* [计算机程序的构造和解释 (原书第2版)](https://book.douban.com/subject/34464721/)
  - https://book.douban.com/subject/1148282/

* 同样是拜读 **计算机程序设计艺术** 之前的准备书目 :)

* Lisp (Scheme)
  - 表达式
  - 命名和环境
  - 组合式求值
  - 复合过程
  - 过程应用的代换模型
  - 应用序和正则序
  - 条件表达式和谓词

```lisp
; Comments
(+ 123 456)
```

### 编程珠玑

* [编程珠玑 第2版 修订版](https://book.douban.com/subject/26302533/)
* [编程珠玑 续 修订版）](https://book.douban.com/subject/26302596/)

```
数年前, 买过一本, 应该是: 编程珠玑 (续), 没看多少, 丢了
此次再观之, 亲切了不少, 也算是个人成长的一种佐证吧 :)
```

* 也算作是拜读 **计算机程序设计艺术** 之前的准备书目吧 :)

### 程序员修炼之道

* [程序员修炼之道 (第2版)](https://book.douban.com/subject/35006892/)
  - 副标题: 通向务实的最高境界

* 软件的熵: 项目的心理性状态 **极其重要, 易被忽略, 隐蔽性强**

```
过度 完美主义 怎么办?
过于纠结 naming, format 之类的细节.
嗯?
保留一点 显而易见 & 无伤大雅 的 小破坏 :)
```

* **ETC**, **DRY**

* DRY
  - Code 的重复是最显而易见的
  - 数据结构, API, Data schema
  - 人 的重复 !!!
  - **开放** & **鼓励复用** 的氛围

* **正交性** & **可逆性**
  - 放弃追逐时尚
  - 不设最终决定

```
权衡的 度, 往往是折磨人的, 理想化 和 现实境况的 妥协, 又是必须的;
但妥协不是结束, 否则是永不处理的 TODO.

如果不是自己导致的 TODO, 谁会去孜孜以求?

价值感 来自于 何处?
```

* 防御式编程
  - 别忘了 `防御自己`
  - DBC 契约式设计
  - Clojure 前置条件 后置条件
  - Elixir Guard
  - 尽早崩溃, 死掉的程序 好过 瘫痪的程序
  - assert 不可能/不应该 发生的事情
  - assert 不要有副作用

```clojure
(defn accept-deposit [account-id amount]
  { :pre [ (> amount 0.00)
           (account-open? account-id) ]
    :post [ (contains? (account-transactions account-id) %) ] }
(create-transaction account-id :deposit amount))
```

```elixir
defmodule Deposits do
  def accept_deposit(account_id, amount) when (amount > 100000) do
  # ...
  end
  def accept_deposit(account_id, amount) when (amount > 1000) do
  # ...
  end
  def accept_deposit(account_id, amount) when (amount > 0) do
  # ...
  end
end
```
