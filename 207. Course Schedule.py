"""
time complexity: O(v+e)
space complexity: O(v+e)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initializing the adjacency list representation of the graph 
        graph = [[] for _ in range(numCourses)]
        
        for src, des in prerequisites:
            graph[src].append(des)
        
        timestamp = [0]
        start = [-1]*numCourses
        end = [-1]*numCourses
        
        # define dfs function
        def dfs(node: int) -> bool:
            start[node] = timestamp[0]
            timestamp[0]+=1
            # calling next node
            for nextNode in graph[node]:
                # if next node not visited
                if start[nextNode] == -1:
                    if not dfs(nextNode):
                        return False
                elif end[nextNode]==-1:
                    # this indicates there is back edge present in the DFS tree
                    # Hence, the cycle is present.
                    return False
                
            end[node] = timestamp[0]
            timestamp[0]+=1
            
            return True
        
        
        # outer loop
        for v in range(numCourses):
            # check whether the node v is visited
            if start[v] == -1:
                # calling dfs function
                if not dfs(v):
                    return False
        return True
        