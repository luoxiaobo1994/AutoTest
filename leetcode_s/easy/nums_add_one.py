# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 16:35
# Desc: 把一个正数按位拆分成一个数组,然后给这个数组+1.返回加1后的数组.

"""
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
"""


class Solution:
    def plusOne(self, digits):
        digits[-1] += 1  # 先让最后一位+1
        if 10 not in digits:
            return digits
        while 10 in digits:
            x = digits.index(10)
            if x != 0:
                digits[x] = 0
                digits[x-1] += 1
            else:
                digits[x] = 0
                digits = [1] + digits
        return digits

ls = [9,9,9,9,9]
print(Solution().plusOne(ls))
