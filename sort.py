#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 排序
# 把无序列表转换为有序列表，针对数字

# 常见方法非常多，按照看的教程一个有意思的分类：
# Low B 三人组：冒泡，选择，插入 （都是原地排序，复杂度n平方，效率较低）
# 牛逼  三人组： 快排，堆排，归并 （待总结）
# 其它  排序 ： 希尔，计数，基数 （待总结）

# 原地排序，也叫就地排序，不借助其它辅助结构直接改自身，即 in-place

# Low B 三人组

# 冒泡排序
# 从头开始每次都两两比较把最大的交换过去
# 每挤过去一个，最后面的有序区就多一个。只排无序区
def buble_sort(li):
    for i in range(len(li) -1):
        for j in range(len(li) -1 -i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


if __name__ == "__main__":
    ls = [11, 44, 33, 77, 55, 22, 66]
    print(ls)
    print(buble_sort(ls))
    