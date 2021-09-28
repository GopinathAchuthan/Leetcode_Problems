# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Breath First Search

# Time Complexity: O(N)
# Space Complexity: O(max(D,L))
# where N - number of nodes
#       D - diameter of the tree
#       L - Height of the tree
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            n = len(queue)
            total = 0
            for _ in range(n):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(total/n)
        return res

# Method 2: Depth First Search
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        value = defaultdict(lambda: 0)
        count = defaultdict(lambda: 0)
        def dfs(node,level):
            if not node:
                return
            value[level]+=node.val
            count[level]+=1
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root,0)
        
        return [value/count for value,count in zip(value.values(),count.values())]