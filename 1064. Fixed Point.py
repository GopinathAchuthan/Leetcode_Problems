'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]<mid:
                left=mid+1
            else:
                right=mid-1
        return left if left!=len(arr) and arr[left]==left else -1