# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 22:01
# Desc: 字符串翻转

"""
算法核心:
根据中心,对称交换即可.
--> 双指针,首位各一个,两个值交换即可.

"""


class Solution():

    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # 首尾交换即可
            left += 1  # 交换完,别忘记指针加减
            right -= 1
