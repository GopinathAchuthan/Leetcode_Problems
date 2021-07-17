class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [False]*m
        cols = [False]*n
        for row,col in indices:
            rows[row]^=True
            cols[col]^=True
        
        return sum(row^col for row in rows for col in cols)
        