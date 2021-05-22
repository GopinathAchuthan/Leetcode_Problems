class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [1,0]
        
        for i in s:
            if result[1]+widths[ord(i)-97]>100:
                result[0]+=1
                result[1]=widths[ord(i)-97]
            else:
                result[1]+=widths[ord(i)-97]
    
        return result