---
title: (2021) 阅读 经典书籍
description: ~
date: 2021-01-28
---

# 始于 2021

------------------

## 复分析: 可视化方法

* [复分析: 可视化方法](https://book.douban.com/subject/35316347/)
  - 译者: 齐民友
  - 出版年: 2021-01

```
假想有一个社会, 在那里, 鼓励到了一定年龄的公民去读乐谱, 这一切都是令人尊敬的.
然而这个社会有一个非常奇怪且令人苦恼的法律,
也几乎没有人记得这个法律是怎么来的,
即: 禁止听音乐和演奏音乐!

在这个社会里, 虽然音乐的重要性是被广泛承认的, 但是由于某些原因,
音乐并没有被广泛地欣赏.

这个寓言里, 立法禁止学音乐的学生直接从 "声音的直觉"
去体验与理解音乐, 这明显是不公正不合理的.
但是在我们的数学家社会里就有这样的法律.
一条不成文的法律.
那就是: 禁止数学成为可视的!

这反映了一个事实:
近几百年来形象思维在数学中的名声被玷污了.
虽然伟大的数学家们从来也不在意这种风尚,
然而 "街头巷尾的数学家们" 直到前不久才接受了几何的挑战.

这本书将用一种新的, 可以看得见的, 可视化的论证方式
解释初等复分析的真理, 公开地向当前占统治地位的 纯符号逻辑推理 叫板!
```

* 这本书比较特殊, 因为 `大部分看不懂` :)
  - 所以阅读方式比较另类
  - 就是反复的粗略的看
  - 建立一个 **概览性的** 认知
  - 至于能不能某一天 能有全面深入的理解, 就: **一切随缘了**

> 本书不做笔记, 不做点评. 以免 **贻笑大方**

------------------

## 计算机程序的构造和解释

* [计算机程序的构造和解释 (原书第2版)](https://book.douban.com/subject/34464721/)
  - https://book.douban.com/subject/1148282/

* 同样是拜读 **计算机程序设计艺术** 之前的准备书目 :)

### 过程 抽象

* Lisp (Scheme)
  - 表达式
  - 命名和环境
  - 组合式求值
  - 复合过程
  - 过程应用的代换模型
  - 应用序和正则序
  - 条件表达式和谓词

```scheme
; Comments
(+ 123 456)
```

* Lisp 可以将 `过程` 作为 `数据` 进行处理
  - 基本表达
  - 组合
  - 抽象

* 表达式
  - 组合式 `(+ 2.7 10)` -> `12.7`
  - 复合过程

```scheme
(define (square x)
  (* x x)
)
```

  - 条件表达式 (`谓词: >, =, <, and, or, not`)

```scheme
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))
  )
)

(define (abs x)
  (cond ((< x 0) (- x))
        (else x)
  )
)
```

```scheme
; 定义一个 谓词
(define (>= x y)
  (not (< x y))
)
```

* 应用序(求值) vs 正则序(求值)

* 词法作用域

```scheme
(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001)
  )
  (define (improve guess)
    (average guess (/ x guess))
  )
  (define (average a b)
    (/ (+ a b) 2)
  )
  (define (sqrt-iter guess)
    (if (good-enough? guess)
      guess
      (sqrt-iter (improve guess))
    )
  )
  (sqrt-iter 1.0)
)

(display (sqrt 36.0))
; 6.000000005333189
```

* 高阶过程 & Lambda

```scheme
(define (deriv g)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x)) dx)
  )
)

(define dx 0.00001)

(define (cube x)
  (* x x x)
)

(display ((deriv cube) 4))
; 48.00011999748221
```

### 数据 抽象

```scheme
(define x (cons 1 2))
(define y (cons 3 4))
(define z (cons x y))

(car (car z))
; 1
(car (cdr z))
; 3

; cons construct
; car, cdr 的命名是历史原因
; IBM 704 的寄存器取址模式相关
```

