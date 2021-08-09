class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2)>len(num1):
            num1, num2 = num2, num1
        
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        carry = 0
        idx = 0
        while(idx<len(num2)):
            val = carry+int(num1[idx])+int(num2[idx])
            num1[idx] = str(val%10)
            carry, idx = val//10, idx+1
        
        while(carry!=0 and idx<len(num1)):
            val = carry+int(num1[idx])
            num1[idx] = str(val%10)
            carry, idx = val//10, idx+1
        
        while(carry!=0):
            num1.append(str(carry%10))
            carry//=10

        return ''.join(num1[::-1])
        