# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/2 20:44

"""
给定一个字符串,查找出最长的子串,要求子串没有重复.返回子串的长度.
如:bbbbb -->b,abcabcbb-->abc
"""

class Solution:
    def lengthOfLongestSubstring(self,s):
        """
        :type s:str
        :rtype:int
        """
        dic = {}  # 期望存上目标字符的索引
        start = -1 # 为什么-1开始.因为传入' '空格时,0--1=1,至少一个的情况.
        max = 0  # 初始的子串长度

