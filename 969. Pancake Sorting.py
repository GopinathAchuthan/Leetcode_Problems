'''
Time Complexity: O(N^2)
Space Complexity: O(1)

Topic: Array, Decrease ans Conquer
'''
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:        
        ans = []
        
        for i in range(len(arr),1,-1):
            if arr[i-1] != i:
                for j in range(i):
                    if arr[j] == i:
                        arr[:j+1] = arr[j::-1]
                        ans.append(j+1)
                        arr[:i] = arr[i-1::-1]
                        ans.append(i)
                        break
        return ans