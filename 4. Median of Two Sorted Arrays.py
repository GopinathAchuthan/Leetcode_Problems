class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenNums1 = len(nums1)
        lenNums2 = len(nums2)
        singleMedium = True
        if (lenNums1+lenNums2)%2==0:
            singleMedium = False
            # single median
        medianIndex = (lenNums1+lenNums2)//2
        if not singleMedium:
            medianIndex -= 1
        
        i,j,k = 0,0,0
        while(i<lenNums1 and j<lenNums2):
            if k == medianIndex:
                if singleMedium:
                    return min(nums1[i],nums2[j])
                else:
                    if nums1[i]<nums2[j]:
                        if i+1<lenNums1 and nums1[i+1]<nums2[j]:
                            print('check1')
                            return (nums1[i]+nums1[i+1])/2
                        else:
                            print('check2')
                            return (nums1[i]+nums2[j])/2
                    else:
                        if j+1<lenNums2 and nums2[j+1]<nums1[i]:
                            print('check3')
                            return (nums2[j]+nums2[j+1])/2
                        else:
                            print('check4')
                            return (nums1[i]+nums2[j])/2
                        
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
            k += 1

        while(i<lenNums1):
            if k == medianIndex:
                if singleMedium:
                    return nums1[i]
                else:
                    return (nums1[i]+nums1[i+1])/2
            k+=1
            i+=1

        while(j<lenNums2):
            if k == medianIndex:
                if singleMedium:
                    return nums2[j]
                else:
                    return (nums2[j]+nums2[j+1])/2
            k+=1
            j+=1
