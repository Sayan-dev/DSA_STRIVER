class Solution:

    def maximumPath(self, n, M):
        memo = [[-1 for i in range(n)]for j in range(n)]
        def add(r,c, M):
            if r>n-1:return 0
            if c>n-1:return 0
            if r<0:return 0
            if c<0:return 0

            if r==0: return M[0][c]

            if memo[r][c] == -1:
                memo[r][c] =  M[r][c] + max(add(r-1, c-1, M),add(r-1, c, M), add(r-1, c+1, M))


            return memo[r][c]

        max_sum = 0
        for c in range(n):
            max_sum = max(max_sum, add(n-1,c,M))
        
        return max_sum



        
        

