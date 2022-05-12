# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 23:18
# Desc: 翻转一个整数

class Solution():
    def reverseNum(self, num):
        res = 0  # 初始的结果，0是对应循环的另外一种结果。 输入为0，可以直接返回0.
        flag = 0
        if num < 0:
            num = num * -1
            flag = 1
        while num != 0:
            n = num % 10  # 求余
            new_res = res * 10 + n  # 结果会在循环里，逐渐*10+余数。
            if (new_res - n) / 10 != res:  # 数字溢出，返回0
                return 0
            res = new_res
            num = num // 10  # 刷新计算的值。
        if res > 2**31-1 or res < -2**31:  # 超过或小于边界，返回0
            return 0
        if flag:
            return res*-1  # 原本是负数的，还得乘-1
        return res


print(Solution().reverseNum(-123))