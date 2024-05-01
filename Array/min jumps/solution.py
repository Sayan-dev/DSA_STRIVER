class Solution:
    def minJumps(self, arr, n):
        maxJump = arr[0] # How much can we go with current jumps
        lastIndex = arr[0] # Lst index we can go using current jump

        jumps = 1

        if n == 1: return 0


        for i in range(1,n):
            if i>maxJump: return -1
            maxJump = max(maxJump, i + arr[i])

            if lastIndex > n-2 : return jumps

            if i == lastIndex:
                jumps+=1
                lastIndex = maxJump
                if lastIndex >= n-1:
                    return jumps
        
            
        
        return -1 