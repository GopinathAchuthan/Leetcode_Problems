'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Prefix Sum
'''
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        curr, ans = 0, 0
        total = 0
        for num in nums:
            total+=num
        for k in range(len(nums)-1):
            curr += nums[k]
            if curr>=total-curr:
                ans += 1
        
        return ans
        