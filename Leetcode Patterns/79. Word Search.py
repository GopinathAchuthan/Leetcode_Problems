'''
Topics: Graph, Recursive DFS, Post order Traversal

Time Complexity:    O(mnw)
Call Stack Space :  O(w)
Auxiliary Sapce:    O(mn)
Space Complexity:   O(mn+w)
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # post order traversal
        def dfs(i,j,w):
            # base case
            if w == len_w[0]-1:
                return board[i][j]==word[w]
            
            # recursive calls
            if board[i][j]==word[w]:
                captured[i][j] = True
                for r,c in [[i-1,j], [i,j-1], [i+1,j], [i,j+1]]:
                    if 0<=r<len_b[0] and 0<=c<len_b[1] and not captured[r][c]:
                        if dfs(r,c,w+1):    return True
                captured[i][j] = False
            
            # returning false
            return False
        
        
        len_b = [len(board), len(board[0])]
        len_w = [len(word)]
        captured = [[False]*len_b[1] for _ in range(len_b[0])]
        
        for i in range(len_b[0]):
            for j in range(len_b[1]):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        
        return False