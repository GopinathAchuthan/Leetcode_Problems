'''
Topics: Array, Recursion, Backtracking, Enumeration

Time Complexity: O(n*2^n)
Call Stack Space: O(n)
Auxiliary Space: O(n)
Space Complexity: O(n)
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.func(sorted(nums),0,len(nums),[],res)
        return res
    
    def func(self, nums, i, n, slate, res):
        # base case
        if i==n:
            res.append(list(slate))
            return
        
        # resursive calls
        # exclude nums[i]
        k=i+1
        while k<n and nums[i] == nums[k]:
            k+=1
        self.func(nums, k, n, slate, res)
        
        # include nums[i]
        slate.append(nums[i])
        self.func(nums, i+1, n, slate, res)
        slate.pop()
        
        return