'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            d = abs(num) -1
            if nums[d]>0:
                nums[d]*=-1
        
        result = []
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        
        return result