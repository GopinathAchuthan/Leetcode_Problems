'''
Time Complexity: O(m)
Space Complexity: O(1)

Topics: Array, Two Pointers
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j  = 0, 0
        n = len(s)
        m = len(t)
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
            j+=1
        
        return i==n