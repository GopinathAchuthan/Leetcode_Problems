class Solution:
    def intToRoman(self, num: int) -> str:
        mem = {1:'I', 5:'V', 10:'X',
                50:'L', 100: 'C', 500: 'D', 
                1000: 'M'}
        place = 1
        out = []
        
        while(num!=0):
            digit = num%10
            if digit == 0:
                pass
            elif digit < 4:
                out.append(''.join([mem[place] for _ in range(digit)]))
            elif digit == 4:
                out.append(mem[place]+mem[5*place])
            elif digit < 9:
                out.append(str(mem[5*place])+"".join([mem[place] for _ in range(digit-5)]))
            else:
                out.append(mem[place]+mem[10*place])
            
            place *=10
            num//=10
                
        
        return ''.join(out[::-1])
        