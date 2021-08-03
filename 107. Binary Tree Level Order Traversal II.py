# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # base case
        if root is None:
            return []
        
        curr_level = [root]
        output = []
        
        while curr_level!=[]:
            next_level = []
            output.append([])
            for node in curr_level:
                output[-1].append(node.val)
                if node.left:   next_level.append(node.left)
                if node.right:  next_level.append(node.right)
            curr_level = next_level
        
        return output[::-1]