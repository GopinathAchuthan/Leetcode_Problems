class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.__helper(nums, 0, res)
        return res
    
    def __helper(self, slate, i, res):
        if i == len(slate)-1:
            res.append(list(slate))
        else:
            for k in range(i, len(slate)):
                slate[i], slate[k] = slate[k], slate[i]
                self.__helper(slate, i+1, res)
                slate[i], slate[k] = slate[k], slate[i]