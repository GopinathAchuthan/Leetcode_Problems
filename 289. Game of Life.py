class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        turnAlive = set()
        turnDead = set()
        m = len(board)
        n = len(board[0])
        shifts = [(-1,-1),(-1,0),(-1,1),
                     (0,-1),(0,1),
                     (1,-1),(1,0),(1,1)]
        for row in range(m):
            for col in range(n):
                alive = 0
                neighbors = set()
                for shift in shifts:
                    i, j = row+shift[0], col+shift[1]
                    if 0 <= i < m and 0 <= j < n:
                        neighbors.add(tuple([i,j]))
                        alive += board[i][j]
                # recalculate alive value
                alive += len(neighbors.intersection(turnDead)) # previous Alive
                alive -= len(neighbors.intersection(turnAlive)) # previous Dead
                
                # rules
                if board[row][col]:
                    if 2>alive or 3<alive:
                        board[row][col] = 0
                        turnDead.add(tuple([row,col]))
                elif alive == 3: # board[row][col] is zero
                    board[row][col] = 1
                    turnAlive.add(tuple([row,col]))