import sys
from typing import List



class Solution:


    def max_prod_subarray(self, n, caps: List[int]):
        maxim=-sys.maxsize
        pre = 1
        suff = 1
        for i in range(n):
            pre = pre * caps[i]
            if caps[i] == 0:
                pre = 1
            suff = suff * caps[n-i-1]
            if caps[n-i-1] == 0:
                suff = 1  
            maxim = max(pre,suff)

        return maxim




        
        

