# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(max(L,D))
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        res = []
        
        while queue:
            res.append(max([node.val for node in queue]))
            numNodes = len(queue)
            for _ in range(numNodes):
                node = queue.popleft()
                if node.left:   queue.append(node.left)
                if node.right:  queue.append(node.right)
            
        return res