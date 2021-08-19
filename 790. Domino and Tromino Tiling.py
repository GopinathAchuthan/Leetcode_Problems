class Solution:
    def __init__(self):
        self.cache = {}
        self.cache[0] = 1
        self.cache[1] = 1
        self.cache[2] = 2
        
        self.MOD = (10**9) + 7
        
    def numTilings(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = (2*self.numTilings(n-1)+self.numTilings(n-3))%self.MOD
        
        return self.cache[n]