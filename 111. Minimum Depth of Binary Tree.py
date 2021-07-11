# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [root]
        level = 0
        flag = False
        while(queue):
            level += 1
            temp = []
            for node in queue:
                if not node.left and not node.right:
                    flag = True
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if flag: break
            queue = temp
        
        return level
        