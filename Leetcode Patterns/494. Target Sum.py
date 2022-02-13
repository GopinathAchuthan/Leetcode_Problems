'''
Topics: Dynamic Programming

Time Complexity: O(n*m)
Space Complexity: O(n*m)
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs_func(idx,target):
            if (idx,target) in mem:
                return mem[(idx,target)]
            
            # base case
            if idx==0:
                return 0
                
            mem[(idx,target)] = dfs_func(idx-1,target-nums[idx]) + dfs_func(idx-1,target+nums[idx])
            return mem[(idx,target)]
        
        mem = dict()
        if nums[0]!=0:
            mem[(0,nums[0])] = 1
            mem[(0,-nums[0])] = 1
        else:
            mem[(0,0)] = 2
        
        return dfs_func(len(nums)-1,target)