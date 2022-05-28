# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/28 14:29
# Desc: 选择排序算法

def select_easy_sort(ls):
    """
    选择排序的原理:不断的找出最小(大)的,筛出来,依次排进去. 最后就按顺序排序了.
    这一版的问题:生成了两个列表,内存消耗高.内置方法min和remove都有循环查找操作,耗时.
    """
    ls_new = []  # 增加内存负担
    for i in range(len(ls)):
        min_val = min(ls)  # 耗时操作
        ls_new.append(min_val)
        ls.remove(min_val)  # 耗时操作
    return ls_new


def select_normal_sort(ls):
    for i in range(len(ls) - 1):
        min_loc = i  # 假定当前位置就是最小值.
        for j in range(i + 1, len(ls)):  # 从当前位置往后的地方找.
            if ls[j] < ls[min_loc]:  # 找到的这个值,如果比之前假定的最小值还小.
                min_loc = j  # 刷新最小值的下标.
        if min_loc != i:  # 不是之前假定的位置.
            ls[i], ls[min_loc] = ls[min_loc], ls[i]  # 元素交换,让小的来前面.
        print(ls)

ls = [3,5,1,4,2,6,9,7]
select_normal_sort(ls)

