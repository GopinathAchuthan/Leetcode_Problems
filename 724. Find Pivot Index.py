'''
Time Complexity: O(n)
Space Complexity: O(1)

Topic: Array, Prefix Sum
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum = 0
        for i in range(0,len(nums)):
            if leftSum == total-leftSum-nums[i]:
                return i
            leftSum += nums[i]
            
        return -1