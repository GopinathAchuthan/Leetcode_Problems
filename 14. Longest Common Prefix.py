'''
Time Complexity: O(mn)
Space Complexity: O(1)

Topic: String
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = len(strs[0])
        
        for i in range(1,len(strs)):
            end = min(end,len(strs[i]))
            for j in range(end):
                if strs[0][j]!=strs[i][j]:
                    end = j
                    break

        return strs[0][:end]
                           