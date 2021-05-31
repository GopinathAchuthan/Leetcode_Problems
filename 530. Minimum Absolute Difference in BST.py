# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        state = [None,float('inf')]
        
        def getElements(node):          # inorder traversal
            if not node:
                return
            
            getElements(node.left)
            
            if state[0] is None:
                state[0] = node.val
            else:
                state[1] = min(state[1], abs(node.val-state[0]))
                state[0] = node.val
                
            getElements(node.right)
        
        getElements(root)
        
        return state[1]