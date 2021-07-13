class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        mem = set()
        for num in nums:
            if num in mem:
                ans.add(num)
            mem.add(num)
        return list(ans)