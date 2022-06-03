'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()   
        left, right = 0, n-1
        peak = -1
        
        # find peak element index
        while left<=right:
            mid = left+(right-left)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                left = mid+1
            else:
                right = mid-1
        peak = left
        
        # find target index from left part of mountain array if available
        # search target in ascending zone
        left, right = 0, peak
        while left<=right:
            mid = left+(right-left)//2
            value = mountain_arr.get(mid)
            if value==target:
                return mid
            elif value<target:
                left = mid+1
            else:
                right = mid-1
        
        # if target is not available in left part of mountain array, search the target index in the right part.
        # search target in decending zone
        left, right = peak-1, n-1
        while left<=right:
            mid = left+(right-left)//2
            value = mountain_arr.get(mid)
            if value==target:
                return mid
            elif value<target:
                right = mid-1
            else:
                left = mid+1
        
        # if the target is not present, returning -1.
        return -1