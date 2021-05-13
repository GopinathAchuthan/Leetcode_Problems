class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # first row
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        # first column    
        for i in range(1,len(grid)):
            grid[i][0] += grid[i-1][0]
        # remaining cell
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
        
        return grid[-1][-1]