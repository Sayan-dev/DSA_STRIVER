from typing import List

class Sack:
    def __init__(self, value, weight, frac):
        self.value = value
        self.weight = weight
        self.frac = frac

class Solution:
    def fractional_knapsack(self, n, w, sack: List[Sack]):
        sorted_sacks = sorted(sack,key=lambda x:(x.frac,x.value), reverse=True)
        curr_weight = 0
        curr_price = 0
        for i in range(n):
            diff_left = w - curr_weight
            if diff_left==0:
                break

            if sorted_sacks[i].weight + curr_weight>w:
                curr_price = curr_price + sorted_sacks[i].frac * diff_left
                curr_weight = w
                continue
            curr_price = sorted_sacks[i].value + curr_price
            curr_weight = sorted_sacks[i].weight + curr_weight

        return curr_price



        
        

