# Time Complexity: O(k*Comb(n,k))
# Recursive Stack: O(k)
# Output Size: O(Comb(n,k))
# Maximum slate size: O(k)
# Space Complexity: O(k + Comb(n,k) + k) --> O(Comb(n,k))
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.__helper(1,n,k,[],res)
        return res
    
    def __helper(self, start, end, k, slate, res):
        if k == 0:
            res.append(list(slate))     # O(k)
            return
        for i in range(start, end-k+2):
            slate.append(i)
            self.__helper(i+1,end,k-1,slate,res)
            slate.pop()