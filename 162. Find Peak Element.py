class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N-1
        
        while(left<right):
            mid = left+(right-left)//2
            if mid+1 <N and nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left