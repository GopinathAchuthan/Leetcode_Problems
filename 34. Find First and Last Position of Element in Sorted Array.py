'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        left, right = 0, len(nums)-1
        ans1, ans2 = -1, -1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        ans1 = left
        
        # check whether the target is present or not
        if left==len(nums) or nums[left]!=target: 
            return [-1,-1]
        
        # left, right = 0, len(nums)-1
        right = len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid-1
        ans2 = right
        return [ans1, ans2]