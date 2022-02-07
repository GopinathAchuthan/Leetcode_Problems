'''
Topics: Array

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):    return []
        
        ans = []
        for row in range(m):
            start = n*row
            end = n*(row+1)
            ans.append(original[start:end])
        
        return ans