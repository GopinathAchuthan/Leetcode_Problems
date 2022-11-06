'''
Time Complexity: O(n)
Space Complexity: O(n)

Topics: Array, Hashmap
'''
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ans = -1
        counts = Counter(nums)
        
        for num, count in counts.items():
            if count == 1:
                ans = max(ans, num)
        
        return ans