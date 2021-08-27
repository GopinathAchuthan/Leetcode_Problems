class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.__helper(candidates, 0, target, [], res)
        return res
    
    def __helper(self, arr, i, target, slate, res):
        if target == 0: # base case
            res.append(list(slate))
            return
        elif target<0 or i == len(arr):  # backtracking condition
            return
        
        # include
        slate.append(arr[i])
        self.__helper(arr,i,target-arr[i],slate,res)
        slate.pop()
        
        # exclude
        self.__helper(arr, i+1, target, slate, res)