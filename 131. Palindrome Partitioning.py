class Solution:
    def __backtracking(self, result, arr, start, curr,dp):
        if start>=len(arr):
            result.append(list(curr))
            return
        for end in range(start,len(arr)):
            if arr[start]==arr[end] and (end-start<=2 or dp[start+1][end-1]):
                dp[start][end] = True
                curr.append(arr[start:end+1])
                self.__backtracking(result,arr,end+1,curr,dp)
                curr.pop()
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        result = []
        self.__backtracking(result,s,0,[],dp)
        return result