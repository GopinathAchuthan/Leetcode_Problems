# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1,n
        
        while start<=end:
            mid = start+(end-start)//2
            if isBadVersion(mid):
                end = mid-1
            else:
                start = mid+1
        return start