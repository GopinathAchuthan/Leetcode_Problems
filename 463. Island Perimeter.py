class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        i = 0
        
        while i<len(grid):
            j = 0
            while j<len(grid[i]):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i>0:
                        perimeter -= grid[i-1][j]
                    if j>0:
                        perimeter -= grid[i][j-1]
                    if i<len(grid)-1:
                        perimeter -= grid[i+1][j]
                    if j<len(grid[i])-1:
                        perimeter -= grid[i][j+1]
                j+=1
            i+=1
        
        return perimeter