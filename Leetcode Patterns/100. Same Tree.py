"""
Topics: Tree, BFS, DFS

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        a = deque()
        a.append((p,q))
        
        while a:
            n1, n2 = a.pop()
            if n1.val!=n2.val:
                return False
            if n1.left and n2.left:     a.append((n1.left, n2.left))
            elif n1.left or n2.left:    return False
            
            if n1.right and n2.right:   a.append((n1.right, n2.right))
            elif n1.right or n2.right:  return False
            
        return True