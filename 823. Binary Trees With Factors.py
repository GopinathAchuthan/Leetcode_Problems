class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9+7
        arr.sort()
        dp = dict.fromkeys(arr,1)
        
        for root in arr:
            for left in arr:
                if root%left == 0:
                    right = root/left
                    if right in arr:
                        dp[root]+=dp[right]*dp[left]
                        dp[root] %= mod

        return sum(dp.values())%mod