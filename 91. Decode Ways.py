class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        prev = curr = 1
        for i in range(1,len(s)):
            if s[i]=='0':
                if s[i-1] not in {'1','2'}:
                    return 0
                curr = prev
            elif s[i-1] == '1' or s[i-1] == '2' and s[i] in {'1','2','3','4','5','6'}:   
                prev, curr = curr, prev+curr
            else:
                prev = curr
            
        return curr