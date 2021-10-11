class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        
        mem = dict()
        mem[0] = 1
        count, total = 0, 0
        
        for num in nums:
            total += num
            if total-k in mem:
                count += mem[total-k]
            mem[total] = mem.get(total, 0)+1
        
        return count