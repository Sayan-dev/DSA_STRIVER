import sys
from typing import List



class Solution:

    def rod_cutting(self, n, costs: List[int], sum):
        dp = [[0 for i in range(sum+1)] for j in range(n)]

        # total = self.cut(costs,n-1,sum, dp)
        for i in range(sum+1):
            dp[0][i]=i* costs[0]

        for i in range(n):
            for j in range(sum+1):
                not_take = 0 + dp[i-1][j]
                take = -sys.maxsize
                if i+1<=j:
                    take = costs[i] + dp[i][j-i-1]
                dp[i][j] = max(not_take,take)
        


        return dp[n-1][sum]



        
        

