#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归（调用自己，必须有结束条件）
# 在方法内部，如果碰到递归，则结束后再一层层上来。
# 即先打印后递归，和先递归后打印的区别。

# 先打印，结果为 3，2，1
def func1(x):
    if x>0:
        print(x)
        func1(x-1)

# 先递归，结果为1，2，3
def func2(x):
    if x>0:
        func2(x-1)
        print(x)

# 汉诺塔问题
# 大小圆盘三个柱子间移动，每次只能移动一个，小的必须在大的上面
# 设有n个盘子，ABC三个柱子，盘子开始均在A上按顺序放好，需要全部移动到C上
# 过程分三个步骤：1. 把第n-1个盘子（上面的），从A通过C移动到B【需要完成的过程】
#              2. 把第n个盘子（下面的），从A移动到C 【一步，每次移动的一步】
#              3. 把第n-1个盘子（上面的），从B通过A移动到C 【需要完成的过程】
# 每次均按照这个模式移动，因此是个递归问题，中间的过程就是重复调用。步骤可通过n为3开始推广得到
# 方法本身定义为，把第n个盘子，从A通过B移动到C，中间打印的一步即为移动的一步
def hanoi(n, A, B ,C):
    if n>0:
        # 第一步
        hanoi(n-1, A, C, B)
        # 第二步
        print("Moving from {} to {}".format(A, C))
        # 第三步
        hanoi(n-1, B, A, C)

if __name__ == "__main__":
    func1(3)
    print('---')
    func2(3)
    print('---')
    hanoi(4, "A", "B", "C")