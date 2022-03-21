# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/20 10:39

"""
描述
给出一个包含 0 .. N 中 N 个数的序列，找出0 .. N 中没有出现在序列中的那个数。

样例
样例 1:

输入:[0,1,3]
输出:2
样例 2:

输入:[1,2,3]
输出:0

解题思路：
在leetcode的讲解中看到了一个很好的位运算办法，而且也很简单易懂，思路也很简单。
index: 0123
value: 0134
missing
=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
=(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
=0∧0∧0∧0∧2
=2
如果不缺数，再加上最大数应该对应的索引（也就是所给的数里面缺的索引，比如上面的例子，没有4号索引），每个数以及它应该对应的索引取
异或，整体再去异或，应该为0，但是由于缺少了一个数，所以整体异或之后所得的结果就是那个缺少的数。

"""


class Solution:
    """
    @param nums : An array of integers
    @return : An interger
    """

    def findMissing(self, nums):
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing


s = Solution()
ls = [0, 1, 2, 4, 5, 6, 7, 8, 9]
print(s.findMissing(ls))
