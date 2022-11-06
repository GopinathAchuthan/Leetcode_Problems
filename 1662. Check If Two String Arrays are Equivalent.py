'''
Time Complexity: O(S)
Space Complexity: O(1)

Topic: String
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p,q = 0,0
        for i in range(len(word1)):
            for j in range(len(word1[i])):
                # sanity check
                if len(word2)==p:
                    return False
                
                if word1[i][j] != word2[p][q]:
                    return False
                
                q += 1
                # handling index overflow
                if len(word2[p])==q:
                    p+=1
                    q=0
        
                
        return len(word2)==p
                