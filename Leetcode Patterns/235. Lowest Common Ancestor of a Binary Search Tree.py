"""
Topics: BST, Recursive DFS, Post Order Traversal

Time Complexity: O(n)
Call stack space: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p,q = q,p
            
        def dfs(node):
            # base case
            if node.left is None and node.right is None:
                return p==node or q==node
            
            
            p_found = p==node
            q_found = q==node
            # recursive calls
            if node.left:
                p_found = p_found or dfs(node.left)
            if node.right:
                q_found = q_found or dfs(node.right)
            
            
            if p_found and q_found:
                ans[0] = node
                return False
            
            return p_found or q_found
            
        ans = [TreeNode()]
        dfs(root)
        
        return ans[0]