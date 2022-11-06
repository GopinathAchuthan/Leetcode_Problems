'''
Time Complexity: O(n)
Space Complexity: O(n)

Topics: Array, Hashmap
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mem = set()
        
        for char in s:
            if char in mem:
                return char
            mem.add(char)
        
        return ""