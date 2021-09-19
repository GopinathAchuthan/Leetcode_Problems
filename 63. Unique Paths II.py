# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        
        # edge case
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        
        table = [[1]*n for _ in range(m)]
        
        # base case
        for i in range(1,m):
            table[i][0] = table[i-1][0] if obstacleGrid[i][0]==0 else 0
        for j in range(1,n):
            table[0][j] = table[0][j-1] if obstacleGrid[0][j]==0 else 0
        
        
        for r in range(1,m):
            for c in range(1,n):
                table[r][c] = table[r-1][c]+table[r][c-1] if obstacleGrid[r][c]==0 else 0
        
        return table[m-1][n-1]