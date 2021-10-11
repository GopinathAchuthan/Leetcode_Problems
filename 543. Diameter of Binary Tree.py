# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        
        diameter = [0]
        self.__dfs(root,diameter)
        return diameter[0]
    
    def __dfs(self, node, diameter):
        left_maxHeight = 0
        right_maxHeight = 0
        
        # recursive calls
        if node.left:   left_maxHeight = self.__dfs(node.left,diameter)+1
        if node.right:  right_maxHeight = self.__dfs(node.right,diameter)+1
        
        # calc diameter
        diameter[0] = max(diameter[0], left_maxHeight+right_maxHeight)
        
        # return max height
        return max(left_maxHeight, right_maxHeight)