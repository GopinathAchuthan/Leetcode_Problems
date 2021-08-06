# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __buildTreeHelper(self, po,pos,poe, io_map,ios,ioe):
        # po - preorder array
        # pos - preorder array start index
        # poe - preorder array end index
        # io_map - inorder_heap
        # ios - inorder array start index
        # ioe - inorder array end index
        if ios>ioe:
            return None
        root_val = po[pos]
        root = TreeNode(val=root_val)
        root_idx = io_map.get(root_val)
        left_count = root_idx-ios
        root.left = self.__buildTreeHelper(po, pos+1, pos+left_count, io_map, ios, root_idx-1)
        root.right = self.__buildTreeHelper(po, pos+left_count+1,poe, io_map, root_idx+1, ioe)
        
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_heap = {}
        for i,val in enumerate(inorder):
            inorder_heap[val] = i
        return self.__buildTreeHelper(preorder, 0, len(preorder)-1, inorder_heap, 0, len(inorder)-1)