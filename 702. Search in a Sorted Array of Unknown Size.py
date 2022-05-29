'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0,1
        
        while(reader.get(right)<target):
            right=right*2
        left = right//2
        
        while left<=right:
            mid = left+(right-left)//2
            val = reader.get(mid)
            if val==target:
                return mid
            elif val<target:
                left = mid+1
            else:
                right = mid-1
        return -1