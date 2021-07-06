# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        out = True
        
        heap = [root]
        
        while(heap and out):
            # validate symmetric
            n = len(heap)//2
            for i in range(n):
                if heap[i] and heap[~i]:
                    if heap[i].val != heap[~i].val:
                        out = False
                elif not heap[i] and not heap[~i]:
                    continue
                else:
                    out = False
            
            # level order traversal
            temp = []
            nextNode = False
            for node in heap:
                if node:
                    nextNode = True
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    temp.append(None)
                    temp.append(None)
            heap = temp if nextNode else []
        return out