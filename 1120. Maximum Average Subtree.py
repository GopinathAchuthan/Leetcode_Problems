# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(node):
            if not node:
                return 0,0  # total, count
            left_total, left_count = dfs(node.left)
            right_total, right_count = dfs(node.right)
            
            total = left_total+right_total+node.val
            count = left_count+right_count+1
            avg = total/count
            
            if avg>dfs.avg:
                dfs.avg=avg
            
            return total,count
        
        dfs.avg = float('-inf')
        dfs(root)
        
        return dfs.avg