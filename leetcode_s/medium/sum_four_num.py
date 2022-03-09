# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/2 14:47

"""
给定一个包含n个整数的nums和一个目标值target,判断nums中是否存在四个元素,a,b,c,d 使得四个数的和与target相等.
找出所有满足条件,且不重复的四元组.
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums:List[int]
        """
        if len(nums) < 4:  # 元祖数字都不足,直接返回空
            return []
        nums.sort()  # 老样子,先排序
        ans = set()  # 一个集合,去重的.
        for i in range(len(nums) - 3):  # 因为要先取4个,所以一开始只能循环总数-3个
            for j in range(i + 1, len(nums) - 2):  # i被去掉了. 剩余可取的就少了2个了.
                now = nums[i] + nums[j]  # 一半的和,作为双指针两边的起点.
                p = j + 1  # 左边指针,从起始值+1开始
                q = len(nums) - 1  # 右边指针,从结束值-1开始
                while p < q:  # 指针较差为止.
                    if nums[p] + nums[q] + now == target:  # 组合和加和为目标值
                        if (nums[i], nums[j], nums[p], nums[q]) not in ans:  # 且不存在结果集合里
                            ans.add((nums[i], nums[j], nums[p], nums[q]))  # 加进结果集合
                    if nums[p] + nums[q] + now > target:  # 当前组合的加和大于目标值. 右边指针大了
                        q -= 1  # 右边指针-1
                    else:
                        p += 1  # 反之,左边指针+1 向中级靠拢,直到指针交叉,退出循环.

        return ans  # 返回结果.


ls = [1,2,3,4,5,6,7,8,9,10]
target = 25
ss = Solution()
print(ss.fourSum(ls,target))
