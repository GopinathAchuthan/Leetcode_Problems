'''
Time Complexity: O(m+n)
Space Complexity: O(1)

Topics: Array
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p,q = m-1,n-1
        for i in range(m+n-1,-1,-1):
            if p == -1 or q == -1:
                break
            if nums1[p]>nums2[q]:
                nums1[i] = nums1[p]
                p-=1
            else:
                nums1[i] = nums2[q]
                q-=1
        
        if q!=-1:
            for i in range(q+1):
                nums1[i] = nums2[i]