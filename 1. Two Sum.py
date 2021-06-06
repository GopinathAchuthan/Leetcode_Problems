class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        heap = {} # key -> (target-nums[i]): value -> i
        for i in range(len(nums)):
            if nums[i] in heap:
                return [heap[nums[i]],i]
            else:
                heap[target-nums[i]] = i