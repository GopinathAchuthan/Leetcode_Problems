'''
Time Complexity: O(n)
Space Complexity: O(n)

Topics: Array, Hashmap
'''
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        occurence = counts[s[0]]
        
        for val in counts.values():
            if val != occurence:
                return False
        
        return True