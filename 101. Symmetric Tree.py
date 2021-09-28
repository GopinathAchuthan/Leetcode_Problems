# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        queue = deque([(root,root)])
        
        while queue:
            nodeP, nodeQ = queue.popleft()
            if nodeP.val!=nodeQ.val:
                return False
            if nodeP.left and nodeQ.right:
                queue.append((nodeP.left, nodeQ.right))
            elif nodeP.left or nodeQ.right:
                return False
            if nodeP.right and nodeQ.left:
                queue.append((nodeP.right, nodeQ.left))
            elif nodeP.right or nodeQ.left:
                return False
        
        return True