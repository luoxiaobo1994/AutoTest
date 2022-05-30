# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/30 21:55
# Desc: 快速排序

"""
1.找一个元素,进行归位操作:归位目标,左边的元素比他小,右边的元素比他大.
2.针对这个元素的左右侧,逐一递归步骤1.

"""


def partition(ls, left, right):
    tmp = ls[left]
    while left < right:  # 双指针没有重叠.
        while left < right and ls[right] >= tmp:  # 从右边开始找,只要这个数不小于归位的数
            right -= 1  # 往左走一位.

        ls[left] = ls[right]  # 把比归位数小的这个值,放到归位数的位置上.
        while left < right and ls[left] <= tmp:
            left += 1
        ls[right] = ls[left]  # 把比归位数大的值,放到右边的空位上.

    ls[left] = tmp

def quick_sort():
    pass
