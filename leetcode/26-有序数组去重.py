#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
有序数组去重，Remove Duplicates form Sorted Array

原题特别指定了：原地操作in place，不申请新数组空间，O(1)空间复杂度。
最后的constraints中指出，数组可能为空（长度为0）。
意思是只在原数组上操作，并且最终按返回的数字截取范围来判断是否通过。

犯的错误：当成必须保留所有数据，通过遍历对换完成。效率很低。
实际上可以直接覆盖数据。

标准解法：快慢指针。考察目的：数组，快慢指针的思路。
写出来非常优雅。快慢指针是双指针的一种，而双指针的本质是为了区分已处理和未处理区域。
如果没有题目中的空间限制，也可以用Set的特性，或部分语言自带API实现。

'''

# 快慢指针
# 最精炼的写法，减少了不必要的变量和判断。会破坏原数据。
# 时间复杂度O(n)，空间复杂度O(1)
def fast_slow_points(li):
    # 题目的限制条件，可能为空数组
    if len(li) < 1:
        return 0
    # 快慢指针
    slow = 0
    for fast in range(len(li)):
        if li[slow] != li[fast]:
            slow += 1
            li[slow] = li[fast]
    return slow + 1


# 暴力解
# 保留所有数据，只通过对换位置完成。符合题目要求。
# 空间复杂度常数，时间复杂度因为两个迭代为n平方
def brute_force_move(li):
    if len(li) <= 1:
        return len(li)
    if len(li) == 2:
        if li[0] == li[1]:
            return 1
        else:
            return 2
    num = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[j] > li[i]:
                li[i+1] = li[j]
                num += 1
                break
    return num


# 用Set无重复的特性
# 平时可以这么用，题目限制做题是过不了的（使用了额外空间/截取原数组判断）
def set_remove_duplicates(li):
    return len(set(li))


if __name__ == "__main__":
    ls = [1, 1, 2, 2, 2, 3, 3]
    # ls = [1, 1, 1, 2]
    # ls = [1, 1]
    # ls = [1, 2]
    # ls = []
    print(ls[0:fast_slow_points(ls)])
    print(ls[0:set_remove_duplicates(ls)])
    print(ls[0:brute_force_move(ls)])