import sys
from typing import List



class Solution:

    def rod_cutting(self, n, costs: List[int], sum):
        prev = curr = [0 for i in range(sum+1)]
        

        # total = self.cut(costs,n-1,sum, dp)
        for i in range(sum+1):
            prev[i]=i* costs[0]

        for i in range(n):
            for j in range(sum+1):
                not_take = 0 + prev[j]
                take = -sys.maxsize
                if i+1<=j:
                    take = costs[i] + curr[j-i-1]
                curr[j] = max(not_take,take)
            prev = curr
        


        return prev[sum]



        
        

