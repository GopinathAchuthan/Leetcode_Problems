class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        left, right = 0, min(B-1, n-1)
        pos, count = -1, 0
        last = 0

        while(last<n):
            pos = -1
            for i in range(right,left-1,-1):
                if A[i] == 1:
                    pos = i
                    break
            
            if pos == -1:
                return -1
            
            count +=1
            last = pos+B
            left, right = pos+1, min(n-1, pos+2*B-1)
        
        return count