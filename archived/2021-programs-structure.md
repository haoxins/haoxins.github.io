---
title: 计算机程序的构造和解释 第2版
description: Structure and Interpretation of Computer Programs
date: 2021-01-28
---

* [计算机程序的构造和解释 (原书第2版)](https://book.douban.com/subject/34464721/)
  - https://book.douban.com/subject/1148282/

* 同样是拜读 **计算机程序设计艺术** 之前的准备书目 :)

* **不推荐**
  - Scheme (Lisp) 有特色, 但过时了
  - 翻译不行!

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

* 元循环求值器
* 惰性求值
  - 正则序 和 应用序
  - 将 流 视作 惰性的 表
* 非确定性计算
* 逻辑程序设计
  - 模式匹配

### 寄存器 计算

> 不如看 **MMIX: 新千年的精简指令集计算机** (Donald Knuth)
