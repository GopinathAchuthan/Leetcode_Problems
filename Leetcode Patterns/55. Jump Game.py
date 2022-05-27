'''
Topics: Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        n = len(nums)-1
        for i in range(n+1):
            steps = max(steps,nums[i])
            if i+steps>=n:
                return True
            if steps==0:
                return False
            steps-=1
        return True