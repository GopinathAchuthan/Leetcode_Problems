'''
Topics: Strings

Time Complexity: O(n+m)
Space Complexity: O(1)
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i , j  = len(s)-1, len(t)-1
        skip_i = skip_j = 0
        
        while i>=0 or j >=0:
            while i>=0:
                if s[i]=='#':   skip_i, i = skip_i+1, i-1
                elif skip_i>0:  skip_i, i = skip_i-1, i-1
                else:           break
            
            while j>=0:
                if t[j]=='#':   skip_j, j = skip_j+1, j-1
                elif skip_j>0:  skip_j, j = skip_j-1, j-1
                else:           break
            
            if i>=0 and j>=0 and s[i] != t[j]:
                return False
            if (i>=0) != (j>=0):
                return False

            i, j = i-1, j-1
            
        return True