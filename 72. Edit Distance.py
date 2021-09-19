# Method 1: Recursive Method
'''
Time Complexity: O(M*N)
Space Complexity: O(M*N)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        self.__align(word1,m,word2,n,dp)
        return dp[m][n]
    
    def __align(self,word1,i,word2,j,dp):
        if dp[i][j]==-1:
            if word1[i-1]==word2[j-1]:
                dp[i][j] = self.__align(word1,i-1,word2,j-1,dp)
            else:
                dp[i][j] = 1+ min(self.__align(word1,i-1,word2,j-1,dp),
                                    self.__align(word1,i,word2,j-1,dp),
                                    self.__align(word1,i-1,word2,j,dp))
        return dp[i][j]

# Method 2: Iterative Method
'''
Time Complexity: O(M*N)
Space Complexity: O(min(M,N))
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)<len(word2):
            word1, word2 = word2, word1
        
        m,n = len(word1),len(word2)
        dp = [[j for j in range(n+1)] for _ in range(min(2,m+1))]
        
        for i in range(1,m+1):
            dp[i%2][0] = i
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i%2][j] = dp[(i-1)%2][j-1]
                else:
                    dp[i%2][j] = 1 + min(dp[(i-1)%2][j-1], dp[i%2][j-1], dp[(i-1)%2][j])
        return dp[m%2][n]