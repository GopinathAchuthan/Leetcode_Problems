# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            
            if inorderTraversal.prev is None:
                inorderTraversal.prev = node.val
            else:
                inorderTraversal.minDiff = min(node.val - inorderTraversal.prev, inorderTraversal.minDiff)
                inorderTraversal.prev = node.val
            
            inorderTraversal(node.right)
        
        inorderTraversal.prev = None
        inorderTraversal.minDiff = float('inf')
        inorderTraversal(root)
        
        return inorderTraversal.minDiff