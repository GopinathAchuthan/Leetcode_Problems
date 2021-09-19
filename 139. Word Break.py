# Time Complexity: O(N*N) (without considering substring computation)
# Time Complexity: O(N^3)
# Space Complexity: O(N)

# Method 1: Iteration
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


# Method 2: Recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        return self.__helper(s,0,len(s)-1,set(wordDict),dp)
    
    def __helper(self, arr, start, end, words,dp):
        if start>end:
            return True
        if start in dp:
            return dp[start]
        dp[start] = False
        for i in range(start,end+1):
            if arr[start:i+1] in words:
                if self.__helper(arr,i+1,end,words,dp):
                    dp[start] = True
                    break
                else:
                    dp[i+1] = False
            
        return dp[start]
        