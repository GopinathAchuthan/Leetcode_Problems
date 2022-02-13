'''
Topics: Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob_1(nums[:-1]), self.rob_1(nums[1:]))
    
    def rob_1(self, arr):
        state0 = state1 = 0
        for i in arr:
            state0, state1 = state1, max(state0+i, state1)
        return state1