# Time Complexity: O(N*2^N)
# Space Complexity: O(N)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.__helper(word,0,[],res)
        return res
    
    def __helper(self,word,i,slate,res):
        # base case
        if i == len(word):
            res.append(''.join(slate))
            return
            
        if len(slate) == 0 or slate[-1].isalpha():
            for k in range(1,len(word)-i+1):
                slate.append(str(k))
                self.__helper(word,i+k,slate,res)
                slate.pop()
        slate.append(word[i])
        self.__helper(word,i+1,slate,res)
        slate.pop()