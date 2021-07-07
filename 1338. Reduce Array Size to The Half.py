class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        mem = {}
        for val in arr:
            if val not in mem:
                mem[val] = 0
            mem[val]+=1
        
        occur = list(mem.values())
        occur.sort(reverse=True)
        i = 0
        count = 0
        
        while(count<n/2):
            count+=occur[i]
            i+=1
        
        return i
            
        