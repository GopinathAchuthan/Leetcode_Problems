# Bottom View of Binary Tree

'''
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.
'''


#Function to return a list containing the bottom view of the given tree.
def bottomView(root):
    # code here
    ans = {}
    def preorderTraversal(node,level,pos):
        if node is None:
            return
        
        preorderTraversal(node.left,level+1,pos-1)
        
        if pos not in ans:
            ans[pos] = (level,node.data)
        else:
            if ans[pos][0]<=level:
                ans[pos] = (level,node.data)
        
        preorderTraversal(node.right,level+1,pos+1)
        
    
    preorderTraversal(root,0,0)
    ans = sorted(ans.items(),key=lambda x:x[0])
    return list(map(lambda x:x[1][1],ans))