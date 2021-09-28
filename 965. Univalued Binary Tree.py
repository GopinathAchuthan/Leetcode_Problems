# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        target = root.val
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.val!=target:
                return False
            if node.left:   queue.append(node.left)
            if node.right:  queue.append(node.right)
        
        return True