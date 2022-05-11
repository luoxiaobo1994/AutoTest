# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 15:40
# Desc:  给定一个数组,里面有一个数字,只出现了一次.其余的都出现了2次以上.找出这个只出现1次的数.

"""
解题思路:
使用位运算,任何数,异或自己,等于自己.5^0=5
异或自己等于0,5^5=0
连续异或,则能挑选出那个不一样的.5^1^2^6^2^5^1=6

"""


class Solution:
    def singleNumber(self, nums):
        s = 0
        for i in nums:
            s = s ^ i
        return s
