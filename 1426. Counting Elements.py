'''
Time Complexity: O(n)
Space Complexity: O(n)

Topics: Array, Hashmap
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        mem = set(arr)
        ans = 0
        
        for val in arr:
            if val+1 in mem:
                ans+=1
        
        return ans