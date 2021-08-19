class Solution:
    def dp(self, n,k, mem):
        if k in mem[n]:
            return mem[n][k]
        mem[n][k] = self.dp(n-1,k,mem)+self.dp(n-1,k-1,mem)
        return mem[n][k]
    
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        heap = {}
        for i in range(rowIndex+1):
            heap[i] = {}
            heap[i][0] = 1
            heap[i][i] = 1
            
        for i in range(rowIndex+1):
            res.append(self.dp(rowIndex, i, heap))
        
        return res
    
        