* 层次性数据 & 闭包

```scheme
(define x (cons (list 1 2) (list 3 4)))

(length x)
; 3

(list x x)
; (((1 2) 3 4) ((1 2) 3 4))

(length (list x x))
; 2
```

* 这一章节看着比较熟悉, 回忆起了当年阅读 @`Elixir 程序设计` 的时候
* 递归, map, filter, reduce

```
递归 数学归纳法

朴实无华的思想
当一次性看见多个应用案例的时候
依旧忍不住赞叹
那种 one for all 的美感!

大道! 至简! 妙哉! 美哉!
```

```scheme
(map square (list 1 2 3 4))
; (1 4 9 16)
```

* 符号数据

```scheme
(define a 1)
(define b 2)
(list a b)
; (1 2)
(list 'a b)
; (a 2)
```

```scheme
(define (memq item x)
  (cond ((null? x) false)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))
  )
)
(memq 'apple '(pear banana prune))
; #f
(memq 'apple '(x (apple sauce) y apple pear))
; (apple pear)
```

- 符号求导数对于 Lisp 有着特殊的历史意义
- Lisp 不愧是为了表达数学推导过程而诞生的语言, 可把玩, 但 (编码效率极低)
- BTW, 这或许也就是为啥, 本书中大量数学处理的案例的原因吧

* Huffman (手工摘抄, 错误难免)

```scheme
(define (make-leaf symbol weight)
  (list 'leaf symbol weight)
)
(define (leaf? object)
  (eq? (car object) 'leaf)
)
(define (symbol-leaf x)
  (cadr x)
)
(define (weight-leaf x)
  (caddr x)
)
(define (make-code-tree left right)
  (list left
        right
        (append (symboles left) (symboles right))
        (+ (weight left) (weight right)))
)

(define (left-branch tree) (car tree))
(define (right-branch tree) (cadr tree))
(define (symboles tree)
  (if (leaf? tree)
      (list (symbol-leaf tree))
      (caddr tree)
  )
)
(define (weight tree)
  (if (leaf? tree)
      (weight-leaf tree)
      (cadddr tree)
  )
)
```

```scheme
(define (decode bits tree)
  (define (decode-1 bits current-branch)
    (if (null? bits)
      '()
      (let ((next-branch
               (choose-branch (car bits) current-branch))
           )
           (if (leaf? next-branch)
               (cons (symbol-leaf next-branch)
                     (decode-1 (car bits) tree)
               )
               (decode-1 (car bits) next-branch)
           )
      )
    )
  )
  (decode-1 bits tree)
)

(define (choose-branch bit branch)
  (cond ((= bit 0) (left-branch branch))
        ((= bit 1) (right-branch branch))
        (else (error "Bad bit -- choose-branch" bit))
  )
)
```

> Scheme 的编码体验真的是 蛮差的 :)

#### 小游戏 复数

* 直角坐标形式: `z = x + iy` (i^2 == -1)
  - 加
* 极坐标形式: `z = re^iA` (r 模, A 幅角)
  - 乘

* 数据抽象 的 **最小允诺原则**

```
运算 (add-complex sub-complex mul-complex div-complex)

-----------------------------------------------------

数据 (real-part & imag-part, magnitude & angle)
----------------------------------------------
        直角坐标 表示       |      极坐标 表示
```

* 基于类型的分派
  - **可加性**

### 模块 对象 状态

* 基于对象 vs 基于(信息)流处理

```scheme
; Global (open) state
(define balance 100)

(define (withdraw amount)
  (if (>= balance amount)
      (begin (set! balance (- balance amount))
             balance
      )
      "Insufficient funds"
  )
)

(withdraw 36)
; 64
(withdraw 36)
; 28
(withdraw 36)
; Insufficient funds

; Internal (scope) state
(define withdraw2
  (let ((balance 100))
    (lambda (amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
             balance
          )
          "Insufficient funds"
      )
    )
  )
)

(withdraw2 36)
; 64
(withdraw2 36)
; 28
(withdraw2 36)
; Insufficient funds

; Instance (object) state
(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance
        )
        ("Insufficient funds")
    )
  )
)

(define W1 (make-withdraw 100))
(define W2 (make-withdraw 100))

(W1 60)
; 40
(W2 70)
; 30
```

