'''
Topics: Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        state0 = state1 = 0
        
        for num in nums:
            state0, state1 = state1, max(state0+num, state1)
        
        return state1