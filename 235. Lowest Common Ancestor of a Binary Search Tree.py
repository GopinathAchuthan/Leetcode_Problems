# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iteration
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        
        while(True):
            value = node.val
            if p_val<value and q_val<value:
                node = node.left
            elif p_val>value and q_val>value:
                node = node.right
            else:
                return node

# Recursive
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val<val and q_val<val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val>val and q_val>val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            