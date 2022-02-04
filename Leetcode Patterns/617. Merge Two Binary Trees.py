"""
Topics: Tree, BFS, DFS

Time Complexity: O(n1)
Space Complexity: O(n1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Note: In this function, I am modifing the root1 into merged tree.
        It is also possible to create merged tree without modification.
        """
        # base case
        if root1 is None: return root2
        elif root2 is None: return root1
        
        q = deque()
        q.append((root1, root2))
        
        while q:
            n1, n2 = q.pop()
            n1.val += n2.val
            # left branch
            if n1.left and n2.left:
                q.append((n1.left, n2.left))
            elif n1.left is None:
                n1.left = n2.left
            # right branch
            if n1.right and n2.right:
                q.append((n1.right, n2.right))
            elif n1.right is None:
                n1.right = n2.right
        
        return root1