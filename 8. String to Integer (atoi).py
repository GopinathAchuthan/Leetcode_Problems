class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        firstCharOccur = False
        sign = 1
        
        for val in s:
            if not firstCharOccur:
                if val == ' ':
                    continue
                elif val == '+' or val == '-' or ord(val)>=48 and ord(val)<=57:
                    firstCharOccur = True
                    if val == '-':
                        sign = -1
                    elif val == '+':
                        continue
                    else:
                        ans=ord(val)-48
                        
                else:
                    break
            else:
                if ord(val)>=48 and ord(val)<=57:
                    ans*=10
                    ans+=ord(val)-48
                else:
                    break
        
        if sign*ans<-2**31:
            return -2**31
        elif sign*ans>2**31 - 1:
            return 2**31-1
        else:
            return sign*ans