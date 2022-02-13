'''
Topics: Dynamic Programming

Time Complexity: O(nt)
Space Complexity: O(n+t)
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr = []
        for num in nums:
            if num<=target:
                arr.append(num)
        arr.sort()
        n = len(arr)
        
        table = [0]*(target+1)
        table[0] = 1
        
        for i in range(1,target+1):
            k = 0
            while(k<n):
                val = arr[k]
                k+=1
                if i-val>=0:
                    table[i]+=table[i-val]
                else:
                    break
    
        return table[target]