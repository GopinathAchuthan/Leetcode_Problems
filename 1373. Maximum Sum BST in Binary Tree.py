# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def traversal(node):
            if not node:
                return (0,True,0,0)
            
            left_sum, left_bfs, left_min, left_max = traversal(node.left)
            right_sum, right_bfs, right_min, right_max = traversal(node.right)
            out = None
            if left_bfs and right_bfs:
                if node.left and node.right:                            # both branch is present
                    val = node.val
                    if left_max<val<right_min:
                        maxSum = left_sum+right_sum+val
                        if maxSum>traversal.sum: traversal.sum = maxSum
                        out = (maxSum, True, left_min, right_max)
                elif not node.left and not node.right:                  # left node
                    if node.val>traversal.sum: traversal.sum = node.val
                    out = (node.val,True, node.val, node.val)
                elif node.left:                                         # left branch is present
                    if left_max<node.val:
                        maxSum = left_sum+node.val
                        if maxSum>traversal.sum: traversal.sum = maxSum
                        out = (maxSum,True, left_min,node.val)
                elif node.right:                                        # right branch is present
                    if right_min>node.val:
                        maxSum = right_sum+node.val
                        if maxSum>traversal.sum: traversal.sum = maxSum
                        out = (maxSum,True,node.val,right_max)
            
            return out if out else (0,False,0,0)
        
        traversal.sum = float('-inf')
        traversal(root)
        
        return traversal.sum if traversal.sum>0 else 0