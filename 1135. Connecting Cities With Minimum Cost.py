class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        subset = list(range(n+1))
        
        def findSubset(node):
            if subset[node] != node:
                subset[node] = findSubset(subset[node])
            return subset[node]
        
        def union(node1, node2):
            subset[node1] = subset[node2]
        
        connections.sort(key = lambda x:x[2])
        totalCost = 0
        numEdges = 0
        for connection in connections:
            node1, node2, edge = connection
            
            subset_node1 = findSubset(node1)
            subset_node2 = findSubset(node2)
            
            if subset_node1 == subset_node2:
                pass
            else:
                union(subset_node1, subset_node2)
                totalCost += edge
                numEdges += 1
        
        return totalCost if numEdges==n-1 else -1