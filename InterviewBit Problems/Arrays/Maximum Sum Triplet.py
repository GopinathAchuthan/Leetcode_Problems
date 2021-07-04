from bisect import bisect_left
class Solution:
    def binarySearch(self, arr, key):
        i = bisect_left(arr, key)
        if i:
            return i-1
        else:
            return -1
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        max1 = [0]*n
        max1[-1] = A[-1]

        for i in range(n-2,-1,-1):
            max1[i] = max(A[i], max1[i+1])
        
        max3 = [A[0]]
        ans = 0

        for i in range(1,n-1):
            idx = self.binarySearch(max3,A[i])

            if idx!=-1:
                if max1[i+1]<=A[i]:
                    continue
                ans = max(ans, max3[idx]+A[i]+max1[i+1])
            
            max3.insert(idx+1, A[i])
        
        return ans

            