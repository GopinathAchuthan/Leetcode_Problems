# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        leftToRight = True
        mem = [root]
        res = []
        
        while(mem):
            if leftToRight:
                res.append([node.val for node in mem])
            else:
                res.append([node.val for node in mem[::-1]])
            leftToRight = not leftToRight
            
            temp = []
            for node in mem:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            mem = temp
        
        return res