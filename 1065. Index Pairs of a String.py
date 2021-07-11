class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        text_idx = {}
        for i in range(len(text)):
            if text[i] in text_idx:
                text_idx[text[i]].append(i)
            else: text_idx[text[i]] = [i]
        ans = []
        for word in words:
            first_letter = word[0]
            size = len(word)
            for pos in text_idx[first_letter]:
                if word == text[pos:pos+size]:
                    ans.append([pos,pos+size-1])
        return sorted(ans)