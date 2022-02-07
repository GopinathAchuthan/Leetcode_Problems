"""
Topics: Tree, BFS, DFS

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.pop()
            node.left, node.right = node.right, node.left
            if node.left:   q.append(node.left)
            if node.right:  q.append(node.right)
        
        return root