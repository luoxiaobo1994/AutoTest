# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 14:38
# Desc: 提前知道一段时间的股价.求这段时间的操作,所能获得的最大收益.

"""
原理:
低买,高卖.
算法核心:
相邻两数

"""


class Solution:
    def maxProfit(self, prices):
        sum = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                sum += prices[i + 1] - prices[i]
            continue
        return sum


prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))


class Solution2:
    def maxProfit(self, prices):
        return sum([prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] - prices[i] > 0])
