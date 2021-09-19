# Time Complexity: O(M*N)
# Space Complexity: O(N)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total%2==1:
            return False
        n = total//2
        dp = [False]*(n+1)
        dp[0] = True
        
        for num in nums:
            for i in range(n,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
                
        return dp[n]