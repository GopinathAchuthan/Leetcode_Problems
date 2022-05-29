#Solution 1:
'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start, end = -1,-1
        left, right = 0, n-1
        
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        start = left
        
        if start==n or nums[start]!=target:
            return False
        
        left, right = 0,n-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        end = left
        
        return True if (end-start)>(n//2) else False

#Solution 2:
'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        # base case
        if n==0 or nums[n//2]!=target:
            return False
        
        start, end = -1,-1
        left, right = 0, n-1
        
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        start = left
        
        if start==n or nums[start]!=target:
            return False
        
        end = start+(n//2)
        
        return end<n and nums[end]==target