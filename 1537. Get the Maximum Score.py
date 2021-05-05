class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        partialSum1 = [0]
        partialSum2 = [0]
        
        
        i = 0
        j = 0
        
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i] == nums2[j]:
                partialSum1[-1]+=nums1[i]
                partialSum2[-1]+=nums2[j]
                partialSum1.append(0)
                partialSum2.append(0)
                i+=1
                j+=1
            
            elif nums1[i] < nums2[j]:
                partialSum1[-1]+=nums1[i]
                i+=1
            
            else:
                partialSum2[-1]+=nums2[j]
                j+=1
                
        
        while(i<len(nums1)):
            partialSum1[-1]+=nums1[i]
            i+=1
        
        while(j<len(nums2)):
            partialSum2[-1]+=nums2[j]
            j+=1
        
        
        k = 0
        while(k<len(partialSum1)):
            ans+= max(partialSum1[k], partialSum2[k])
            k+=1
        return ans % (10**9 + 7)