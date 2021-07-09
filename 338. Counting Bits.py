class Solution:
    def countBits(self, n: int) -> List[int]:
        mem = [0]
        for i in range(1,n+1):
            mem.append(mem[i&(i-1)]+1)
        
        return mem