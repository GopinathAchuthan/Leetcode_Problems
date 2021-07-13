class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right = len(matrix[0])-1
        down = len(matrix)-1
        left = 0
        top = 1
        ans = []
        i,j = 0,-1
        
        while(True):
            if j>=right:
                break
            while(j<right):
                j+=1
                ans.append(matrix[i][j])
            right-=1
            if i>=down:
                break
            while(i<down):
                i+=1
                ans.append(matrix[i][j])
            down-=1
            if j<=left:
                break
            while(j>left):
                j-=1
                ans.append(matrix[i][j])
            left+=1
            if i<=top:
                break
            while(i>top):
                i-=1
                ans.append(matrix[i][j])
            top+=1
            
        return ans