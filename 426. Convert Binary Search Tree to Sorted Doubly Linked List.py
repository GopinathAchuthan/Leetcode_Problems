"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:            
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def helper(node):
            nonlocal tail
            if node.left: helper(node.left)
            tail.right = node
            node.left = tail
            tail = node
            if node.right: helper(node.right)
        
        head = Node()   
        tail = head
        
        helper(root)
        
        # join head and tail
        head = head.right
        head.left = tail
        tail.right = head
        
        return head