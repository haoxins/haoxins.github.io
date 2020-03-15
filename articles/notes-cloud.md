---
title: Cloud notes
description: Cloud is future ~
date: 2019-06-28
---


https://www.gqlstandards.org







* 尽量使 `Scheduled queries` 越简单越好, 把复杂逻辑保存为 `Views`
  - 当 `DEBUG` 或 `change` 逻辑时, 变更 `Views` 不需要变更 `Scheduled queries`
