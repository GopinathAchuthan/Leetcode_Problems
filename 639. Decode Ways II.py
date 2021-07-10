class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        if s[0] == '0':
            return 0
        
        prev = curr = 1
        if s[0] == '*':
            curr = 9
        
        for i in range(1,len(s)):
            if s[i] == '*':
                if s[i-1] not in {'1','2','*'}:
                    prev, curr = curr, curr*9%MOD
                elif s[i-1] == '1':
                    prev,curr = curr, (prev*9+curr*9)%MOD
                elif s[i-1] == '2':
                    prev,curr = curr, (prev*6+curr*9)%MOD
                else:
                    prev, curr = curr, (curr*9+prev*15)%MOD
            elif s[i] == '0':
                if s[i-1] in ['1','2']:
                    curr = prev
                elif s[i-1] == '*':
                    curr = (prev*2)%MOD
                else:
                    return 0
            elif s[i-1] == '*':
                if s[i] not in {'7','8','9'}:
                    prev,curr = curr, (curr+prev*2)%MOD
                else:
                    prev,curr = curr, prev+curr
            elif s[i-1] == '1' or s[i-1]=='2' and s[i] not in {'7','8','9'}:
                prev, curr = curr, (prev+curr)%MOD
            else:
                prev = curr
            
        return curr