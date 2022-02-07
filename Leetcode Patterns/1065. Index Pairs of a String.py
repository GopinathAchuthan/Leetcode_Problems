'''
Topics: String, Trie

Time Complexity: O(n**2)
Space Complexity: O(n)
'''
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # initialize words dictionary
        words_dict = {}
        for char in string.ascii_lowercase:
            words_dict[char] = []
        # add value to the words dictionary
        for word in words:
            words_dict[word[0]].append((word, len(word)))
        
        ans = []
        n = len(text)
        for i in range(n):
            for word, len_word in words_dict[text[i]]:
                if i+len_word<=n and text[i:i+len_word]==word:
                    ans.append([i, i+len_word-1])
                                       
        return sorted(ans)