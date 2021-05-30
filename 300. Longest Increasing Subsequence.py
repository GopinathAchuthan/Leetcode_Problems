class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and L[j]>L[i]:
                    L[i] = L[j]
            L[i]+=1
            
        return max(L)
                    