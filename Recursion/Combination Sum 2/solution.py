class Solution:
    answer=[]
    def outputSum(self,candidates,current: list[int],index:int,target:int):

        if target == 0:
            self.answer.append(current.copy())

        if target <= 0:
            return
        

        prev = -1

        for i in range(index,len(candidates)):
            if candidates[i] == prev:
                continue
            current.append(candidates[i])
            self.outputSum(candidates,current,i+1,target-candidates[i])
            current.pop()
            prev = candidates[i]
    
    
 

        
    

    def combisum2(self, candidates: list[int], target:int):
        # Write your code here

        # Sort array
        # Skip an index once you have done it
        # Return when sum exceeds target 

        candidates.sort()
        self.outputSum(candidates,[],0,target)



        return self.answer