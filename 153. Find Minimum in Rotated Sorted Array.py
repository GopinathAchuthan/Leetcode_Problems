class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        else:
            left = 0
            right = len(nums)-1
            mid = (right+left+1) //2
            
            while(left<right):
                if nums[mid]<nums[mid-1] and nums[mid]<nums[mid]+1 or mid==right:
                    break
                    
                if nums[mid]>nums[left] or nums[mid]>nums[right]:
                    left = mid
                else:
                    right = mid
                    
                mid = (left+right+1)//2
                            
            return nums[mid]