# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/9/11 9:36

import random
from base.common import runtime
from time import time


# @runtime
def select_sort(origin_items,comp=lambda x, y : x <y):
    """ 简单排序 """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(origin_items,comp=lambda x, y: x>y):
    """ 高质量冒泡排序(搅拌排序) """
    items = origin_items[:]
    for i in range(len(items)- 1):
        swapped = False
        for j in range(i,len(items)- 1 - i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1],items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 -i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

def bubbleSort(arg):
    num = len(arg)
    flag = True  # 交换标志.
    count = 0  # 统计交换次数
    while flag:
        for i in range(num):
            for j in range(0, num - i - 1):  # 自己前面的就不用排了,到你这,前面都排好了.
                if arg[j] > arg[j + 1]:  # 比较
                    arg[j], arg[j + 1] = arg[j + 1], arg[j]  # 交换
                    count += 1  # 交换,次数加1
                else:
                    flag = False  # 没有产生交换,退出循环.
    print(f"共执行交换{count}次.")
    print(f"排序后的列表:{arg}")
    return arg

def moretest(n,func):
    start = time()
    for i in range(n):
        ls = random.sample(range(20), 7)
        func(ls)
    return time()-start


if __name__ == '__main__':
    ls = random.sample(range(100),20)
    bubbleSort(ls)