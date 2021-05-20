class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        # first row
        for value in matrix[0]:
            ans+=value
        # first column
        for i in range(1,len(matrix)):
            ans+=matrix[i][0]
        # remaining
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
                ans+=matrix[i][j]
                
        return ans