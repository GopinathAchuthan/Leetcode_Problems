# Time Complexity: O(N)
# Space Complexity: O(1)
# Method 1: Mathematics answer
# In this method there is a possibility of integer overflow.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)


'''
Time Complexity: O(n)
Space Complexity O(1)

Topics: Array, Hashmap, Cycle sort, Math
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return list(set(range(len(nums)+1)) - set(nums))[0]
        # return len(nums)*(len(nums)+1)//2 - sum(nums)
        
        n = len(nums)
        for i in range(n):
            while nums[i]!=n and nums[i]!=i:
                d = nums[i]
                nums[d], nums[i] = nums[i], nums[d]
            
        
        for i in range(n):
            if i!=nums[i]:
                return i