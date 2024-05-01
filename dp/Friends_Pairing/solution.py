from typing import List
import math

class Solution:

    def find_pairs(self, n):
        dp = [i for i in range(n+1)]

        for i in range(n+1):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + (i-1)*dp[i-2]



        
        return dp[n]


        
        

