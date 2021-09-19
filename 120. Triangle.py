# Time Complexity: O(N*N)
# Space Complexity: O(N)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        table = list(triangle[n-1])
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                table[j] = min(table[j],table[j+1])+triangle[i][j]
        return table[0]