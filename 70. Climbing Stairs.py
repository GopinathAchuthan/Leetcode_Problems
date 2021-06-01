class Solution:
    def climbStairs(self, n: int) -> int:
        N = [1,1,2]
        if n>2:
            N.extend([0 for i in range(3,n+1)])
            for i in range(3,len(N)):
                N[i] = N[i-1] + N[i-2]
        
        return N[n]