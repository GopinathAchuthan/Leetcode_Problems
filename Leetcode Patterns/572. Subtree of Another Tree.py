"""
Topics: TREE, BFS, DFS

Time Complexity: O(n1*n2)
Space Complexity: O(n1+n2)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        p = deque()
        q = deque()
        
        # same tree subroutine
        def sameTree(p, q):
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
        
        # main part
        q.append(root)
        
        while q:
            node = q.popleft()
            matched = False
            if node.val == subRoot.val:
                matched = sameTree(node, subRoot)
            if matched: return True
            
            if node.left:   q.append(node.left)
            if node.right:  q.append(node.right)
        
        return False
    