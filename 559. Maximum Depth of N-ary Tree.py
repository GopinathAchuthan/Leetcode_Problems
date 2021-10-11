"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
        
        return depth