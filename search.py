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

# 二分查找，复杂度logn，远低于n，但需要数组已排好序。仅适合数字
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    # 到最后左右指针可能重合，所以循环条件包含等于
    while left <= right:
        mid = (left + right) // 2
        if val == li[mid]:
            return mid
        elif val > li[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == "__main__":
    ls = [12, 22, 33, 43, 54, 67, 23]
    print(linear_search(ls, 33))
    ls.sort()
    print(binary_search(ls, 67))
