# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mem = set([i for i in range(1,n+1)])
        return list(mem-set(nums))


# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            while(i+1 != nums[i]):
                d = nums[i]
                if nums[d-1]==d:
                    break
                nums[d-1] , nums[i] = nums[i], nums[d-1]
        
        for i in range(n):
            if i+1!=nums[i]:
                res.append(i+1)
        
        return res