"""
Topics: Array, Hash Table

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        
        for i in range(len(nums)):
            d = target - nums[i]
            if d in mem:
                return [mem[d], i]
            mem[nums[i]] = i
        
        return [-1,-1]