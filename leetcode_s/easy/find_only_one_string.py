# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/12 0:08
# Desc: 给定一个字符串，找出第一个不重复的字符串。


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for x in s:
            if x not in dic:
                dic.update({x: s.count(x)})
        for y in dic.keys():
            if dic[y] == 1:
                return s.index(y)
        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for x in s:
            if x not in s_dict:
                s_dict.update({x: s.count(x)})
        for y in s_dict.keys():
            if s_dict[y] == 1:
                return s.index(y)
        return -1
