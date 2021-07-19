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