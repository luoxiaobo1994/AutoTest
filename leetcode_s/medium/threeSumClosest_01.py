# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/12/8 12:23

class Solution:
    def threeSumClosest(self, num: list[int], target: int) -> int:
        nums = sorted(num)  # 先进行排序，方便处理。
        result = nums[0] + nums[1] + nums[len(nums) - 1]  # 为什么先取这个？这是一个起始计算值而已。最终比较一下，指针会移动。

        for i in range(len(nums) - 2):  # result已经用了一个了.
            if i > 0 and nums[i] == nums[i - 1]:  # 连续两个数相同。
                continue
            l = i + 1  # 左边的起始指针。
            r = len(nums) - 1  # 右边的指针。
           