# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 14:55
# Desc: 轮转数组

"""
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]   ==> [7] + [1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]   ==> [6,7] + [1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]   ==> [5,6,7] + [1,2,3,4]

解题思路:
轮转之后,原本的相对位置是没有改变的.5,6,7并没有轮转成7.6.5,所以,直接截取就好了.
轮转的次数,大于数组长度,则必然超过多次回正的周期了.所以,轮转的次数需要对数组长度求余
"""


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < len(nums):
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        else:
            nums[:] = nums[len(nums) - k % len(nums):] + nums[:len(nums) - k % len(nums)]
