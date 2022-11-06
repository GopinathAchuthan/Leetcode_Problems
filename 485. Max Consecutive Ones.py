'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        tempCount = 0
        
        for num in nums:
            if num == 1:
                tempCount+=1
            else:
                maxCount = max(maxCount, tempCount)
                tempCount = 0
        
        maxCount = max(maxCount, tempCount)
        
        return maxCount