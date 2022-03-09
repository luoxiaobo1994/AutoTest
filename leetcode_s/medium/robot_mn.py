# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/8 22:41

class Solution: # dp
    def uniquePaths(self , m , n ):
        # write code here
        dp = [1]*m # 每次只处理一行，故使用一维数组来记录即可，不需要二维
        for i in range(n-1):
            for j in range(m):
                if j == 0:
                    continue
                else:
                    dp[j] = dp[j-1]+dp[j]
        return dp[-1]


s = Solution()
print(s.uniquePaths(7, 4))