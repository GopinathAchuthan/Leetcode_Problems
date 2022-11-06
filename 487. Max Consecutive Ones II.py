'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Sliding Window
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prevConsecutiveOnes = 0
        currConsecutiveOnes = 0
        maxConsecutiveOnes = 0
        zeroOccurred = 0
        
        for num in nums:
            if num == 0:
                zeroOccurred = 1
                maxConsecutiveOnes = max(maxConsecutiveOnes,zeroOccurred+prevConsecutiveOnes+currConsecutiveOnes)
                prevConsecutiveOnes, currConsecutiveOnes = currConsecutiveOnes, 0
            else:
                currConsecutiveOnes += 1
        
        maxConsecutiveOnes = max(maxConsecutiveOnes, zeroOccurred+prevConsecutiveOnes+currConsecutiveOnes)
        
        return maxConsecutiveOnes