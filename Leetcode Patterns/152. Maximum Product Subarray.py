'''
Topics: Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -10
        currProd = 1
        negProd = 1
        
        for num in nums:
            currProd, negProd = max(num, currProd*num, negProd*num), min(num, negProd*num, currProd*num)
            maxProd = max(maxProd, currProd)
        return maxProd