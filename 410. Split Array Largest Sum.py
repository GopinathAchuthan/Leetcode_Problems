'''
Time Complexity: O(n log D)
Space Complexity: O(1)

Topics: Array, Binary Search, Dynamic Programming
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = nums[0], 0
        
        for num in nums:
            left = max(left, num)
            right += num
        
        while left<=right:
            mid = left+(right-left)//2
            val = self.__getNumOfSplitPossible(nums,mid)
            if val>m:
                left = mid+1
            else:
                right = mid-1
            
        return left
    
    def __getNumOfSplitPossible(self,nums,limit):
        m = 1
        temp = 0
        for num in nums:
            temp += num
            if temp>limit:
                m+=1
                temp = num
        
        return m
                