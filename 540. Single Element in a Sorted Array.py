'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = left+(right-left)//2
            
            if (mid%2==0 and mid+1<len(nums) and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                left = mid+1
            else:
                right = mid-1
            
        return nums[left]