# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([(1,root)])
        maxWidth = 0
        
        while queue:
            currWidth = queue[-1][0]-queue[0][0]+1
            maxWidth = max(maxWidth,currWidth)
            for _ in range(len(queue)):
                key,node = queue.popleft()
                if node.left:   queue.append((2*key, node.left))
                if node.right:  queue.append((2*key+1, node.right))
        
        return maxWidth