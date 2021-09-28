# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        
        x_found, y_found = False, False
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False
            for _ in range(len(queue)):
                node = queue.popleft()
                a,b = 0,0
                if node.left:
                    a = node.left.val
                    queue.append(node.left)
                if node.right:
                    b = node.right.val
                    queue.append(node.right)
                if a==x or b==x:
                    if a==y or b==y:
                        return False  
                    x_found = True
                if a==y or b==y:
                    y_found = True
        