# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N^2)
# Space Complexity: O(N)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.__helper(nums,0,len(nums))
    
    def __helper(self, arr, l, r):
        if l>=r:
            return None
        root_index = self.__findMaxIndex(arr,l,r)
        root = TreeNode(val = arr[root_index])
        
        # recursive calls
        root.left = self.__helper(arr,l,root_index)
        root.right = self.__helper(arr,root_index+1, r)
        
        return root
        
    def __findMaxIndex(self,arr,l,r):
        max_i = -1
        curr_max = -1
        for i in range(l,r):
            if curr_max < arr[i]:
                curr_max = arr[i]
                max_i = i
        return max_i