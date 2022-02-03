# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Note: nums may contains duplicate numbers
        n = len(nums)
        
        for i in range(n):
            while(nums[i]!=i+1):
                d = nums[i]
                if d<1 or d>n or nums[d-1]==d:
                    break
                nums[i], nums[d-1] = nums[d-1], nums[i]
        
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        
        return n+1