class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        if A<2:
            return []
        heap = [1]*(A+1)
        heap[0] = 0
        heap[1] = 0

        for idx in range(2,A+1):
            if heap[idx] == 1:
                i = 2*idx
                while(i<=A):
                    heap[i] = 0
                    i+=idx
        
        return [idx for idx in range(2,A+1) if heap[idx]==1]