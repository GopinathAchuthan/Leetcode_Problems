class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for n in range(1,numRows):
            res.append([1])
            for k in range(1,n):
                res[n].append(res[n-1][k]+res[n-1][k-1])
            res[n].append(1)  
        return res