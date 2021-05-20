class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n-1
        
        def isNoZeroInteger(num: int) -> bool:
            while(num!=0):
                temp = num%10
                num//=10
                if temp == 0:
                    return False
            return True
            
        
        for i in range(1,n):
            a = i
            b = n-i
            if isNoZeroInteger(a) and isNoZeroInteger(b):
                break
        
        
        return [a,b]