# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(D)
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """

        # Edge case
        if depth==1:
            return TreeNode(val,left=root)
        
        queue = deque([root])
        level = 0
        
        while queue:
            level += 1
            if depth == level:
                break
            for _ in range(len(queue)):
                node = queue.popleft()
                if level == depth-1:
                    node.left = TreeNode(val,left=node.left)
                    node.right = TreeNode(val,right=node.right)
                else:
                    if node.left:   queue.append(node.left)
                    if node.right:  queue.append(node.right)
            
        return root