class Solution:
    def makeGood(self, s: str) -> str:
        s = [val for val in s]
        ptr = 0
        while(ptr<len(s)-1):
            if (s[ptr].isupper() and s[ptr+1].islower() or s[ptr].islower() and s[ptr+1].isupper()) and s[ptr].lower() == s[ptr+1].lower():
                s.pop(ptr)
                s.pop(ptr)
                if ptr > 0:
                    ptr-=1
            else:
                ptr+=1
        return "".join(s)