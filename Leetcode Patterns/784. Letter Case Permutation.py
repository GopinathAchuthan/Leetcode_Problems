'''
Topics: Enumneration

Time Complexity: O(n*2^n)
Space Complexity: O(n)
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        self.dfs(s,0,n,list(s), res)
        return res
    
    def dfs(self, s, i, n, slate, res):
        # base case
        if i==n:
            res.append("".join(slate))
            return
        
        # recursive calls
        if s[i].isnumeric():
            self.dfs(s,i+1,n,slate,res)
        else:
            slate[i] = s[i].lower()
            self.dfs(s,i+1,n,slate,res)
            slate[i] = s[i].upper()
            self.dfs(s,i+1,n,slate,res)
        return