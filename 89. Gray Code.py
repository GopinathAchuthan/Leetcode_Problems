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
        grey = ['0','1']
        
        if n>1:
            for _ in range(1,n):
                temp = []
                for i in range(len(grey)):
                    temp.append('0'+grey[i])
                for i in range(len(grey)):
                    temp.append('1'+grey[~i])
                grey = temp
        
        return [int(s,2) for s in grey]