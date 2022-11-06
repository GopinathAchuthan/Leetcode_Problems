'''
Time Complexity: O(N) where N is sum of digits
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        countEvenDigits = 0
        
        for num in nums:
            # count number of digits in num
            countDigits = 0
            while num>0:
                num//=10
                countDigits+=1
                
            if countDigits%2==0:
                countEvenDigits += 1
        
        return countEvenDigits