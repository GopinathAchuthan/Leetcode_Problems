# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        while(len(stack1) == len(stack2)):
            temp1,temp2 = [],[]
            n = len(stack1)
            for i in range(n):
                node1 = stack1[i]
                node2 = stack2[i]
                if not node1 and not node2:
                    continue
                elif not node1 or not node2:
                    return False
                else:
                    if node1.val != node2.val:
                        return False
                    temp1.append(node1.left)
                    temp1.append(node1.right)
                    temp2.append(node2.left)
                    temp2.append(node2.right)
            stack1, stack2 = temp1, temp2
            if not stack1 or not stack2:
                break
                
        if len(stack1)!= len(stack2):
            return False
        else:
            return True
        
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        
        if (root.val==subRoot.val) and self.isSameTree(root,subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right