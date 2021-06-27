class Solution:
    def maxScore(self, s: str) -> int:
        mem1 = [0]
        for char in s:
            if char == '0':
                mem1.append(mem1[-1])
            else:
                mem1.append(mem1[-1]+1)
        
        mem1.pop(0)
        score = 0
        for i in range(len(s)-1):
            num0 = i-mem1[i]+1
            num1 = mem1[-1]-mem1[i]
            if score<num0+num1:
                score = num0+num1
                
        return score