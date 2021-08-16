class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    temp = 1
                    grid[r][c] = 0
                    queue = deque()
                    queue.append((r,c))
                    while queue:
                        row,col = queue.popleft()
                        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr, nc = row+dr, col+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                                temp+=1
                                grid[nr][nc] = 0
                                queue.append((nr,nc))
                    area = max(temp,area)
        return area