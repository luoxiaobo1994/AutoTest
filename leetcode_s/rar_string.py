# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/12/6 20:45


class Solution:
    def compressString(self , test_string ):
        # write code here
        dic = {}
        for item in test_string:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        new_string = ''
        for k,v in dic.items():
            new_string += k
            new_string += str(v)
        if len(test_string) == len(new_string):
            return test_string
        else:
            return new_string
    def compressString2(self,test_string):
        dic = {}
        for item in range(len(test_string)):
            if 

s = Solution()
print(s.compressString('abcccaaaa'))