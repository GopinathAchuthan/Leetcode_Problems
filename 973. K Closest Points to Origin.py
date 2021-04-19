# Method 1
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda point: point[0]**2+point[1]**2)
        return points[:k]

# Method 2
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = defaultdict(lambda:[])
        for point in points:
            heap[point[0]**2+point[1]**2].append(point)
        heap = sorted(heap.items())
        
        res = []
        i = 0                       # heap variable pointer
        while k>0:
            k -= len(heap[i][1])
            res += heap[i][1]
            i+=1
            
        return res
