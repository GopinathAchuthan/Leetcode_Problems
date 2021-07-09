class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [-10001]
        for num in nums:
            if mem[-1]<num:
                mem.append(num)
            else:
                idx = bisect.bisect_left(mem,num)
                mem[idx] = num
                
        return len(mem)-1