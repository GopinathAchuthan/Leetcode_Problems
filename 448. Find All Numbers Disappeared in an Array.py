class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mem = set([i for i in range(1,n+1)])
        return list(mem-set(nums))