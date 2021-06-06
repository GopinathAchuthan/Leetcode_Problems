# Level order traversal in spiral form

'''
Complete the function to find spiral order traversal of a tree. 
For below tree, function should return 1, 2, 3, 4, 5, 6, 7.
    1
   / \
  2   3
 / \ / \
7  6 5  4
'''


#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    if not root:
        return []
        
    ans = []
    rightToLeft = True
    
    # Level Order Traversal
    heap = [root]
    while(heap!=[]):
        temp = []
        
        for node in heap:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        
        if rightToLeft:
            heap.reverse()
        
        for node in heap:
            ans.append(node.data)
    
        heap = temp
        rightToLeft = not rightToLeft
    
    return ans