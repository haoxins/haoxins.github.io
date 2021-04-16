---
title: 阅读 经典书籍
description: ~
date: 2021-01-28
---

* [银河帝国]: galactic-empire.md

------------------

# 始于 2021

## TAOCP

* [Wiki - The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)

* [计算机程序设计艺术 MMIX增补](https://book.douban.com/subject/35170836/)
* [计算机程序设计艺术 卷4A](https://book.douban.com/subject/34452973/)
* [计算机程序设计艺术 卷3](https://book.douban.com/subject/26953756/)
* [计算机程序设计艺术 卷2](https://book.douban.com/subject/26850558/)
* [计算机程序设计艺术 卷1](https://book.douban.com/subject/26681685/)

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

## 银河帝国

* 移步 [银河帝国][银河帝国]

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
((acc 'deposit) 30 )
; 80
((acc 'withdraw) 20 )
; 60
```

- 如果一个语言支持在表达式里 `同一的东西可以相互替换` 的观念
- 且这样的替换不会改变表达式的值
- 称为: **具有引用透明性**
- 包含 `set!` 打破了 `引用透明性`
- 相对于 函数式程序设计, 采用赋值(`set!`)的程序设计被称为 命令式程序设计

### 元语言 抽象

### 寄存器 计算

------------------

## 编程珠玑

* [编程珠玑 第2版 修订版](https://book.douban.com/subject/26302533/)
* [编程珠玑 续 修订版）](https://book.douban.com/subject/26302596/)

```
数年前, 买过一本, 应该是: 编程珠玑 (续), 没看多少, 丢了
此次再观之, 亲切了不少, 也算是个人成长的一种佐证吧 :)
```

* 也算作是拜读 **计算机程序设计艺术** 之前的准备书目吧 :)

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
* [时间的秩序](https://book.douban.com/subject/33424487/)
* [Helgoland ?](https://book.douban.com/subject/35265189/)

* 如果只看一本的话: `现实不似你所见: 量子引力之旅`
