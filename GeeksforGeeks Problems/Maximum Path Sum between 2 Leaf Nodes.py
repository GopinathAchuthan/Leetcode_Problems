# Maximum Path Sum between 2 Leaf Nodes

'''
Given a binary tree in which each node element contains a number. 
Find the maximum possible sum from one leaf node to another leaf node.

NOTE: Here Leaf node is a node which is connected to exactly one different node.

Example 1:
Input :      
           3                               
         /   \                          
       4       5                     
      / \      
    -10   4                          
Output: 16
Explanation :
Maximum Sum lies between leaf node 4 and 5.
4 + 4 + 3 + 5 = 16.

Example 2:
Input :    
           -15                               
         /    \                          
        5       6                      
      /  \     / \
    -8    1   3   9
   /  \            \
  2   -3            0
                   / \
                  4  -1
                     /
                    10  
Output :  27
Explanation:
The maximum possible sum from one leaf node 
to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)
'''

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
def maxPathSumUtil(node,depth):
    if not node:
        return 0
    
    leftPath = maxPathSumUtil(node.left,depth+1)
    rightPath = maxPathSumUtil(node.right,depth+1)
    pathMax = 0
    
    if (node.left and node.right) or depth==0:
        maxPathSumUtil.result = max(maxPathSumUtil.result,leftPath+rightPath+node.data)
        pathMax = max(leftPath,rightPath)+node.data
    elif node.left:
        pathMax = leftPath+node.data
    else:
        pathMax = rightPath+node.data
    
    return pathMax


def maxPathSum(root):
    # code here
    maxPathSumUtil.result = float('-inf')
    maxPathSumUtil(root,0)
    
    return maxPathSumUtil.result
