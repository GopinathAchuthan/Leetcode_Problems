'''
Time Complexity: O(log x)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        
        while left<=right:
            mid_value = left+(right-left)//2
            if mid_value*mid_value<=x:
                left = mid_value+1
            else:
                right = mid_value-1
        
        return right