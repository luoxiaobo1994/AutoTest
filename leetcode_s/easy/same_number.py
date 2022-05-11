# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 15:18
# Desc: 判断给定的数组里,是否有重复数组,有则返回True,没有则返回False

"""
解题思路:
法1.直接set()成集合,再对比集合的长度和原列表的长度.一样就没有重复,不一样.就有重复的.
法2.先将列表排序.sort一下,再循环,两个相邻的数,要是相等,就有重复了.
"""


class Solution1():

    def same_number(self, nums):
        if len(set(nums)) != len(nums):
            return True
        return False


class Solution2():

    def same_number(self, nums):
        nums.sort()  # 排序和循环都耗时,占空间,不推荐.
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
