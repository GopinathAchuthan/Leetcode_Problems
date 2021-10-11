# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxSeq = 1
        queue = deque()
        queue.append((root,float('-inf'),0))
        
        while queue:
            node,parent,curr = queue.pop()
            if node.val == parent+1:
                curr+=1
            else:
                curr = 1
            maxSeq = max(maxSeq, curr)
            if node.left:
                queue.append((node.left, node.val, curr))
            if node.right:
                queue.append((node.right, node.val, curr))
        
        return maxSeq
        