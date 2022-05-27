# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/26 17:53
# Desc: 找到第一个错误的版本号
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self,n,targrt):
        # 二分查找
        start = 0
        end = n
        while start < end:
            mid = start + (end-start) //2
            # if
