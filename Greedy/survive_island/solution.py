import sys
import math
from controller import Controller


class Solution:

    def survive_island(self,S:int, N: int, M:int):
        # Write your code here
        total = S*M
        if N<M:
            return f'No' 
        
        days = math.ceil(total / N)







        return f'Yes {days}'