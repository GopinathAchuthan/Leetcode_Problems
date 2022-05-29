'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0,row*col-1
        
        while left<=right:
            mid = left+(right-left)//2
            r,c = mid//col, mid%col
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                left = mid+1
            else:
                right = mid-1
        return False