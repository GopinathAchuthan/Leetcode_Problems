class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        for i in range(1,n):
            for j in range(k):
                costs[i][j] += min([costs[i-1][x] for x in range(k) if x!=j])
        
        return min(costs[-1])