# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)==0:
            return True if n==1 else False
        
        graph = [[] for _ in range(n)]
        
        # creating adjacency list for graph representation
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # parents list is used for to store the parent of the node 
        # and whether the node is seen or not. The value -1 indicates it is not seen
        parents = [-1]*n
        
        queue = deque()
        count = 0
        
        for i in range(n):
            if parents[i]==-1:
                parents[0] = -2
                count +=1
                # if the number of connected is more than one, return False
                if count>1:
                    return False
                queue.append(i)
                while queue:
                    curr = queue.popleft()
                    for nextNode in graph[curr]:
                        if parents[nextNode] == -1:
                            parents[nextNode] = curr
                            queue.append(nextNode)
                        elif parents[curr]!=nextNode:
                            # if this condition is satisfied then, it indicates
                            # the graph has cross edge
                            return False
        return True
        