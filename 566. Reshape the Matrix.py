class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m*n != r*c:
            return mat
        
        out = []
        
        p,q = 0,0
        
        for i in range(r):
            out.append([])
            for j in range(c):
                out[i].append(mat[p][q])
                
                if q<n-1:
                    q+=1
                else:
                    p+=1
                    q=0
        return out