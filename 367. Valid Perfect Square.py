'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right = 1, num
        
        while left<=right:
            mid = left+(right-left)//2
            val = mid*mid
            if val==num:
                return True
            elif val<num:
                left = mid+1
            else:
                right = mid-1
        
        return False
            