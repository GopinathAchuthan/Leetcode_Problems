# Solution 1:
'''
Topics: Array, Hash Table

Time Complexity: O(mn)
Space Complexity: O(1)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        isCol = False
        for i in range(m):
            if matrix[i][0]==0:
                isCol = True
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if (matrix[i][0]==0) or (matrix[0][j]==0):
                    matrix[i][j] = 0
        
        # check whether first row is need to change to zero
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j] = 0
        
        if isCol:
            for i in range(m):
                matrix[i][0] = 0

# Solution 2:
'''
Topics: Array, Hash Table

Time Complexity: O(mn)
Space Complexity: O(m+n)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        