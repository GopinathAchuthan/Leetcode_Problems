'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
            curr += nums[i]
            ans[i] = curr
        
        return ans