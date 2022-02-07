# Solution 1:
"""
Topics: Array, Sorting, Hash Table

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        max_count = 0
        for val, count in Counter(nums).items():
            if count>max_count:
                max_count = count
                res = val
            
        return res

# Solution 2:
"""
Topics: Array, Voting Algorithm

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = -1
        count = 0
        for num in nums:
            if count==0:
                res = num
            count += 1 if num==res else -1
        
        return res