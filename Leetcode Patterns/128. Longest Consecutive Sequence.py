'''
Topics: Array, Hash Table

Time Complexity O(n)
Space Complexity: O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num-1 not in nums_set:
                count = 0
                while num in nums_set:
                    count += 1
                    num += 1
                ans = max(ans,count)
        
        return ans