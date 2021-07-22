class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        rev_min = [0]*N
        rev_min[-1] = nums[-1]
        for i in range(N-2,-1,-1):
            rev_min[i] = min(nums[i], rev_min[i+1])
        
        curr = nums[0]
        for i in range(1,N):
            if curr<=rev_min[i]:
                return i
            else:
                curr = max(curr, nums[i])
            
            