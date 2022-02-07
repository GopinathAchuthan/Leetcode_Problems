"""
Topics: Array, Matrix

Time Complexity: O(n**2)
Space Complexity: O(1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # diagonal flip
        for i in range(1,n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # vertical flip
        for i in range(n):
            for j in range(n//2):
                k = n-j-1
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
        
    