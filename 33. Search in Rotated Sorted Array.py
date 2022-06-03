# Method 1 is better for this problem
# Method 1:
'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: find minimum/maximum element first
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>nums[-1]:
                left = mid+1
            else:
                right = mid-1
        min_value_index = left
        
        # Step 2: narrow down the possible range where the target be there
        if target<=nums[-1]:
            left = min_value_index
            right = len(nums)-1
        else:
            left = 0
            right = min_value_index-1
            
        # Step 3: do binary search to search the target and return the target's index
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        
        return -1
        
# Method 2:
'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        """
        For our understanding, let's consider elements greater than nums[-1] as             green zone. Remining elements are in red zone.
        Eg: GGGGGRRRRRRRRRRRR
        """
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[-1]:
                # red zone
                if target>nums[-1]:
                    # if target in green zone
                    right = mid-1     
                else:
                    # if target in red zone
                    if nums[mid]<target:
                        left = mid+1
                    else:
                        right = mid-1
                    
            else:
                # green zone
                if target<=nums[-1]:
                    # if target in red zone
                    left = mid+1
                else:
                    # if target in green zone
                    if nums[mid]<target:
                        left = mid+1
                    else:
                        right = mid-1
        return -1
                        