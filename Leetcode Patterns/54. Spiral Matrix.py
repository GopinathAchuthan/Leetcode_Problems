# Time Complexity: O(M*N)
# Space Complexity: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up,down = 0, len(matrix)-1
        left,right = 0, len(matrix[0])-1
        res = []
        while True:
            if left>right: break
            for j in range(left,right+1):
                res.append(matrix[up][j])
            up+=1
            if up>down: break
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right-=1
            if left>right: break
            for j in range(right,left-1,-1):
                res.append(matrix[down][j])
            down-=1
            if up>down: break
            for i in range(down,up-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res