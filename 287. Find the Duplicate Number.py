class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = set()
        for num in nums:
            if num in mem:
                return num
            mem.add(num)