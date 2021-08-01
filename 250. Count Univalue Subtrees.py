# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        ans  = [0]
        if not root:
            return ans[0]
        def dfs(node, ans):
            if not node.left and not node.right:
                ans[0]+=1
                return True
            result_left, result_right = True, True
            if node.left:   result_left = dfs(node.left, ans) and node.val == node.left.val
            if node.right:  result_right = dfs(node.right, ans) and node.val == node.right.val
            
            if result_left and result_right:
                ans[0]+=1
                return True
            return False
            
        dfs(root, ans)
        return ans[0]