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
                
