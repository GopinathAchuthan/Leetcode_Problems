'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Hashmap

'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        table = [0]*101
        for h in heights:
            table[h] += 1
        
        k = 0
        mismatch = 0
        for h in heights:
            while table[k]==0:
                k+=1
            
            if h!=k:
                mismatch += 1
            
            table[k]-=1
        
        return mismatch
            