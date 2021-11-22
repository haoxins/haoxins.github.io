---
title: 程序员修炼之道 第2版
description: 通向务实的最高境界
date: 2021-01-28
---

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

* 角色 (`Actor`) 与进程
  - 角色: 一个独立的处理单元, 具有私有状态, 收发/处理消息
  - 进程: 以角色的形式运转的虚拟处理机

* 角色 (`Actor`)
  - 本地状态在角色之外无法访问
  - 消息都是单向的, no ack
  - 角色一次只处理一条消息, 直到处理完
  - `Elixir`

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
