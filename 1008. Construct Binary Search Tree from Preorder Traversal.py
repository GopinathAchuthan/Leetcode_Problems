# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        
        for value in preorder[1:]:
            temp = root
            while temp!=None:
                if temp.val > value:
                    if temp.left == None:
                        temp.left = TreeNode(value)
                        break
                    temp = temp.left
            
                if temp.val<value:
                    if temp.right == None:
                        temp.right = TreeNode(value)
                        break
                    temp = temp.right
                    
        return root