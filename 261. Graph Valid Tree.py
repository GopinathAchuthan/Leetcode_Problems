class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        adjList = [[] for _ in range(n)]
        parent = [-1]*n
        seen = set()
        
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        queue = deque([0])
        seen.add(0)
        
        while queue:
            node = queue.popleft()
            for nextNode in adjList[node]:
                if nextNode not in seen:
                    parent[nextNode] = node
                    seen.add(nextNode)
                    queue.append(nextNode)
                elif nextNode != parent[node]:
                    return False
        
        return True if len(seen)==n else False