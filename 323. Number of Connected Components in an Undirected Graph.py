class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        seen = [-1]*n
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        num_connected = 0
        for i in range(n):
            if seen[i] == -1:
                num_connected += 1
                seen[i] = 1
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    for adjNode in adjList[node]:
                        if seen[adjNode] == -1:
                            seen[adjNode] = 1
                            queue.append(adjNode)
            
        return num_connected
        