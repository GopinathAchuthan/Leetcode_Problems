# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level = 0
        if not root:    return level
        
        queue = [root]
        while queue:
            level += 1
            temp = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        