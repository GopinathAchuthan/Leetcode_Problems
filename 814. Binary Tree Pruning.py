# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)

        if not left:
            root.left = None
        if not right:
            root.right = None
        if not left and not right and root.val == 0:
            root = None

        return root
        
        
                