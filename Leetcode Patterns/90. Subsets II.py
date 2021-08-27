# Time Complexity: O(N*2^N)
# Space Complexity: O(N*2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.__helper(nums, [], 0, res)
        return res
    
    def __helper(self, arr, slate, i, res):
        if i == len(arr):
            res.append(list(slate))
        else:
            # exclude
            k = i+1
            while(k<len(arr) and arr[i]==arr[k]):
                k+=1
            self.__helper(arr, slate, k, res)
            
            # include
            slate.append(arr[i])
            self.__helper(arr, slate, i+1, res)
            slate.pop()
        return          