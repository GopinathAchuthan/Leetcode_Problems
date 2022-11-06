'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Sliding window
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total, ans = 0, 0
        
        for i in range(k):
            total += nums[i]
            
        ans = total
        
        for i in range(k,len(nums)):
            total += nums[i]-nums[i-k]
            ans = max(ans, total)
        
        return ans/k