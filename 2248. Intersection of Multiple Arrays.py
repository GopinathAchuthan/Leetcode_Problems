'''
Time Complexity: O(m*n)
Space Complexity: O(n)

Topics: Array, Hashmap
'''
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic = dict()
        for key in nums[0]:
            dic[key] = 1
        
        for i in range(1,len(nums)):
            for j in range(len(nums[i])):
                key = nums[i][j]
                if key in dic and dic[key]==i:
                    dic[key] = i+1
        
        ans = []
        
        for key, val in dic.items():
            if val==len(nums):
                ans.append(key)
        
        return sorted(ans)
                
                    