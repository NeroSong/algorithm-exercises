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
写出来非常优雅。
如果没有题目中的空间限制，也可以用Set的特性，或部分语言自带API实现。

'''

# 快慢指针
# 最精炼的写法，减少了不必要的变量和判断
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


# 用Set无重复的特性
# 平时可以这么用，题目限制做题是过不了的（使用了额外空间/截取原数组判断）
def set_remove_duplicates(li):
    return len(set(li))


if __name__ == "__main__":
    ls = [1, 1, 2, 2, 2, 3, 3]
    print(ls[0:fast_slow_points(ls)])
    print(ls[0:set_remove_duplicates(ls)])