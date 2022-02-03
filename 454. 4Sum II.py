class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mem = defaultdict(int)
        count = 0
        
        for n1 in nums1:
            for n2 in nums2:
                mem[n1+n2]+=1
        
        for n3 in nums3:
            for n4 in nums4:
                count += mem[-n3-n4]
        
        return count