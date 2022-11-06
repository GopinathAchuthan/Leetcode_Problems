'''
Time Complexity: O(log min(m,n))
Space Complexity: O(1)

Topic: Array, Binary Search
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        
        # optimization step
        if n<m:
            nums1, nums2 = nums2, nums1
            m,n = n,m
        
        k = (m+n)//2
        left, right = 0, m-1
        
        while left<=right:
            i = left+(right-left)//2
            j = k-1-i
            nums2_right= nums2[j+1] if j+1<n else float('inf')
            if nums2[j]<=nums1[i]<=nums2_right:
                # nums1[i] is the (k+1)th value
                if (m+n)%2==1:
                    return nums1[i]
                else:
                    nums1_left = nums1[i-1] if i-1>=0 else float('-inf')
                    return (max(nums1_left, nums2[j])+nums1[i])/2
            elif nums2[j]>nums1[i]:
                left = i+1
            else:
                right = i-1
        
        # if (k+1)th value is present in nums2 list
        if (m+n)%2==1:
            return nums2[k-left]
        else:
            nums1_left = nums1[right] if right>=0 else float('-inf')
            nums2_left = nums2[k-left-1] if k-left-1>=0 else float('-inf')
            return (nums2[k-left]+max(nums1_left,nums2_left))/2
        