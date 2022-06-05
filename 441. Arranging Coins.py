'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0,n
        
        while left<=right:
            mid = left+(right-left)//2
            val = (mid*(mid+1))//2
            if n<val:
                right = mid-1
            else:
                left = mid+1
        
        return right