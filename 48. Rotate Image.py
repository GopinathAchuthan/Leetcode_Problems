class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N//2):
            for j in range(N):
                matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]
        for i in range(N-1):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        