class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = defaultdict(lambda: 0)
        double = 0
        miss = 0
        for val in nums:
            hash[val] += 1
            
        for i in range(1,len(nums)+1):
            if hash[i] == 0:
                miss = i
            if hash[i] == 2:
                double = i
                
            if double != 0 and miss !=0:
                break
        
        return [double, miss]