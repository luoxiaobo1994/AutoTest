# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/30 20:55
# Desc:

"""
类似打牌摸牌,手上默认有一张(列表首位).
从第2个元素开始,每个元素都假定为抽到的拍.
抽到之后,和手上的牌最后一个依次对比,直到找到的牌不大于当前的数.

"""


def insert_sort(ls):
    for i in range(1, len(ls)):  # i表示摸到的牌的下标.
        tmp = ls[i]
        j = i - 1  # j指手里的牌的最后一个的下标
        while ls[j] > tmp and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = tmp  # 为什么不能直接写ls[i] 因为移动了数据,i位置的数据肯定变了.
        print(ls)


ls = [5, 6, 3, 2, 7, 9, 8, 1]
insert_sort(ls)
print(ls)
