# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return (None, None) #(minvalue, maxvalue)
            leftMin, leftMax = dfs(node.left)
            rightMin, rightMax = dfs(node.right)
            out = None
            if not leftMin and not rightMin:
                out = [node.val,node.val]
            elif leftMin and rightMin:
                if not leftMax<node.val<rightMin:
                    dfs.res = False
                out = [leftMin,rightMax]    
            elif leftMin:
                if not leftMax<node.val:
                    dfs.res = False
                out = [leftMin, node.val]
            else:
                if not rightMin>node.val:
                    dfs.res = False
                out = [node.val,rightMax]
            
            return out
        
        dfs.res = True
        dfs(root)
        
        return dfs.res
        
        