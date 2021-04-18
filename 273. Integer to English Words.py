import re

class Solution:
    def numberToWords(self, num: int) -> str:
        
        # base case
        if num == 0:
            return 'Zero'
        
        # other cases
        ones = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
        tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        teens = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',14:'Fourteen',15:'Fifteen', 
                 16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
        counter = {0:'', 1:'Thousand', 2:'Million', 3:'Billion'}
        
        count = 0
        res = ''
        while num != 0:
            temp = num%1000
            num//=1000
            if temp != 0:
                res = counter[count]+' '+res
                
            # handling three digits
            temp2 = temp%100
            temp//=100
            if temp2 < 10:
                res = ones[temp2]+' '+res
            elif temp2 < 20:
                res = teens[temp2]+' '+res
            else:
                res = tens[temp2//10]+' '+ones[temp2%10]+' '+res
            
            if temp > 0:
                res = ones[temp]+' Hundred '+res
            
            count += 1
        
        return re.sub("\s\s+" , " ", res.strip())