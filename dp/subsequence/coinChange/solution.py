import sys
from typing import List



class Solution:

    def total_coin_combo(self, n, sum, coins: List[int]):
        prev = curr = [0 for i in range(sum+1)]

        for i in range(sum+1):
            if i%coins[0] == 0:
                prev[i] = i / coins[0]
            else: prev[i] = 1e9

        for i in range(1, n):
            for s in range(sum+1):
                prev_sum = 0 + prev[s]
                curr_sum = sys.maxsize
                if coins[i]<=s:
                    curr_sum = 1 + curr[s-coins[i]]

                curr[s] = min(curr_sum,prev_sum)
            prev = curr 

        return prev[sum]



        
        

