'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: String, Hashmap
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # return len(set(sentence)) == 26
        return set(sentence)  == set(string.ascii_lowercase)