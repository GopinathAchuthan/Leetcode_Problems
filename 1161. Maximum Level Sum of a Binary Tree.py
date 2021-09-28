# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        level = 0
        currMax = float('-inf')
        res = 1
        
        while queue:
            total = 0
            level+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                total+=node.val
                if node.left:   queue.append(node.left)
                if node.right:  queue.append(node.right)
            if total>currMax:
                currMax = total
                res = level
                
        return res