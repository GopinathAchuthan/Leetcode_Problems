import math

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A <= 1:
            return 0
        
        n = int(math.sqrt(A))+1
        
        for i in range(2,n):
            if A%i == 0:
                return 0
        
        return 1