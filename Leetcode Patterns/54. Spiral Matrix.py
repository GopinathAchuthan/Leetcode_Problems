"""
Topics: Array, Matrix

Time Complexity: O(mn)
Space Complexity: O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r,c = 0, 0
        m,n = len(matrix)-1, len(matrix[0])-1
        
        ans = list()
        
        while True:
            # left to right
            if c<=n:
                for j in range(c,n+1):
                    ans.append(matrix[r][j])
                r+=1
            else:   break
            # top to bottom
            if r<=m:
                for i in range(r,m+1):
                    ans.append(matrix[i][n])
                n-=1
            else:   break
            # right to left
            if c<=n:
                for j in range(n,c-1,-1):
                    ans.append(matrix[m][j])
                m-=1
            else:   break
            # bottom to top
            if r<=m:
                for i in range(m,r-1,-1):
                    ans.append(matrix[i][c])
                c+=1
            else:   break
        
        return ans