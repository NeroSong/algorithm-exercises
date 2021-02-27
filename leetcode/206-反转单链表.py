#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
反转单链表，Reverse Singly-linked List

非常直观的题目，反转后返回头结点。
考察对链表的理解程度。

有遍历新建法和逐步调换法两种思路，前者整体反转，后者逐个反转。
逐个反转，又有双指针和递归两种方式。
最优解法为双指针法。
'''


# 单链表定义
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 遍历新建
# 最直观的思路：先遍历获取所有值放在栈中，然后从栈中弹出创建新链表
# 时间和空间复杂度均为O(n)
def reverseList_new(head: ListNode) -> ListNode:
    stack = []
    while head != None:
        stack.append(head.val)
        head = head.next
    if not stack:
        return None
    nw = ListNode(stack.pop())
    flag = nw
    while stack:
        nw.next = ListNode(stack.pop())
        nw = nw.next
    return flag


# 递归法
# 链表本身由递归定义，而递归本质上是栈的应用
# 在归回来的过程中，虽然p一直被返回，但实际上并没有被用到
# 每一层的返回过程，head本身在不断的回溯，到了栈顶返回值p才终于被传出去
# 时空复杂度均O(n)
def reverseList_recur(head: ListNode) -> ListNode:
    # 递归解法，递进去时的终止条件
    # 其实是从head.next==None开始回归的，前面是防止给空链表
    if head == None or head.next == None:
        # 返回最后的节点，也就是反转后的头节点
        print("我是停止递归条件中的返回！" + "我返回了个" + str(head.val))
        return head
    # 开始递
    p = reverseList_recur(head.next)
    # 开始归，归的时候每次调换一对
    print("我是执行完调换后的返回！我调换了" + str(head.val) + "和" + str(head.next.val) +
          "，我返回了个" + str(p.val))
    head.next.next = head
    head.next = None

    # 从打印出的节点内容可知：p节点从一开始赋值后就没有变过，一路被传递回来
    # 只是归回来时，每次往回走一层，head就会往前移动一个，然后再调换
    return p


# 双指针法
# 之所以要双指针，是因为在单链表中遍历反序，
# 一个指针要确定下一个节点的位置，
# 另一个则负责记录前一个节点的位置，好让当前节点的next掉头
# 时间复杂度O(n)，完整遍历，空间复杂度O(1)。实际上因为操作更少，是最快的方案
def reverseList_double_point(head: ListNode) -> ListNode:
    cur = None
    flag = head
    # flag是当前要改指向的节点，开始后就移向下一个节点
    # cur代表上一个节点，改完之后同步前进到当前节点
    # 最后当前节点跟上flag的步伐
    while flag != None:
        flag = head.next
        head.next = cur
        cur = head
        head = flag
    return cur


def showList(head: ListNode) -> None:
    ls = []
    while head != None:
        ls.append(head.val)
        head = head.next
    print(ls)


if __name__ == "__main__":
    # 测试用例链表
    # ls = [1,2,3,4,5]
    ln = ListNode(1)
    head0 = ln
    for i in range(2, 6):
        ln.next = ListNode(i)
        ln = ln.next

    # 测试空节点
    head1 = None

    # 不同方法
    # nln = reverseList_new(head0)
    # nln = reverseList_recur(head0)
    nln = reverseList_double_point(head0)
    showList(nln)

    # nln = reverseList_new(head0)
    # nln = reverseList_recur(head0)
    nln2 = reverseList_double_point(head1)
    showList(nln2)