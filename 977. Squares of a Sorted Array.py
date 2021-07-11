class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [num*num for num in nums]
        ans = [0]*n
        left, right = 0,n-1
        for i in range(n-1, -1, -1):
            if nums[left]>=nums[right]:
                ans[i] = nums[left]
                left+=1
            else:
                ans[i] = nums[right]
                right-=1
        return ans