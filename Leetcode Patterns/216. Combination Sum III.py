class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.__helper(k, n, 1, [], res)
        return res
    
    def __helper(self, k, n, i, slate, res):
        if k==0 and n==0:
            res.append(list(slate))
            return
        if k<=0 or i==10 or n<0:
            return

        # include
        slate.append(i)
        self.__helper(k-1, n-i, i+1, slate, res)
        slate.pop()
        
        # exclude
        self.__helper(k, n, i+1, slate, res)