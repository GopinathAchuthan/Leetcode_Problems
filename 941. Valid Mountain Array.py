'''
Time Complexity: O(n)
Space Complexity: O(1)

Topic: Array
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # edge case
        if len(arr)<3:
            return False
        
        i,j = 0, len(arr)-1
        while i<=len(arr)-2:
            if arr[i]>=arr[i+1]:
                break
            i+=1
        
        while j>=1:
            if arr[j]>=arr[j-1]:
                break
            j-=1
        
        return i!=len(arr)-1 and j!=0 and i==j