# Time complexity: N!
# Space complexity: N
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.__helper(Counter(nums), len(nums), [], res)
        return res
    
    def __helper(self, mem, n, slate, res):
        # base case
        if n==0:
            res.append(list(slate))
            return
        
        for val in mem:
            if mem[val]>0:
                slate.append(val)
                mem[val]-=1
                self.__helper(mem, n-1, slate, res)
                mem[val]+=1
                slate.pop()