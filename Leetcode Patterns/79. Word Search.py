# M - # of rows, N - # of columns, L - length of word
# Time Complexity: O(M*N*3^L)
# Space complexity: O(L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.helper(board, r,c, word, 0):
                    return True
        return False
    
    def helper(self, board,r,c, word, i):
        # edge case
        if i == len(word):
            return True
        # backtracking condition
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!=word[i]:
            return False
        
        left,right,up,down = False, False, False, False
        temp = board[r][c]
        board[r][c], i = ' ', i+1
        left = self.helper(board, r,c+1, word, i)
        right = self.helper(board, r,c-1, word, i)
        up = self.helper(board, r-1, c, word, i)
        down = self.helper(board, r+1, c, word, i)
        board[r][c] = temp
        return left or right or up or down
            