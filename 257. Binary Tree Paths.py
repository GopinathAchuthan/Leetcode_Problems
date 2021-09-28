# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Iterative Method

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        queue = deque()
        queue.append((root,str(root.val)))
        
        while queue:
            node, path = queue.pop()
            if node.left is None and node.right is None:
                res.append(path)
            if node.left:
                queue.append((node.left,path+'->'+str(node.left.val)))
            if node.right:
                queue.append((node.right,path+'->'+str(node.right.val)))
        
        return res


# Method 2: Recursive Method

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.__dfs(root,"", res)
        return res
    
    def __dfs(self, node, path, res):
        """
        :type node: TreeNode
        :type slate: str
        :type res: List[str]
        """
        path += str(node.val)
        # base case
        if node.left is None and node.right is None:
            res.append(path)
        
        path += '->'
        # recursive calls
        if node.left:
            self.__dfs(node.left, path, res)
        if node.right:
            self.__dfs(node.right,path, res)