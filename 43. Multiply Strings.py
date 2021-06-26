class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2=='0':
            return '0'
        
        if len(num2)<len(num1):
            num1, num2 = num2, num1 
        
        num1, num2 = num1[::-1], num2[::-1]
        
        out = ['0' for _ in range(len(num1)+len(num2))]
        
        for i in range(len(num1)):
            ptr = i
            carry = 0
            for j in range(len(num2)):
                mul = int(num1[i])*int(num2[j])
                mul += int(out[ptr])+carry
                carry = mul//10
                out[ptr] = str(mul%10)
                ptr+=1
            while(carry):
                temp = carry+int(out[ptr])
                out[ptr] = str(temp%10)
                carry = temp//10
                ptr+=1
                
        out = out[::-1] # reverse the output
        ptr = 0
        while(out[ptr]=='0'):   
            ptr+=1
        
        return ''.join(out[ptr:])   # removing leading zero and returning output