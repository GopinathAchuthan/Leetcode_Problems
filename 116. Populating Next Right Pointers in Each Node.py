"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        
        queue = deque([root])
        
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:   queue.append(node.left)
                if node.right:  queue.append(node.right)
                if prev is not None:
                    prev.next = node
                prev = node
            
        return root