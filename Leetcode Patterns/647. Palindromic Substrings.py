'''
Topics: Dynamic Programming

Time Complexity: O(n^2)
Space Complexity: O(1)
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            ans += self.function(s,i,i,n)
            ans += self.function(s,i,i+1,n)
        
        return ans
    
    def function(self,s,left,right,n):
        count = 0
        while(left>=0 and right<n and s[left]==s[right]):
            count+=1
            left-=1
            right+=1
        return count