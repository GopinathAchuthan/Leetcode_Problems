class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = temp = float('-inf')
        for num in nums:
            temp = max(temp+num,num)
            ans = max(ans,temp)
        
        return ans