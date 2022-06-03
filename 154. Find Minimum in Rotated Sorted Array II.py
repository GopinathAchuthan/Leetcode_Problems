'''
Time Complexity: O(n)
                 Worst Case - O(n)
                 Best Case - O(log n)
Space Complexity: O(1)

Topic: Two Pointer, Binary Search
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        # two pointer
        ## if left and right elements are same, 
        ## we can reduce the size to remove duplicate elements.
        ## So that we can perform binary search to find minimum value.
        while left<right and nums[0]==nums[left]==nums[right]:
            left+=1
            right-=1
        
        # binary search
        k = nums[right]
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>k:
                left = mid+1
            else:
                right = mid-1
        
        return min(nums[0],nums[left])