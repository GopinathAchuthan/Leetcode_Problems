class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        temp = 1
        
        while(n>temp):
            temp <<=2
        
        if temp == n:
            return True
        
        return False