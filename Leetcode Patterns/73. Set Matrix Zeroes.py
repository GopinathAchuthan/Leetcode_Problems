# Time Complexity: O(N)
# Space Complexity: O(1)
# Topic: Array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0]*length
        ans[0] = 1
        
        for i in range(1,length):
            ans[i] = nums[i-1]*ans[i-1]
        
        right = 1
        for i in range(length-1,-1,-1):
            ans[i] = ans[i]*right
            right*=nums[i]
        
        return ans