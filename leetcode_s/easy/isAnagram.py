# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/12 0:37
# Desc: 给定两个字符串，判断他们是否互为字母相同，但位置不同的字符串。

"""
字母异位词：长度一样，组成的字母一样，各字母出现的频率一样。

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1.update({i:s.count(i)})
        for j in t:
            dic2.update({j:t.count(j)})
        for z in dic1.keys():
            if dic1[z] == dic2[z]:
                continue
            else:
                return False
        else:
            return True
