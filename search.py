#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 查找
# 在数组中寻找相同值，找到返回下标，否则返回None


# 线性查找
def linear_search(li, val):
    for i, v in enumerate(li):
        if v == val:
            return i
    return None


# 二分查找，复杂度logn，远低于n，但需要num数组已升序排列。
# 更新了一个防止整形溢出的写法，一般用不到
# 有两种写法，这个算其中一个标准模板。标记重要的地方要仔细。
def binary_search(li, val):
    left = 0
    right = len(li) - 1  # 重要，-1
    # 到最后左右指针可能重合，所以循环条件包含等于
    while left <= right:  # 重要，<=
        mid = (left +
               right) // 2  # 或者这样写防止整形溢出，mid = left + (right - left) // 2
        if val == li[mid]:  # 重要，三种情况分开判断
            return mid
        elif val > li[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None  # 有时候判断第一个插入位置，left在最后重合后会向后一步，因此返回left即可。


if __name__ == "__main__":
    ls = [12, 22, 33, 43, 54, 67, 23]
    print(linear_search(ls, 33))
    ls.sort()
    print(binary_search(ls, 67))
