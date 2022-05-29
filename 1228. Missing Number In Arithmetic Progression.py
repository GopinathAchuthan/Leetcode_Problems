'''
Time Complexity: O(log n)
Space Complexity: O(1)

Topic: Math, Binary Search
'''
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        '''
        Arthimetic progression formula
        An = A1+(n-1)d
        => An = A0+n*d
        => n = (An-A0)/n
        In this problem,
        An - last element
        A0 - first element
        n is length of arr
        '''
        d = (arr[-1]-arr[0])//len(arr)
        
        left, right = 0,len(arr)-1
        
        while left<=right:
            mid = left+(right-left)//2
            
            if arr[mid]==arr[0]+mid*d:
                left = mid+1
            else:
                right = mid-1
        
        
        # return arr[left]-d -> won't work for d=0, 
        # that time left == len(arr). So it will be out of bound
        
        return arr[right]+d
        # Or we can use return arr[0]+left*d