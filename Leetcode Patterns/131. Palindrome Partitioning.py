# Time Complexity: O(N*2^N)
# Space Complexity: O(N*N)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        mem = [[False]*len(s) for _ in range(len(s))]
        self.__helper(s, 0, mem, [], res)
        return res
    
    def __helper(self, s, i, mem, slate, res):
        if i == len(s):
            res.append(list(slate))
        for k in range(i,len(s)):
            if s[i]==s[k] and (k-i<=2 or mem[i+1][k-1]):
                mem[i][k] = True
                slate.append(s[i:k+1])
                self.__helper(s,k+1,mem,slate, res)
                slate.pop()