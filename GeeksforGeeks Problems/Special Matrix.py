# Special Matrix

'''
Given N and a square matrix with dimension NxN. Find the minimum number
of moves required to make a matrix special. In a single move, you can
select an arbitary element and increase/decrease it by 1.

A special matrix is defined as a matrix where at least one row or column
that contains only special numbers.

A special number P is a non-negative integer for which the following quadratic 
equation has at least one negative integer root:
x^2+x-(2*p)=0

'''

import bisect
class Solution:
    def __init__(self):
        self.P = []
        for i in range(46):
            self.P.append(i*(i+1)//2)
    def minMoves (self, N, matrix):
        #code here
        ans = float('inf')
        
        # row-wise
        for i in range(N):
            moves = 0
            for j in range(N):
                pIndex = bisect.bisect_left(self.P,matrix[i][j])
                moves+=min(abs(matrix[i][j]-self.P[pIndex]), abs(matrix[i][j]-self.P[pIndex-1]))
            ans = min(ans,moves)
        
        #col-wise
        for j in range(N):
            moves = 0
            for i in range(N):
                pIndex = bisect.bisect_left(self.P,matrix[i][j])
                moves+=min(abs(matrix[i][j]-self.P[pIndex]), abs(matrix[i][j]-self.P[pIndex-1]))
            ans = min(ans,moves)
        return ans


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N = int(input())
		matrix = []
		for _ in range(N):
			arr = list(map(int,input().split()))
			matrix.append(arr)

		ob = Solution()
		print(ob.minMoves(N, matrix))