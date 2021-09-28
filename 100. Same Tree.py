# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(min(M,N))
# Space Complexity: O(M+N)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        :type p: TreeNode
        :type q: TrrNode
        :rtype: bool
        """
        
        # Edge Case
        if p is None:
            if q is None:
                return True
            else:
                return False
        elif q is None:
            return False
        
        
        q1 = deque([p])
        q2 = deque([q])
        
        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if n1.val!=n2.val:
                return False
            
            if n1.left and n2.left:
                q1.append(n1.left)
                q2.append(n2.left)
            elif n1.left or n2.left:
                return False
            if n1.right and n2.right:
                q1.append(n1.right)
                q2.append(n2.right)
            elif n1.right or n2.right:
                return False
        
        return True