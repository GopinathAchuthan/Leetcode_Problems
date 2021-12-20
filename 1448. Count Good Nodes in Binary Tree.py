# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return -1
        good_count = 0
        
        queue = deque()
        queue.append((root,root.val))
    
        # bfs
        while queue:
            node, max_path_val = queue.popleft()
            
            if node.val>=max_path_val:
                max_path_val = max(max_path_val, node.val)
                good_count += 1 
            if node.left:
                queue.append((node.left,max_path_val))
            if node.right:
                queue.append((node.right,max_path_val))
        
        
        return good_count