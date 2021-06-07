# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:            
        heap = [p,q]
        while(heap!=[]):
            a = heap.pop(0)
            b = heap.pop(0)
            if a and b:
                if a.val != b.val:
                    return False
                heap.append(a.left)
                heap.append(b.left)
                heap.append(a.right)
                heap.append(b.right)
            elif not a and not b:
                continue
            else:
                return False
        return True