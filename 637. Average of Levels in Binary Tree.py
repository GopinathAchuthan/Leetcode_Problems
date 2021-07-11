# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Breath First Search
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        ans = []
        
        while(queue):
            value = count = 0
            temp = []
            for node in queue:
                value+=node.val
                count+=1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(value/count)
            queue = temp
        
        return ans

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