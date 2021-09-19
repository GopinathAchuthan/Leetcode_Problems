# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        a,b,c = nums[0],nums[1],nums[0]+nums[2]
        for i in range(3,len(nums)):
            a,b,c = b,c,nums[i]+max(a,b)
        return max(b,c)