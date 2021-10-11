# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        mem = dict()
        mem[0] = 1
        count = [0]
        
        # depth first search
        self.__dfs(root, mem, 0, count, targetSum)
        
        # returning count
        return count[0]
    
    def __dfs(self, node, mem, currSum, count, k):
        currSum += node.val
        
        if currSum-k in mem :
            count[0] += mem[currSum-k]
        mem[currSum] = mem.get(currSum,0)+1
        
        # recursive calls
        if node.left:   self.__dfs(node.left, mem, currSum, count, k)
        if node.right:  self.__dfs(node.right, mem, currSum, count, k)
    
        mem[currSum] = mem[currSum] - 1