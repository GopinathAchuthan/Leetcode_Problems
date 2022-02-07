# Soln 1 and Soln 2 are similar. Yet Soln 1 performs better than Soln 2 in case of Time Taken
# And Space taken is same for both the solution.

# Solution 1:
'''
Topics: Array, Recursion, Backtracking

Time Complexity: O(N^((T/M)+1))

Call Stack Space: O(T/M)
Auxiliary Sapce: O(T/M)
Space Complexity: O(T/M)

where T - target
      M - minimum value in candidates.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr,i,n,rem,target,slate,res):
            # base case
            if target==0:
                res.append(list(slate))
                return
            
            # backtracking condition
            if target<0 or i>=n:
                return
            
            # recursive calls
            curr_sum = 0
            for k in range(i,n):
                
                slate.append(arr[k])
                helper(arr,k,n,rem-curr_sum, target-arr[k],slate,res)
                slate.pop()
                curr_sum += arr[k]
            return
        
        
        
        res = []
        helper(sorted(candidates),0,len(candidates),sum(candidates),target,[],res)
        return res


# Solution 2:
'''
Topics: Array, Recursion, Backtracking

Time Complexity: O(N^((T/M)+1))

Call Stack Space: O(T/M)
Auxiliary Sapce: O(T/M)
Space Complexity: O(T/M)

where T - target
      M - minimum value in candidates.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.__helper(candidates, 0, target, [], res)
        return res
    
    def __helper(self, arr, i, target, slate, res):
        # base case
        if target == 0: 
            res.append(list(slate))
            return
        # backtracking condition
        if target<0 or i == len(arr):
            return
        
        # include
        slate.append(arr[i])
        self.__helper(arr,i,target-arr[i],slate,res)
        slate.pop()
        
        # exclude
        self.__helper(arr, i+1, target, slate, res)