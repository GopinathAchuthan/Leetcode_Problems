# Method 1: Tabulation DP
# Time complexity: O(M*N)
# Space Complexity:O(min(M,N))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        if m<n:
            text1, text2 = text2, text1
            m,n = n,m
        
        table = [[0]*(n+1) for _ in range(2)]
        
        # Bottom-Up DP
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    table[i%2][j] = 1+table[(i-1)%2][j-1]
                else:
                    table[i%2][j] = max(table[(i-1)%2][j],table[i%2][j-1])
        
        return table[m%2][n]


# Method 2: Memoization DP
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        mem = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            mem[i][0] = 0
        for j in range(n+1):
            mem[0][j] = 0
        
        self.__lcs_helper(text1,m,text2,n,mem)
        return mem[m][n]
    
    def __lcs_helper(self, text1, i, text2, j, mem):
        if mem[i][j]==-1:
            if text1[i-1]==text2[j-1]:
                mem[i][j] = 1+self.__lcs_helper(text1,i-1,text2,j-1,mem)
            else:
                mem[i][j] = max(self.__lcs_helper(text1,i-1,text2,j,mem), self.__lcs_helper(text1,i,text2,j-1,mem))
        return mem[i][j]