'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Sliding window
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # edge case
        if k==0:    
            return 0
        
        left, prod, ans = 0, 1, 0

        for right in range(len(nums)):
            prod *= nums[right]
            while left<=right and prod>=k:
                prod//=nums[left]
                left+=1
            ans += right-left+1
        
        return ans