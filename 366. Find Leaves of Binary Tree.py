# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(node):
            if not node:
                return 0
            
            pos = max(dfs(node.left), dfs(node.right))
            
            if pos not in dfs.res.keys():
                dfs.res[pos] = []
            dfs.res[pos].append(node.val)
            
            
            return pos+1
        
        dfs.res = dict()
        dfs(root)
        # print(dfs.res)
        
        return list(dfs.res.values())