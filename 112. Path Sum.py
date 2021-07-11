# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node,curr,targetSum):
            if not node.left and not node.right:
                if curr+node.val == targetSum:
                    dfs.res = True
            curr+=node.val
            if node.left:
                dfs(node.left,curr,targetSum)
            if node.right:
                dfs(node.right,curr,targetSum)
        
        dfs.res = False
        dfs(root,0,targetSum)
        
        return dfs.res