```scheme
(define (make-account balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance
        )
        "Insufficient funds"
    )
  )
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance
  )
  (define (dispatch m)
    (cond ((eq? m 'withdraw) withdraw)
          ((eq? m 'deposit) deposit)
          (else (error "Unknown request -- make-account" m))
    )
  )
  dispatch
)

(define acc (make-account 100))

((acc 'withdraw) 50)
; 50
((acc 'deposit) 30)
; 80
((acc 'withdraw) 20)
; 60
```

- 如果一个语言支持在表达式里 `同一的东西可以相互替换` 的观念
- 且这样的替换不会改变表达式的值
- 称为: **具有引用透明性**
- 包含 `set!` 打破了 `引用透明性`
- 相对于 函数式程序设计, 采用赋值(`set!`)的程序设计被称为 命令式程序设计

#### 小游戏: 数字电路模拟器

* 摘抄2段局部代码

```scheme
(define (add-gate a1 a2 output)
  (define (and-action-procedure)
    (let ((new-value (logical-and (get-signal a1) (get-signal a2))))
      (after-delay and-gate-delay
        (lambda ()
          (set-signal! output new-value)
        )
      )
    )
  )
  (add-action! a1 and-action-procedure)
  (add-action! a2 and-action-procedure)
  'ok
)

(define (make-wire)
  (let ((signal-value 0) (action-procedures '()))
    (define (set-my-signal! new-value)
      (if (not (= signal-value new-value))
          (begin (set! signal-value new-value)
                 (call-each action-procedures)
          )
          'done
      )
    )
    (define (accept-action-procedure! proc)
      (set! action-procedures (cons proc action-procedures))
      (proc)
    )
    (define (dispatch m)
      (cond ((eq? m 'get-signal) signal-value)
            ((eq? m 'set-signal!) set-my-signal!)
            ((eq? m 'add-action!) accept-action-procedure!)
            (else (error "Unknown operation -- wire" m))
      )
    )
    dispatch
  )
)
```

#### 并发

* **serializer**
  - **mutex** 互斥元, `acquired` or `released`

* 并发 时间 通信

```
从本质上看, 在并发控制中,
任何时间概念都必然与通信有内在的密切联系.

有意思的是, 时间与通信之间的这种联系也出现在相对论里,
在那里的光速是与时间和空间有关的基本常量.

我们在计算模型领域遇到的复杂性,
可能就是物理世界中最基本的复杂性的一种反映.
```

* **流**
  - `无穷`
  - 此处用 `数学问题的计算` 去讲解 `流/Generator` 的应用, 是我目前见到过的最佳的例子
  - **无穷的流**, 无限的 **无理数** 的数值逼近, 第一次觉得如此美妙! 赞!

```scheme
; v1
(define (sum-primes a b)
  (define (iter count accum)
    (cond ((> count b) accum)
          ((prime? count) (iter (+ count 1) (+ count accum)))
          (else (iter (+ count 1) accum))
    )
  )
  (iter a 0)
)

; v2
(define (sum-primes a b)
  (accumulate +
              0
              (filter prime? (enumerate-interval a b))
  )
)
```

> 本章讲解并不全面, 但是用数学问题举例, 独具美感!

### 元语言 抽象

### 寄存器 计算

------------------

## 编程珠玑

