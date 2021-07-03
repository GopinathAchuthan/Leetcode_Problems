# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return float('-inf')
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            
            maxPath = max(node.val, node.val+leftPath, node.val+rightPath)
            maxSum = max(maxPath, node.val+leftPath+rightPath)
            if dfs.maxSum<maxSum:
                dfs.maxSum = maxSum
            
            return maxPath if maxPath>0 else 0
        
        dfs.maxSum = float('-inf')
        dfs(root)
        return dfs.maxSum