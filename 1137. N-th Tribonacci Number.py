class Solution:
    def __init__(self):
        self.cache = {}
        self.cache[0] = 0
        self.cache[1] = 1
        self.cache[2] = 1
        
    def tribonacci(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.cache[n]