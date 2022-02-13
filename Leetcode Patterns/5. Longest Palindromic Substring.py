'''
Topics: Dynamic Programming

Time Complexity: O(n^2)
Space Complexity: O(1)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def spreadFromCenter(left,right,n):
            while(left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
            return left+1,right
        
        n = len(s)
        l,r = 0,1
        
        for i in range(len(s)):
            l1,r1 = spreadFromCenter(i,i,n)
            l2,r2 = spreadFromCenter(i,i+1,n)
            if r-l<r1-l1:
                l,r = l1,r1
            if r-l<r2-l2:
                l,r = l2,r2
        
        return s[l:r]