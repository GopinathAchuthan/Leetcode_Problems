# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        return max(self.__helper(nums,0,len(nums)-1), self.__helper(nums,1,len(nums)))
    def __helper(self,nums,start,end):
        a,b,c = 0,0,nums[start]
        for i in range(start+1,end):
            a,b,c = b,c,nums[i]+max(a,b)
        return max(b,c)