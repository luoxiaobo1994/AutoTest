# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 22:07
# Desc: 整数翻转,正数翻转还是正数,负数翻转还是负数.翻转后0开头的,去掉0.

class Solution():

    def reverseNum(self, num):
        ls = 0
        for i in range(len(str(num))):
            n = num % 10 * 10 **i
            ls += n
        return ls


print(Solution().reverseNum(123))