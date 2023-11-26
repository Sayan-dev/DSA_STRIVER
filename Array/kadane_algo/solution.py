class Solution: 
     
   
    def maxSubArraySum(self, nums: list[int]):
        
        maxCurr = maxTotal = nums[0]

        for i in range(1,len(nums)):
            maxCurr = max(nums[i], nums[i]+maxCurr)
            if maxCurr>maxTotal:
                maxTotal = maxCurr



        return maxTotal