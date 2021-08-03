# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __pathSum_helper(self, node, targetSum, res, curr_path):
        targetSum -= node.val
        curr_path.append(node.val)
        if not node.left and not node.right:
            if targetSum is 0:
                res.append(list(curr_path))
        else:
            if node.left:
                self.__pathSum_helper(node.left, targetSum, res, curr_path)
            if node.right:
                self.__pathSum_helper(node.right, targetSum, res, curr_path)
        curr_path.pop()
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.__pathSum_helper(root, targetSum, res, [])
        return res