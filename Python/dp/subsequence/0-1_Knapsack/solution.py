import sys
from typing import List

class Solution:
    def zeroOneknapSack(self, n, W, v: List[int],w:List[int]):
        dp = [[0 for j in range(W+1)] for i in range(n)]

        for i in range(w[0],W):
            dp[0][i] = v[0]

        for i  in range(1,n):
            for j in range(W+1):

                prev = 0 + dp[i-1][j]
                curr = -sys.maxsize
                if w[i]<=j:
                    curr = v[i]+dp[i-1][W-w[i]]
                
                dp[i][j] = max(prev, curr)

        return dp[n-1][W]



        
        

