class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        N = len(nums)
        nums = [a*x*x+b*x+c for x in nums]
        heapq.heapify(nums)
        res = []
        for _ in range(N):
            res.append(heapq.heappop(nums))
        return  res