# Solution 1:
class Solution:
    def grayCode(self, n: int) -> List[int]:
        grey = []
        for i in range(2**n):
            grey.append(i^i>>1)
        return grey

# Solution 2:
class Solution:
    def grayCode(self, n: int) -> List[int]:
        binary = ['0','1']
        
        for _ in range(1,n):
            binary = ['0'+b for b in binary] + ['1'+b for b in binary[::-1]]
        
        return [int(b,2) for b in binary]