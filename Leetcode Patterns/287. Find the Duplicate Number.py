"""
Topics: Array, Cycle Sort, Floyd's Cycle Detection

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while nums[i]!=i+1:
                d = nums[i]
                
                if nums[d-1]==d:
                    return d
                
                nums[i], nums[d-1] = nums[d-1], nums[i]
        
        return -1