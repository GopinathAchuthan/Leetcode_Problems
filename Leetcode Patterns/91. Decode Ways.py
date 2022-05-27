'''
Topics: Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        valid2DigitStr = set()
        for i in range(10,27):
            valid2DigitStr.add(str(i))
        
        state0 = state1 = state2 = 0
        
        if s[0]=='0':
            return 0
        else:
            state0 = state1 = 1
        
        for i in range(1,len(s)):
            if s[i]!='0':
                state2 += state1
            if s[max(0,i-1):i+1] in valid2DigitStr:
                state2 += state0
            state0,state1,state2 = state1,state2,0
        
        return state1