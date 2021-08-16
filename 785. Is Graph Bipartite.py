# Method 1: BFS + with two group set
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        seen = [-1]*N
        group1 = set()
        group2 = set()
        
        for i in range(N):
            if seen[i]==-1:
                seen[i] = 1
                queue = deque([i])
                group1.add(i)
                while queue:
                    length = len(queue)
                    for _ in range(length):
                        vertex = queue.popleft()
                        for neighbor in graph[vertex]:
                            if seen[neighbor] == -1:
                                seen[neighbor] = 1
                                queue.append(neighbor)
                                group2.add(neighbor)
                            elif neighbor in group1:
                                return False
                    group1, group2 = group2, group1
        return True
                

# Method 2: BFS + with curr level and next level method
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        seen = set()
        prev_level = set()
        for i in range(N):
            if i not in seen:
                # breadth first search
                curr_level = {i}
                seen.add(i)
                while len(curr_level)>0:
                    next_level = set()
                    for node in curr_level:
                        for nextNode in graph[node]:
                            if nextNode not in seen:
                                next_level.add(nextNode)
                            elif nextNode not in prev_level:
                                return False
                    # adding next level nodes to seen
                    seen.update(next_level)
                    prev_level = curr_level
                    curr_level = next_level
        
        return True
                
