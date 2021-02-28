#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
最小栈，Min-Stack

实现一个带有最小获取最小元素方法的栈。即如下四个方法：
- pop()：删除栈顶元素
- push(x)：将x压入栈中
- top()：获取栈顶元素
- min()：获取最小元素
所有方法时间复杂度在常数级别

易混淆的点：后两个方法只是查询，不需要将获取的元素弹出

考察核心：如何在O(1)复杂度实现最小值的查询，如何在弹出栈顶元素恰好是最小元素时得到上一个最小元素

解决方法：
1. 辅助栈法：通过辅助栈实现，在另一个栈里存着最小值，查询时直接返回
2. 单栈法：思想同辅助栈，只是都保存在一个栈中，用一个变量记录当前最小值
3. 单栈差值法：单栈法的改进，通过记录差值，来减少对空间的使用
4. 新建数据结构法：用改进的链表实现一个栈，每个节点增加保存最小值的字段

'''


# 1. 辅助栈法
# 压入栈中时，如果有更小的值，则压入辅助栈
# 弹出栈顶时，如果恰好是最小值，则辅助栈也弹出（更新最小值）
# 查询顶端和最小时，直接返回两个栈的顶部元素
class MinStack1:
    def __init__(self):
        self.stack = []
        self.help = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.help or x <= self.help[-1]:
            self.help.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.help[-1]:
            self.help.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.help[-1]


# 2. 单栈法
# 减少了新建另一个栈的开销，改用变量记录最小值
# 本质上是把最小值也记录在栈中，弹出后能获取上一个最小值
class MinStack2:
    def __init__(self):
        self.stack = []
        self.minItem = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.minItem = x
        # x小于最小值，先把当前最小值压入栈中，再压入x
        if x <= self.minItem:
            self.stack.append(self.minItem)
            self.minItem = x
        self.stack.append(x)

    def pop(self) -> None:
        # 弹出的值如果是当前最小值，就再弹出一次并更新到最小值
        # 也就是为啥之前push更新最小值前，要先压入一次当前最小值，这里就能用到
        if self.stack.pop() == self.minItem:
            self.minItem = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minItem


# 3. 单栈差值法
# 栈中不保存元素而是每次和最小值的差值
# 相对于单栈法，每次都是通过当前最小值和栈顶值，推出了之前的最小值，因此更节省一点空间
class MinStack3:
    def __init__(self):
        self.stackDiff = []
        self.minItem = 0

    def push(self, x: int) -> None:
        if not self.stackDiff:
            self.minItem = x
        # 保存差值
        self.stackDiff.append(x - self.minItem)
        # 如果x更小，则跟新最小值差值
        # 此时入栈的差值为负数
        if x < self.minItem:
            self.minItem = x

    def pop(self) -> None:
        # 如果栈顶非负，出栈元素为栈顶+差值
        # if self.stackDiff[-1] >= 0:
        # 如果需要返回值，返回差值和栈顶的和，即为元素的值
        # return self.stackDiff.pop() + self.minItem
        if self.stackDiff[-1] < 0:
            # 如果栈顶为负值，此时栈顶元素就是当前最小值差值
            # return self.minItem
            # 并且说明要更新最小值差值
            self.minItem = self.minItem - self.stackDiff.pop()

    def top(self) -> int:
        if self.stackDiff[-1] >= 0:
            return self.minItem + self.stackDiff[-1]
        else:
            return self.minItem

    def min(self) -> int:
        return self.minItem


# 4. 新建数据结构法
# 用增加了min字段的链表实现这个栈
class MinStack4:
    class ListNodeMin:
        def __init__(self, x, y):
            self.val = x
            self.min = y
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if self.head == None:
            self.head = self.ListNodeMin(x, x)
        else:
            # 新节点比较更新min
            n = self.ListNodeMin(x, min(self.head.min, x))
            # 链表向前添加新节点，这样next就回到了上一个节点
            n.next = self.head
            self.head = n

    def pop(self) -> None:
        # 回到上一个节点，即弹出栈顶
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def min(self) -> int:
        return self.head.min

