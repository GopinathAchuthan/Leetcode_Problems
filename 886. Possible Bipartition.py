class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        n = n+1
        adjList = [[] for _ in range(n)]
        seen = [-1]*n
        
        for p1, p2 in dislikes:
            adjList[p1].append(p2)
            adjList[p2].append(p1)
        
        group1 = set()
        group2 = set()
        
        for i in range(1,n):
            if seen[i]==-1:
                seen[i] = 1
                queue = deque()
                queue.append(i)
                group1.add(i)
                while queue:
                    length = len(queue)
                    for _ in range(length):
                        vertex = queue.popleft()
                        for neighbor in adjList[vertex]:
                            if seen[neighbor] == -1:
                                seen[neighbor] = 1
                                queue.append(neighbor)
                                group2.add(neighbor)
                            elif neighbor in group1:
                                return False
                    group1, group2 = group2, group1
        return True