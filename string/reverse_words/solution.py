from typing import List
import math

class Solution:

    def find_pairs(self, s:str):
        new_s = s.split(" ")
        answer = []
        for i in range(len(new_s)-1,-1,-1): 

            if new_s[i] != '':
                answer.append(new_s[i]) 

        
        return " ".join(answer)


        
        

