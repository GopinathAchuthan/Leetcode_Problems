'''
Time Complexity: O(n)
Space Complexity: O(n)

Topics: Array
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mem = set()
        
        for num in arr:
            if num*2 in mem:
                return True
            if num%2==0 and num//2 in mem:
                return True
            mem.add(num)
        
        return False