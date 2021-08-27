# Time Complexity: O(2^N)
# Space Complexity: O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.__helper(candidates, 0, target, [], res)
        return res
    
    def __helper(self, arr, i, target, slate, res):
        if target == 0:
            res.append(list(slate))
            return
        elif target<0 or i == len(arr) or arr[i]>target:
            return
        
        # include
        slate.append(arr[i])
        self.__helper(arr, i+1, target-arr[i], slate, res)
        slate.pop()
        
        # exclude
        k = i
        while(k<len(arr) and arr[i]==arr[k]):
            k+=1
        self.__helper(arr, k, target, slate, res)