# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/2 12:10


"""
从列表里找两数相加,得到目标值.
如: 从[2,7,11,15]找出相加=9的两个数.返回他们的下标. 如 2+7=9 返回[0,1]

"""


class Solution:
    # 基础版本
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        for i in nums:  # 循环遍历.2 7 11 15
            j = target - i  # 当前值和目标值的差 j = 9 - 2 = 7
            start_index = nums.index(i)  # 当前值在原生列表的索引. 0
            next_index = start_index + 1  # 下一个值,至少是当前值在原生列表里的下一个. nums[1] = 1
            temp_nums = nums[next_index:]  # 从下一个值开始截取原生列表,得到一个新的临时列表. [7,11,15]
            if j in temp_nums:  # 如果7在[7,11,15]里面
                # 当前问题,只是考虑了四个数的列表求. 只返回找到的第一个符合要求的组合. 如果多了,就没有了.
                return (start_index, next_index + temp_nums.index(j))  # 返回当前值的索引,当前值下一个值+临时列表里的差值的索引.


class Solution2:
    # 相比上一个,这个用来求所有符合要求的组合情况.
    # 如[2,7,11,15,6,5,3] target=9,需要返回[(0,1),[4,6]]
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        res = []
        for i in nums:  # 循环遍历.2 7 11 15
            j = target - i  # 当前值和目标值的差 j = 9 - 2 = 7
            start_index = nums.index(i)  # 当前值在原生列表的索引. 0
            next_index = start_index + 1  # 下一个值,至少是当前值在原生列表里的下一个. nums[1] = 1
            temp_nums = nums[next_index:]  # 从下一个值开始截取原生列表,得到一个新的临时列表. [7,11,15]
            if j in temp_nums:  # 如果7在[7,11,15]里面
                # 当前问题,只是考虑了四个数的列表求. 只返回找到的第一个符合要求的组合. 如果多了,就没有了.
                res.append((start_index, next_index + temp_nums.index(j)))  # 返回当前值的索引,当前值下一个值+临时列表里的差值的索引.
        return res


class Solution3:
    # 优化版本
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        dic = {}
        for i in range(len(nums)):  # 还是先遍历
            if target - nums[i] not in dic:  # 目标值与当前值的差,不在字典里.
                dic[nums[i]] = i  # 那么dic['2'] = 0  把当前值当做建,在原生列表里的索引当做值. ==> dic={"2":0,"7":1,"11":2,"15":3}
            else:
                return [dic[target - nums[i]], i]  # 否则 [dic[差值在原生列表的索引],当前值的索引]  返回的是差值的索引,和当前循环到的索引.


ls = [2, 7, 11, 15]
target = 9
ss = Solution3()
print(ss.twoSum(ls, target))
