"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = deque([root])
        level = 0
        
        while queue:
            num_nodes = len(queue)
            levels.append(list())
            for _ in range(num_nodes):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.children:
                    queue.extend(node.children)
            # go to next level
            level+=1
        
        return levels