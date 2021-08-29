# Time Complexity: O(M*N)
# Space Complexity: O(M*N)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m,n = len(heights), len(heights[0])
        pacific, atlantic = deque(), deque()
        
        for i in range(m):
            pacific.append([i,0])
            atlantic.append([i,n-1])
        for j in range(n):
            pacific.append([0,j])
            atlantic.append([m-1,j])
        
        set1 = self.__helperBFS(heights,m,n, pacific)
        set2 = self.__helperBFS(heights,m,n, atlantic)
        
        return set1.intersection(set2)
        
    def __helperBFS(self,heights,m,n,queue):
        res = set()
        for r,c in queue:
            res.add((r,c))
        
        while queue:
            row,col = queue.popleft()
            for r,c in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if r<0 or c<0 or r==m or c==n:
                    continue
                if (r,c) in res:
                    continue
                if heights[row][col]<=heights[r][c]:
                    res.add((r,c))
                    queue.append([r,c])
        return res
            