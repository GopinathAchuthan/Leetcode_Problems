class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set(nums)
        return len(mem)!=len(nums)