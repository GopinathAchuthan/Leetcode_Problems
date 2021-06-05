# Check for BST
'''
Given a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
'''

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        if not root:
            return True
            
        state = [None, True] # [prev_element, ans]
            
        def preorderTraversal(node):
            if not node:
                return
            
            preorderTraversal(node.left)
            
            if state[0] is None:
                state[0] = node.data
            else:
                if state[0] < node.data:
                    state[0] = node.data
                else:
                    state[1] = False
                    return
            
            preorderTraversal(node.right)
            
        preorderTraversal(root)
        
        return state[1]