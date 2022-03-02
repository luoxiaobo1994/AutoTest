# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/12/8 12:20


"""
给定一个数组,给定一个目标值. 从数组里找出3个数,相加之后,与这个目标值最接近.返回这个三个数的和.
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 先排序.好处理一些.
        nums = sorted(nums)
        # 因为要取3个,所以先取1,2和最后一个,看看相加的结果和目标值的差距,再进行平移
        result = nums[0] + nums[1] + nums[len(nums) - 1]  # 第一个组合结果.
        for i in range(len(nums) - 2):  # 因为最后一位已经取了,所以-2.
            if i > 0 and nums[i] == nums[i - 1]:  # 重复数字的情况,
                continue
            # 双指针的起点
            l = i + 1  # 左边,
            r = len(nums) - 1
            while l < r:  # 左右不较差
                val = nums[i] + nums[l] + nums[r]  # 临时结果.
                if abs(val - target) < abs(result - target):
                    result = val  # 取最接近目标值的那个值,刷新全局的result
                if val == target:  # 临时结果直接和目标值相等,那就是最近的了,直接返回.
                    return target
                elif val < target:  # 临时结果比目标值小了.
                    l += 1  # 那么左边的值小了,左边往右移1位
                else:
                    r -= 1  # 临时结果比目标值大了,那么右边的数往左移1位.
        return result

ls = [-1,1,2,-4]
target = 1
ss = Solution()
print(ss.threeSumClosest(ls, target))