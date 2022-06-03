'''
Time Complexity: O(n)
Space Complexity: O(1)

Best Case Time Complexity: O(log n)
Worst Case Time Complexity: O(n)

Topic: Binary Search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # base case
        if len(nums)==0:
            return False
        
        # edge case
        if nums[0]==target or nums[-1]==target:
            return True
        
        # if elements in leftmost is same as rightmost element of nums
        left, right = 0, len(nums)-1
        
        while left<=right and nums[left]==nums[right]:
            left+=1
        
        # let's us assume the region where the elements are greater than
        # nums[-1] as green region. And other region as brown region
        # Eg., GGGGGGGGGBBBBBBBBBBBBBBBBBB
        
        # now, search for target in nums
        target_region = 'green' if target>nums[-1] else 'brown'
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            
            if nums[mid]>nums[-1]:
                # nums[mid] is in green region
                if target_region=='brown' or nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                # nums[mid] is in brown region
                if target_region=='green' or nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1   
        
        # return false if the target is not present in nums
        return False