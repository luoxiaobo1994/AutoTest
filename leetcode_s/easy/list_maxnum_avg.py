# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/20 10:49

"""
给定一个列表 list_1，里面嵌套了多个列表，请你计算出每个嵌套列表的最大值，并输出所有最大值的平均值。
"""

class Solution():

    def avg_max(self, nums):
        ls = []
        for i in nums:
            i.sort()
            ls.append(i[-1])
        return round(sum(ls)/len(ls),2)

ls = [[54, 28, 88, 99, 77],[99, 6, 37, 68, 83],[90, 52, 36, 4, 53],[85, 66, 11, 11, 61],[20, 52, 9, 81, 61],[23, 67, 37, 39, 18],[21, 36, 66, 80, 30],[74, 80, 5, 7, 96],[30, 35, 71, 73, 4],[40, 67, 67, 11, 71]]
s = Solution()
print(s.avg_max(ls))
