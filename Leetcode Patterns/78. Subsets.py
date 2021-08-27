# Time Complexity: O(N*2^N)
# Space Complexity: O(N*2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for val in nums:
            out+=[gen+[val] for gen in out]
        return out
                