'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        
        for i in range(len(arr)-1,-1,-1):
            arr[i], maxRight = maxRight, max(maxRight, arr[i])
        
        return arr
        
        
        