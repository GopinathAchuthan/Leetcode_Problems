# DFS
class Solution:
    def island(self, grid, row, col):
        if grid[row][col] == '0':
            return
        grid[row][col] = '0'
        if col+1 < len(grid[row]):
            self.island(grid, row, col+1)
        if col-1 >= 0:
            self.island(grid, row, col-1)
        if row+1 < len(grid):
            self.island(grid, row+1, col)
        if row-1 >= 0:
            self.island(grid, row-1, col)
        return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # for i in range(len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.island(grid, i, j)
                    
        return count
        
# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    queue = deque()
                    queue.append((r,c))
                    while queue:
                        row,col = queue.popleft()
                        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr, nc = row+dr, col+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                                grid[nr][nc] = '0'
                                queue.append((nr,nc))
        return count