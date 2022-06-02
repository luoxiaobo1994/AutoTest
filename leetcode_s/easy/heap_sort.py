# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/6/1 23:18
# Desc: 堆排序实现


def shift(li, low, high):
    """
    :param li : 传入一个堆列表
    :param low : 堆的根节点
    :param high : 堆的最后一个元素位置
    :return
    """
    i = low  # 循环从根节点开始
    j = 2 * i + 1  # j是左子节点
    tmp = li[low]  # 把根节点的数据先取出来.
    while i <= high:
        if li[j + 1] > li[j] and j + 1 <= high:  # 有右子节点,并且比较大.
            j = j + 1  # 把当前指针指向右边的子节点.
        if li[j] > tmp:
            li[i] = li[j]
