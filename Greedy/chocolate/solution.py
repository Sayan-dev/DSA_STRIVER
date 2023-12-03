import sys
from typing import List
from controller import Controller


class Solution:

    def chocolate_distribution(self,n:int,m:int, a:List[int]):
        # Write your code here
        sorted_a = sorted(a,key=None,reverse=True)
        diff = sys.maxsize
        maxim = 0
        minim = m -1
        while minim<=n-1:
            diff = min(sorted_a[maxim] - sorted_a[minim],diff)
            maxim +=1
            minim +=1

        return diff