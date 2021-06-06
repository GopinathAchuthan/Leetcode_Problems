# Left View of Binary Tree

'''
Given a Binary Tree, print Left view of t. Left view of a Binary Tree 
is set of nodes visible when tree is visited from Left side. The task 
is to complete the function leftView(), which accepts root of the tree 
as argument.

Left view of following tree is 1 2 4 8.

          1
       /    \
      2      3
    /  \    /  \
   4    5  6    7
    \
     8   
'''



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    # code here
    if not root:
        return []
    
    view = []
    heap = [root]
    
    while(heap!=[]):
        view.append(heap[0].data)
        temp = []
        for node in heap:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        heap = temp
    return view
