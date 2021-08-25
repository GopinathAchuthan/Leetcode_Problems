# Method 1
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

# Method 2
class Solution:
    def generateSubsets(self, subsets, curr_subset, index, nums):
        subsets.append(curr_subset)
        for i in range(index, len(nums)):
            if index!=i and nums[i-1]==nums[i]:
                continue
            curr_subset.append(nums[i])
            self.generateSubsets(subsets, curr_subset[:], i+1, nums)
            curr_subset.pop()
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr_subset = []
        nums.sort()     
        self.generateSubsets(subsets, curr_subset, 0, nums)
        return subsets