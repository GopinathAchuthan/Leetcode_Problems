class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        n = len(matrix)
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i))
        pointer = [0]*n
        count = 0
        value = 0
        idx = -1
        while(count<k):
            value, idx = heapq.heappop(heap)
            count+=1
            pointer[idx]+=1
            if pointer[idx]<n:
                heapq.heappush(heap, (matrix[idx][pointer[idx]], idx))
        
        return value