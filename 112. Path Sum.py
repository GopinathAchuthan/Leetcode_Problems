# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            node, pathSum = queue.pop()
            pathSum += node.val
            
            if node.left is None and node.right is None:
                if pathSum == targetSum:
                    return True
            if node.left:
                queue.append((node.left, pathSum))
            if node.right:
                queue.append((node.right, pathSum))
        
        return False
        
        