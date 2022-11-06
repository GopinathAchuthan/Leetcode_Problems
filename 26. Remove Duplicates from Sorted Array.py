'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        k = 1
        for i in range(1,len(nums)):
            if temp!=nums[i]:
                temp = nums[i]
                nums[k] = nums[i]
                k+=1
        
        return k