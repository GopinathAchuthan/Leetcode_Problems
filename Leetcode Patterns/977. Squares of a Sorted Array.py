'''
Topics: Array, 2 Pointers

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        hashTable = deque()
        left, right = 0, len(nums)-1
        
        while left<=right:
            a = nums[left]*nums[left]
            b = nums[right]*nums[right]
            
            if a>=b:
                hashTable.appendleft(a)
                left+=1
            else:
                hashTable.appendleft(b)
                right-=1
        
        return hashTable