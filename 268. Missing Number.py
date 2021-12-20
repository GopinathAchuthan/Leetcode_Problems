# Time Complexity: O(N)
# Space Complexity: O(1)

# Method 1: Mathematics answer
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)

# Time Complexity: O(N)
# Space Complexity: O(1)

# Method 2: Cycle Sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while(i!=nums[i] and nums[i]!=n):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(n):
            if nums[i]!=i:
                return i
            
        return n
