# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        mem = [root]
        res = []
        
        while(mem):
            res.append([node.val for node in mem])
            temp = []
            for node in mem:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            mem = temp
        
        return res