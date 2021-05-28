class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for i in range(numRows)]
        currLine = 0
        flag = True
        
        if numRows == 1:
            return s
        
        for val in s:
            if flag:        # down
                rows[currLine].append(val)
                currLine+=1
            else:           # cross
                rows[currLine].append(val)
                currLine-=1
            
            if currLine == numRows:
                flag = False
                currLine -= 2
            if currLine < 0:
                flag = True
                currLine = 1
        
        return "".join("".join(row) for row in rows)
        