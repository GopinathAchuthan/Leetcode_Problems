# Time Complexity: O(N*2^N)
# Space Complexity: O(N*2^N)

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.helper(s,0,'',res)
        return res
    
    def helper(self, s, i, slate, res):
        if i == len(s):
            res.append(slate)
            return
        if s[i].isalpha():
            self.helper(s,i+1, slate+s[i].lower(), res)
            self.helper(s,i+1, slate+s[i].upper(), res)
        else:
            self.helper(s,i+1, slate+s[i], res)