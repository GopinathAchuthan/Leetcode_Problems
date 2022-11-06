'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Prefix sum
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr, minValue = 0, float("inf")
        for num in nums:
            curr+=num
            minValue = min(minValue, curr)
        
        return abs(minValue)+1 if minValue<0 else 1