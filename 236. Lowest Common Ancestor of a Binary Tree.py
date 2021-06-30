# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q, p_found, q_found):
            if not node:
                return (False, False)
            
            p_found1,q_found1 =dfs(node.left, p, q, p_found, q_found)
            p_found2,q_found2 =dfs(node.right, p, q, p_found, q_found)
            
            p_found = p_found1 or p_found2 or node.val==p.val
            q_found = q_found1 or q_found2 or node.val==q.val

            
            if p_found and q_found and not dfs.out:
                dfs.out = node
                
            return p_found, q_found
        
        p_found, q_found = False, False
        dfs.out = None
        dfs(root, p, q, p_found, q_found)
        
        return dfs.out