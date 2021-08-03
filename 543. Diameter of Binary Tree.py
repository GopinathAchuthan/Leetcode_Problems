# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def post_order_traversal(node):
            # base case:
            if not node.left and not node.right:
                return 0
            l_pathMax = 0
            r_pathMax = 0
            if node.left:
                l_pathMax = post_order_traversal(node.left)+1
            if node.right:
                r_pathMax = post_order_traversal(node.right)+1
                
            if post_order_traversal.diameter< l_pathMax+r_pathMax:
                post_order_traversal.diameter = l_pathMax+r_pathMax
            return max(l_pathMax, r_pathMax)
            
        post_order_traversal.diameter = 0
        post_order_traversal(root)
        return post_order_traversal.diameter
            
            