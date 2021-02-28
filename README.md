> Just some daily algorithm exercises records & reflections.

如果把问题进行分类，从数据类型和解决思路入手是极好的。因此一道题往往有这两种标签，即数据类型和算法。合适的数据结构是基础，自身带有适用于不同问题的特性。算法也依附于此，由解决问题的思想和具体方式构成。

这次的练习旨在从头开始，查漏补缺，提高能力。首先手写实现基本的数据结构，然后通过做题来整理算法。一边学习，一边记录和总结反思。

## 数据结构

先从数组和链表这两种最基本的物理结构开始。

- 数组在内存中是连续的，顺序结构，即元素一个挨着一个储存。知道下标就可以立即访问，但增加删除时需要移动其它元素。因此适合多读少写的场景。

- 链表，顾名思义是链式结构，在内存中并不紧挨着。每个元素指向下一个元素的位置，因此访问时需要从头遍历才能找到。好处就是增删时只需要修改相邻元素的指向，不需要移动其它元素，开销很小。所以它适合多写少读的场景。

之后的数据结构都是逻辑结构，大多数都可以用数组和链表分别实现。在具体的场景下各有优劣，主要还是取决于问题的侧重和自身的特性。

### 线性数据结构

线性结构，元素都是同一层级的，有序且相互之间前后一一对应，都在一个线性序列当中。

- 数组：高速随机访问
- 链表：灵活内存分布
- 栈：先进后出，类似往罐子里放饼干，只有一头能进出。回溯效果
- 队列：先进先出，类似汽车过山洞，一头进另一头出。回放效果

### 非线性数据结构

非线性结构，元素之间并非权重一致。可能是一对多，或者多对多的关系。

- 散列表：也叫哈希表，key-Value结构，直接映射出地址。高效读写键值对
- 树：表现元素的相对层级关系，例如家谱。一对多
- 图：多对多的复杂关系。例如人际关系，相互是否认识

这些都是最基础的分类，每个结构还可以有特殊的子类实现，比如树里常见的二叉树等。

散列表比较特殊，应该算作对于数组的一种拓展，但因为储存位置实际分散，且相邻元素之间无对应关系，所以不是线性结构。

非线性结构的遍历，往往比较复杂，因为遍历操作本身是线性的。对于非线性结构，不同的遍历方法会导致不同的遍历顺序。

总体上按照相对关系可分为：线性结构，树结构，图结构。根据具体场景来选择使用。

## 算法

算法从定义来说，是要有具体可执行的步骤的，因此必须在相应的数据结构之上描述。但有些思路办法，我们广义上讨论的时候，往往也叫做XXX算法，这里就放在思路集合里。其它的算法则单独列出。

*（随时更新）*

### 思路集合

#### 暴力法
暴力迭代是很多问题解决的起点，先覆盖所有的可能路径，找出答案来，再看哪里能够进一步优化时间和空间，这种思路也是碰到未知领域的一般方法。

#### 循环，迭代，遍历与递归
概念浅析：
- 循环：指一切重复执行的行为，总体上包括后面各种理念
- 迭代和遍历：（在编程语境下）意思都是按照一定的顺序，来访问每一个元素
- 递归：字面意思，有去有回。编程中指方法调用自身的行为，本质上是栈的应用

从思路上说，递归也指一种不断分解问题规模，直到最后无法分解（终止条件），然后层层原路返回累积得到结果。

与之相区别的是，并归思想（分治思想），也是不断分解问题规模，大问题变成小问题，最后将所有小问题合并得到结果。

### 具体算法

#### 双指针

线性结构的单次遍历中，对元素的相关关系进行调整。

ref：[206.反转单链表](./leetcode/206-反转单链表.py)

#### 快慢指针

双指针的一种。两个在线性结构中以不同速度移动的指针，在有环或需要前后对比时效率很高。

有环的情况下，就像龟兔赛跑转圈圈一样，两个不同速度的总会遇到。

ref：[26.有序数组去重](./leetcode/26-有序数组去重.py)


### LeetCode 题解记录

放在仓库的 [leetcode](./leetcode/) 目录下，使用 Python3 ，每个py文件为一道题，包含大量注释。一般会有题目的理解，多个解法，以及一些简单的测试用例。后续也会进行一定的分类。

需要整理的题目记录中ing：

- [26.有序数组去重](./leetcode/26-有序数组去重.py)
- [206.反转单链表](./leetcode/206-反转单链表.py)
- [155.最小栈](./leetcode/155-最小栈.py)

