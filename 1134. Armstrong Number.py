class Solution:
    def __init__(self):
        self.k_power = {}
        
        for i in range(10):
            self.k_power[i]={}
            self.k_power[i][1] = i
        for i in range(10):
            for j in range(2,9):
                self.k_power[i][j] = self.k_power[i][j-1]*i
        
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        
        temp = n
        num = 0
        while(temp!=0):
            num += self.k_power[temp%10][k]
            temp //= 10
        
        if num == n:
            return True
        else:
            return False
        