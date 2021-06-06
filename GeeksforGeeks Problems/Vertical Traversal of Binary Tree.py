# Vertical Traversal of Binary Tree

'''
Given a Binary Tree, find the vertical traversal of it starting 
from the leftmost level to the rightmost level.

If there are multiple nodes passing through a vertical line, then 
they should be printed as they appear in level order traversal of 
the tree.
'''

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        ans = {}
        
        # Level Order Traversal
        heap = [(root,0)]
        while(heap!=[]):
            temp = []
            for node,pos in heap:
                if pos not in ans:
                    ans[pos] = []
                ans[pos].append(node.data)
                if node.left:
                    temp.append((node.left,pos-1))
                if node.right:
                    temp.append((node.right,pos+1))
            heap = temp
        
        ans = sorted(ans.items(),key=lambda x:x[0])
        ans = list(map(lambda x:x[1],ans))

        return [data for subList in ans for data in subList]