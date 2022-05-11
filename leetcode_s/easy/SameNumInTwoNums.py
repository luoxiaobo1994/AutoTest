# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/11 16:11
# Desc:从两个数组里,找出都存在的数字.--> 求交集.


class Solution():

    def intersect(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()  # 排序了,有序数组.
        nums2.sort()
        i = 0
        j = 0
        l = []
        while ((i < len1) and (j < len2)):
            if (nums1[i] == nums2[j]):  # 当前两个指针指向的数值相同
                l.append(nums1[i])  # 符合要求,记录
                i += 1
                j += 1
            elif (nums1[i] > nums2[j]):  # 当前指向位置的两个数对比.
                j += 1  # 数值较大的指针,暂时不动.数值小的指针往后移.
            elif (nums1[i] < nums2[j]):
                i += 1  # 因为:小的后面,可能和大的相等,大的后面,可没有比当前还小的了.
        return l


print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
