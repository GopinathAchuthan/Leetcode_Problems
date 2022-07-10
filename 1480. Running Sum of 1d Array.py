'''
Time Complexity: O(n)
Space Complexity: O(1)

Time Complexity: Array
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        temp = 0
        for num in nums:
            temp+=num
            ans.append(temp)
        
        return ans