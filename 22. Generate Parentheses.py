class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.__helper(n,n,[],res)
        return res
    def __helper(self, openP, closeP, slate, res):
        if openP==0 and closeP ==0:
            res.append(''.join(slate))
            return
        if openP>0:
            slate.append('(')
            self.__helper(openP-1,closeP,slate, res)
            slate.pop()
        if openP<closeP:
            slate.append(')')
            self.__helper(openP,closeP-1,slate, res)
            slate.pop()x    