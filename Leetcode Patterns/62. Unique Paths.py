'''
Topics: Dynamic Programming

Time Complexity: O(mn)
Space Complexity: O(min(m,n))
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<n:
            m,n = n,m
        
        table = [[0]*n for _ in range(min(2,m))]
        
        # base case
        ## fill the first column with value 1
        for j in range(n):
            table[0][j] = 1
        ## fill the first row with value 1
        for i in range(min(2,m)):
            table[i][0] = 1
        
        # computing the unique paths
        for i in range(1,m):
            for j in range(1,n):
                table[i%2][j] = table[(i-1)%2][j]+table[i%2][j-1]
        
        # return the bottom-right corner value
        return table[(m-1)%2][n-1]