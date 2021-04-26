class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        text = text.split()
        lengthSpace = n - sum(map(lambda s:len(s), text))
        if len(text)>1:
            space, endSpace = divmod(lengthSpace, len(text)-1)
            res = text[0]
            for t in text[1:]:
                res+=' '*space
                res+=t
            res+=' '*endSpace
        else:
            res = text[0]+' '*lengthSpace
        
        return res
                
        