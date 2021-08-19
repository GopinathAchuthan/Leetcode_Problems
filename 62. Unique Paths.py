class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<n: m,n = n,m
        mem = [[i]*(n+1) for i in range(2)]
        mem[1][0] = 0
        
        for i in range(2,m+1):
            for j in range(1,n+1):
                mem[i%2][j] = mem[(i-1)%2][j]+mem[i%2][j-1]
        return mem[m%2][n]
        