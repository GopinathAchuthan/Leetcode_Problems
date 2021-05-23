class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1,n+1):
            if i <=n:
                squares.append(i*i)
                
        array = [i for i in range(n+1)]
        
        for i in range(len(array)):
            for square in squares:
                if square<=i:
                    array[i] = min(array[i], 1+array[i-square])
                else:
                    break

        return array[-1]