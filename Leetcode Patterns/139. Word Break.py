'''
Topics: Dynamic Programming

Time Complexity: O(n^2)
Space Complexity: O(n)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        
        table = [False]*(n+1)
        
        # base case
        table[0] = True
        
        for end in range(1,n+1):
            for start in range(end):
                if table[start] and s[start:end] in words:
                    table[end] = True
        
        return table[n]