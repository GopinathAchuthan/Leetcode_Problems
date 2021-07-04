class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start_idx = 0
        end_idx = -1
        maxSum = 0

        tempSum, tempStart, tempEnd = 0, 0,-1
        for idx in range(len(A)):
            if A[idx]<0:
                if maxSum<tempSum:
                    maxSum = tempSum
                    start_idx, end_idx = tempStart, tempEnd
                elif maxSum==tempSum and end_idx-start_idx+1 < tempEnd-tempStart+1:
                        start_idx, end_idx = tempStart, tempEnd
                tempSum = 0
                tempStart = idx+1
            else:
                tempSum += A[idx]
                tempEnd = idx
        # print(tempStart,tempEnd,  start_idx, end_idx, maxSum,tempSum)
        if maxSum<tempSum:
            start_idx, end_idx = tempStart, tempEnd
        elif maxSum==tempSum and end_idx-start_idx < tempEnd-tempStart:
            start_idx, end_idx = tempStart, tempEnd

        return A[start_idx:end_idx+1]

