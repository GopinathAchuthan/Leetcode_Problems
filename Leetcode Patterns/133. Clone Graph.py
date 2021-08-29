# Time Complexity: O(V+E)
# Space Complexity: O(V)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = deque()
        queue.append(node)
        visited  = dict()      # O(V)
        visited[node] = Node(node.val,[])
        
        while queue:
            curr = queue.pop()
            for nextNode in curr.neighbors:
                if nextNode not in visited:
                    visited[nextNode] = Node(nextNode.val,[])
                    queue.append(nextNode)
                visited[curr].neighbors.append(visited[nextNode])
        return visited[node]
        