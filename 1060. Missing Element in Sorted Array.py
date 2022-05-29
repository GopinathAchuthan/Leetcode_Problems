'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        first = nums[0]
        while left<=right:
            mid = left+(right-left)//2
            
            if nums[mid]-first-mid<k:
                left = mid+1
            else:
                right = mid-1
        
        return k+first+right