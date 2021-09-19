# Time Complexity: O(K)
# Space Complexity: O(N)

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        cache = []
        for i in range(n):
            cache.append((matrix[i][0], i, 0))
        heapq.heapify(cache)
        ans = -1
        for _ in range(k):
            ans,row,col = heapq.heappop(cache)
            col+=1
            if col<n:
                heapq.heappush(cache, (matrix[row][col],row,col))
        return ans