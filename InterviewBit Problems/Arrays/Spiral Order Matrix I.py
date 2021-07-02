class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
        out = []
        m, n = len(A), len(A[0])
        right = n
        down = m-1
        left = n-1
        up = m-2

        i,j = 0,-1
        while(True):
            if 1>right:
                break
            for _ in range(right):
                j +=1
                out.append(A[i][j])
            right -= 2

            if 1>down:
                break
            for _ in range(down):
                i += 1
                out.append(A[i][j])
            down -= 2

            if 1>left:
                break
            for _ in range(left):
                j-=1
                out.append(A[i][j])
            left -=2

            if 1>up:
                break
            
            for _ in range(up):
                i-=1
                out.append(A[i][j])
            up -=2
        
        return out