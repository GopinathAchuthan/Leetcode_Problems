'''
Time Complexity: O(n)
Space Complexity: O(n)

Topic: Array
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        heap = []
        heapq.heapify(heap)
        
        k = 0
        while k<len(nums) and len(heap)!=3:
            if nums[k] not in seen:
                seen.add(nums[k])
                heapq.heappush(heap,nums[k])
        
            k+=1
        
        if len(heap)!=3:
            # return max(heap)
            return heap[-1]
        
        for i in range(k,len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                heapq.heappushpop(heap,nums[i])
        
        # return min(heap)
        return heap[0]