* [编程珠玑 第2版 修订版](https://book.douban.com/subject/26302533/)
* [编程珠玑 续 修订版](https://book.douban.com/subject/26302596/)

```
数年前, 买过一本, 应该是: 编程珠玑 (续), 没看多少, 丢了
此次再观之, 亲切了不少, 也算是个人成长的一种佐证吧 :)
```

* 也算作是拜读 **计算机程序设计艺术** 之前的准备书目吧 :)

### 数据决定程序结构

### 编写正确的程序

### 编程小事

### 程序性能分析

### 粗略估算

### 算法设计

### 代码调优

### 节省空间

### 排序

### 取样

### 搜索

### 堆

### 字符串

### 性能监视工具

### 关联数组

### 程序员的忏悔

### 自描述数据

### 劈开戈尔迪之结

### 计算机科学箴言集

### 粗略估算

### 人员备忘录

### 小语言

### 文档设计

### 图形化输出

### 对调查的研究

### 绝妙的取样

### 数值计算

### 选择

------------------

## 程序员修炼之道

* [程序员修炼之道 (第2版)](https://book.douban.com/subject/35006892/)
  - 副标题: 通向务实的最高境界
  - 个人觉得本书的亮点是: 用不同的编程语言贯穿全书

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

* 语义不变式
  - 清晰明确 (人人可以记住) 可执行的 强有力的 约定 (规则/方针)
  - 往往是 简短的一句话

* 资源
  - 在哪分配, 在哪释放
  - 构造函数, 析构函数
  - try ... finally ...
  - Rust!

```rust
fn main() {
  // Create a path to the desired file
  let path = Path::new("hello.txt");
  let display = path.display();

  // Open the path in read-only mode, returns `io::Result<File>`
  let mut file = match File::open(&path) {
    Err(why) => panic!("couldn't open {}: {}", display, why),
    Ok(file) => file,
  };

  // Read the file contents into a string, returns `io::Result<usize>`
  let mut s = String::new();
  match file.read_to_string(&mut s) {
    Err(why) => panic!("couldn't read {}: {}", display, why),
    Ok(_) => print!("{} contains:\n{}", display, s),
  }

  // `file` goes out of scope, and the "hello.txt" file gets closed
}
```

* 耦合
  - 类继承
  - 全局数据 (不仅仅是: 变量)
  - 方法调用链

* 耦合 的 表现
  - 古怪的依赖关系
  - 改一处 动全身
  - 开发不敢改东西
  - 开会要叫很多人

* **TDA** tell-don't-ask

* 响应式
  - 有限状态机 (FSM)
  - 观察者模式 (观察者与观察对象注册在一起)
  - 发布/订阅 (pub channel sub)
  - 响应式编程与流

```
这一部分写的一般
```

* Elixir `|>`
  - 不要囤积状态, 传递下去
* Rust `Option`

```
看得出来, 作者蛮喜欢 Elixir
好巧, 我也是
```

* OO 继承税
  - 耦合严重
* 继承 的 替代
  - 接口/协议
  - 委托
  - mixin

```ruby
# 委托
class Account
  def initialize(...)
    @repo = Persister.for(self)
  end

  def save
    @repo.save()
  end
end
```

```ruby
# mixin
mixin CommonFinders {
  def find(id) { ... }
  def findAll() { ... }
}

class AccountRecord extends BasicRecord with CommonFinders
```

* 并发 (软件) & 并行 (硬件)
  - `时域耦合` (顺序依赖/预设)
  - `共享状态` 是不正确的状态

* 时域耦合
  - 并发
  - 次序

* 共享状态 是不正确的状态
  - 信号量 和 其他形式的互斥
  - 信号量: 同一时间, 一人持有 (Lock)
  - 随机故障通常是并发问题
  - Rust ownership

* 角色(Actor)与进程
  - 角色: 一个独立的处理单元, 具有私有状态, 收发/处理消息
  - 进程: 以角色的形式运转的虚拟处理机

* 角色 (Actor)
  - 本地状态在角色之外无法访问
  - 消息都是单向的, no ack
  - 角色一次只处理一条消息, 直到处理完
  - Elixir

```
传统观点认为, 一旦项目到了编码阶段, 就几乎只剩一些机械工作.
这种态度是软件项目失败的最重要的原因.

代码需要演化: 他不是一个静态的东西

软件更像是园艺而非建筑

重构是一项日复一日的工作
尽早重构, 经常重构
```

* 个人很喜欢这个类比:
  - **园艺**

* 个人思考:
  - **一直在重构的, 务实的程序员, 如何被合理的承认与尊重?**

```
测试获得的主要好处发生在你考虑测试及编写测试的时候,
而不是在运行测试的时候.

构建软件的唯一方法是增量式的
基于端对端构建
```

* 基于特性的测试 **Property-based testing**
  - [Python Hypothesis](https://github.com/HypothesisWorks/hypothesis)

* **安全性的基本原则**
  - 攻击面积最小化
  - 最小特权原则
  - 安全的默认值
  - 敏感数据加密
  - 维护安全更新

* 密码学

```
当涉及密码学的问题时,
常识可能会让你失望.
当涉及加密时:
永远不要自己做!
```

* 命名
  - 表明意图
  - 团队/社区文化
  - 尽可能持续一致性, 即: 始终如一
  - 及时修正
  - 好好取名, 需要时更名

```
注意力分散的人在解决复杂问题时比有意识的人做得更好
```

* 敏捷宣言
  - **个体和互动** 高于流程和工具
  - **工作的软件** 高于详尽的文档
  - **客户合作** 高于合同谈判
  - **响应变化** 高于遵循计划

```
永远不可能有一个叫敏捷的工艺流程

  个人读到这里的时候蛮感动的!
  外行 (我有一个流程)
  内行 (没有一成不变的流程)
  老板选择 有流程的外行 指导 没有流程的内行
```

* 务实的团队
  - 质量是内在的, 无法额外保证
  - 只有在业务上有意义时, 才有必要在用户需要时即期交付
  - 测试状态覆盖率, 而非代码覆盖率

```
认可别人是一种能力
发自内心的认可别人是一种难能可贵的能力
```

------------------

# 始于 2019

## 卡洛·罗韦利 Carlo Rovelli

* [卡洛·罗韦利 Carlo Rovelli](https://book.douban.com/author/1987750/)
  - 最近几年, 这个哥们几乎每年一本书 :)

* [现实不似你所见: 量子引力之旅](https://book.douban.com/subject/27156306/)
  - 在 2021 年, 五一小长假 期间, 又重新读了一遍
  - 五一出游, 书留在了民宿 `在田间`
  - 颇有缘分的是, 屋内恰好有一本: 人生若只如初见

* [时间的秩序](https://book.douban.com/subject/33424487/)
  - 在 2021 年, 五一小长假 前后, 又重新读了一遍
  - 赠与 @`Jan Li`

* [Helgoland ?](https://book.douban.com/subject/35265189/)

```
作者文笔颇具诗意
极少见到科普文笔如此诗韵
读了几遍之后
更觉诗歌集的影子
好奇, 渴望, 激动, 求知
```

```
量子场绘制了空间, 时间, 物质与光,
在事件之间交换信息.
`实在 (Reality)` 是由独立事件构成的网络,
概率使它们相互关联,
在两个事件之间,
空间, 时间, 物质与能量,
消融在一团概率云中.
```

* 时间的崩塌
  - 广义相对论: 物体会使它周围的时间变慢
  - 物体会自然向时间流逝更慢的地方运动
  - (时间的 **统一性** 消失)
  - 如果观测事物的微观状态, 过去和未来的区别会消失
  - 过去与未来的区别只适用于我们对世界的模糊的观察
  - (时间的 **方向** 消失)
  - 狭义相对论: 时间会被速度延缓
  - 在过去与未来之间, 还存在一个时间段, 既非过去, 亦非未来
  - (时间的 **当下** 终结)
  -
  - (时间的 **独立性** 消失)

```
运动 相对于什么?

在空间 A 点, 两个钟分开, 然后又回到 A 会合.
运动相对于这个唯一的参照点 A

如果两个种不再会合, 快慢没有意义!
```

* 时间 - 热 熵 - 不可逆性

* 场
  - 这个极其抽象的概念是最重要的一种思维模式转换

> 无就是无, 无不存在, 就像分母为 0 一样没有意义

* 分立性
  - 除了数学可以连续, 一切皆是分立

```
我们认为物质无法由没有维度的点构成,
因为无论我们把多少点放在一起,
都不会得到有维度的东西.
```

```
高斯提出的描绘曲面的方法,
以及由黎曼推广的描绘三维或更高维空间曲率的方法,
不是要以 "从外面看" 的视角来描绘弯曲的空间,
说明它在外部空间如何弯曲,
而是要从一个在这个空间内部运动的人的视角来描述.
例如, 在普通球体的球面上, 一切沿 "直线" 的运动在走过相同的距离
(赤道的长度)后都会回到起点.
三维球面就是具有同样属性的三维空间.
```

```
如果电子只有在进行相互作用,
与其他物体碰撞时才出现呢?
如果在两次相互作用之间,
电子并没有确定的位置呢?
如果始终具有确定的位置,
是只有足够大的物体才需要满足的条件呢?
```

```
电子不是始终存在,
而是在发生相互作用时才存在,
它们在与其他东西碰撞时才突然出现.
从一个轨道到另一个轨道的量子跃迁实际上是它们真实的存在方式.
电子就是从一个相互作用到另一个相互作用跃迁的集合.
当没有东西扰动它时, 电子不存在于任何地方.
海森堡写出了数学矩阵, 而不是电子的位置和速度.
他把数学矩阵进行乘除运算, 来代表电子可能的相互作用.
```

```
除了那些不变量如质量外,
物体自身没有其他属性.
其位置, 速度, 角动量, 电势等,
只有在碰撞,
与另一个物体相互作用时才具有实在性.
就像海森堡意识到的那样,
不只是位置无法被定义,
在两次相互作用之间,
物体的任何变量都无法被定义.
理论相关性的一面是普遍存在的.
在与另一个物体相互作用的过程中,
物体突然出现,
其物理量 (速度 能量 动量 角动量)不能取任意值,
狄拉克提出了计算物理量可能取值的一般方法.
这些值与原子发射的光谱相似.
如今, 我们把一个变量可以取的特定值的集合称为这个变量的 "谱"
```

```
这就是狄拉克的量子力学;
它是一种计算物理量取值范围的方法,
也是计算某个值在一次相互作用中出现的概率的方法.
就像这样, 两次相互作用之间发生了什么, 理论并没有提及, 它根本不存在.
我们可以把在某个位置找到电子或任何其他粒子的概率想象成一块弥散的云,
云越厚, 发现粒子的概率就越大.
有时把这种云想象成真实存在会很有用.
例如, 表示环绕原子核的电子云可以告诉我们,
当我们观测时电子更有可能出现在哪儿.
这就是原子里的 "轨道"
```

```
这种云由被称为 "波函数" 的数学对象来描述.
薛定谔写出了描述其时间演化的方程.
量子力学经常被误认为等同于这个方程.
薛定谔希望用 "波" 来解释量子理论的奇异之处:
从海浪到电磁波, 波都是我们充分理解的内容.
即便是今天, 仍然有一些物理学家试图通过把实在看作薛定谔的波来理解量子力学.
但海森堡和狄拉克立刻意识到这是不可行的.
如果把薛定谔的波看作真实的东西就把它看得太重要了,
不能帮助我们理解理论, 反而带来了更多困惑.
除了一些特殊情况之外, 薛定谔的波不在物理空间中, 这剥夺了它所有的直观特征.
但是薛定谔的波是关于实在的糟糕图像的主要原因在于,
当一个粒子与其他东西发生碰撞时, 它总在一个点上, 它不会像波一样在空间中散开.
如果我们把电子设想为波, 那么在解释每次碰撞时这个波如何瞬间集中于一点时就会遇到困难.
薛定谔的波不是一个对实在的有效表示, 它是一种计算的辅助,
允许我们以某种精确度预测电子会在何处再次出现.
电子的本质不是波, 波只是它在相互作用中显现自身的方式

电子与其他构成世界的粒子, 都是场的量子化.
与法拉第和麦克斯韦的场相似的 "量子场",
遵循分立性与量子的概率.
狄拉克写出了电子与其他基本粒子的场的方程,
法拉第引入的场与粒子的明显差别消失了.
与狭义相对论相容的量子理论的一般形式被称为 量子场论.

它构成了今日粒子物理学的基础. 粒子是场的量子化, 正如光子是光的量子化.
所有的场都在相互作用中表现出分立的结构.
在 20 世纪, 基本场的清单不断被修改, 如今我们拥有被称为 "基本粒子的标准模型" 的理论,
在量子场论的语境中, 它几乎可以描述除引力外, 我们可见的一切.
```

```
量子力学并没有描述事物本来如何:
它描述的是事物如何出现和事物之间如何相互作用.
它没有描述哪里会有一个粒子, 而是描述了粒子如何向其他粒子展现自己.
存在的事物被简化为可能的相互作用的范围.
实在成了 相互作用, 实在成了 关联.
```

* 量子力学发现了世界的三个特征

```
分立性
  系统状态的信息是有限的, 由普朗克常数限定
不确定性
  未来并非完全由过去决定, 我们所见的严格的规律性最终是统计学上的
关联性
  自然的事件永远是相互作用.
  系统的全部事件都相对于另一系统而出现.
  量子力学教会我们,
  不要以处在某一状态的 "物体" 的角度来思考世界,
  而应该从 "过程" 的角度来思考.
  过程就是从一次相互作用到另一次相互作用的历程.
  物体的属性只有在相互作用的瞬间才以分立的方式呈现,
  也就是只在这些过程的边缘,
  只在与其他物体发生关联时才出现.
  无法对其做出完全确定的预测, 只能进行概率性的预测.
```

```
测量长度, 面积, 体积实际上是在计算单个元素这一观念,
已经在 19 世纪由黎曼本人提出过.
身为发展了连续弯曲数学空间理论的数学家,
黎曼早就清楚离散的物理空间比连续空间更为合理.
```

```
总结一下, 圈量子引力理论, 或者说圈理论,
以一种相当保守的方式整合了广义相对论与量子力学,
因为它并没有引入这两个理论以外的任何其他假设
```

```
广义相对论告诉我们空间是动态的东西,
就像电磁场:
一个活动的巨大软体动物, 可以弯曲伸展, 我们栖居其中.
量子力学告诉我们每种场都由量子构成,
也就是存在着精细的分立结构.
因此物理空间作为一种场, 也由量子构成.
表示其他量子场特征的分立结构也表示量子引力场的特征,
因此也表示空间的特征.
我们预言会有引力的量子, 正如存在光量子, 电磁场的量子, 以及量子场的量子.
但空间是引力场, 引力场的量子就是空间的量子: 空间的分立成分.

圈量子引力的核心预言是空间不是连续体, 不是无限可分的,
它由 "空间原子" 组成, 比最小的原子核的十亿分之十亿分之一还要小.
圈量子引力以精确的数学形式来描述这一空间的原子与分立量子结构.
通过把狄拉克量子力学的一般方程应用到爱因斯坦引力场可以得到这个结果.
圈理论特别强调体积 (比如给定立方体的体积) 不能任意小, 存在一个最小的体积,
比这个最小体积还小的空间不存在.
存在一个最小体积的量子, 即最基本的空间原子.
```

* 自旋网络
  - 物理学中半整数被称为 **自旋**
  - 因为它们出现在自旋物体的量子力学中

