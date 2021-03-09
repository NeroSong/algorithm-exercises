#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链表最常见的5个操作：
- 单链表反转
- 成环检测
- 有序链表合并
- 删除倒数第n个节点
- 求中间节点

这几个操作同时也是LC原题，手写练习一下，最后有测试用例。
"""


# 定义单链表数据结构
class NodeList:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1. 单链表反转
# 方法有：用栈整体反转；递归；双指针
# 最优解：双指针，遍历过程中逐个反转指针，O(n)
def reverse_list(head: NodeList) -> NodeList:
    cur = None
    forward = head
    while forward:
        forward = head.next
        head.next = cur
        cur = head
        head = forward
    return cur


# 2. 链表成环检测
# 哈希表：查找O(1)，遍历加入查找即可（py里可用Set），注意要存元素而不是值，不然可能会重复
# 快慢指针：龟兔赛跑，环内快的一定会赶上慢的，即相遇就成环，否则快指针先到尾部
# 此处用快指针，空间复杂度O(1)，比哈希表好
def is_nodelist_cicle(head: NodeList) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


# 3. 有序链表合并
# 方法：迭代和递归，每一步都需要判断哪个链表的节点更小，以接在后面
# 此处用迭代，复杂度都是O(n+m)，迭代空间为常数，更好点
# 递归看起来很有意思，也写在下面 :)
def merge_sorted_list(l1: NodeList, l2: NodeList) -> NodeList:
    # 迭代，用到了哨兵节点prev
    prev = NodeList(-1)
    cur = prev
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if not l1:
        cur.next = l2
    else:
        cur.next = l1
    return prev.next

    # 递归
    # if not l1:
    #     return l2
    # if not l2:
    #     return l1
    # if l1.val < l2.val:
    #     l1.next = merge_sorted_list(l1.next, l2)
    #     return l1
    # else:
    #     l2.next = merge_sorted_list(l1, l2.next)
    #     return l2


# 打印链表，展现效果
def show_list(head: NodeList) -> None:
    ls = []
    while head:
        ls.append(str(head.val) + "->")
        head = head.next
    ls.append("Null")
    s = ""
    for i in ls:
        s += i
    print(s)


if __name__ == '__main__':
    # 1的测试用例为：
    # 1. 正常链表
    # 2. 空链表
    # 3. 只有一个节点
    # 4. 只有两个节点
    nl1 = NodeList(1)
    head = nl1
    for i in range(2, 6):
        head.next = NodeList(i)
        head = head.next

    nl2 = NodeList(None)

    nl3 = NodeList("only")

    nl4 = NodeList("first")
    nl4.next = NodeList("second")

    test_case_1 = [nl1, nl2, nl3, nl4]

    # 测试并输出结果
    print("反转链表")
    for i in test_case_1:
        show_list(reverse_list(i))
    print("")

    # 2的测试用例：
    # - 无环
    # - 整个为环
    # - 环在中间
    nl5 = NodeList(1)
    head = nl5
    for i in range(2, 6):
        head.next = NodeList(i)
        head = head.next
    head.next = nl5

    nl6 = NodeList(1)
    head = nl6
    head.next = NodeList(2)
    head = head.next
    # 环回到2这个节点
    temp = head
    head.next = NodeList(3)
    head = head.next
    head.next = NodeList(4)
    head = head.next
    head.next = temp

    test_case_2 = test_case_1.copy() + [nl5, nl6]

    # 测试并输出结果
    print("链表成环检测")
    for i in test_case_2:
        print(is_nodelist_cicle(i))
    print("")

    # 有序链表合并
    nl7 = NodeList(1)
    head = nl7
    for i in range(2, 6):
        head.next = NodeList(i)
        head = head.next

    nl8 = NodeList(1)
    head = nl8
    for i in range(3, 11, 3):
        head.next = NodeList(i)
        head = head.next

    print("有序链表合并")
    show_list(nl7)
    show_list(nl8)
    show_list(merge_sorted_list(nl7, nl8))
    print("")
