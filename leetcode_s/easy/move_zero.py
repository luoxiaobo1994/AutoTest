# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 20:56
# Desc: 给一个数组,将里面的0,移动到末尾去.

"""
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

输入: nums = [0]
输出: [0]

输入: nums = [1,2,3,4]
输出: [1,2,3,4]
"""

class Solution():

    def moveZeros(self,nums):
        index = 0
        for i in nums:
            if i != 0:
                pass