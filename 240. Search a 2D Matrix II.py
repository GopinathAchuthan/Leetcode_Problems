'''
Time Complexity: O(m+n)
Space Complexity: O(1)

Topics: Array, Decrease & Conquer
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix),len(matrix[0])
        
        row, col = 0, n-1
        
        while row<m and col>=0:
            val = matrix[row][col]
            
            if target == val:
                return True
            elif target > val:
                row += 1
            else:
                col -= 1
        
        return False
                