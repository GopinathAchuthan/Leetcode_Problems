class Solution:
    def findClosestIndex(self, arr, key):
        def nearestIndex(arr, i, j, key):
            if abs(arr[i]-key)<=abs(arr[j]-key):
                return i
            else:
                return j
        
        left, right = 0, len(arr)-1
        mid = 0
        
        #edge case
        if key>arr[right]:
            return right
        if key<arr[left]:
            return left
        
        while(left<right):
            mid = left + (right-left)//2
            if arr[mid] == key:
                return mid
            elif arr[mid]>key:
                if arr[mid-1]<key:
                    return nearestIndex(arr, mid-1, mid, key)
                right = mid-1
            else:
                if arr[mid+1]>key:
                    return nearestIndex(arr, mid, mid+1, key)
                left = mid+1    
        return mid
    
    def findKClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==0:
            return []
        n = len(arr)
        left = right = self.findClosestIndex(arr, x)        
        count = 1

        while(count<k):
            count+=1
            if left>0 and right+1<n:
                if abs(arr[left-1] - x) <= abs(arr[right+1] - x):
                    left-=1
                else:
                    right+=1
            elif left>0:
                left-=1
            else:
                right+=1
        
        return arr[left:right+1]