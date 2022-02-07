'''
Topics: Array, Cycle Sort 

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        
        for i in range(len(nums)):
            while nums[i]!=i+1:
                d = nums[i]
                if nums[d-1]==d:
                    ans.add(d)
                    break
                
                nums[i], nums[d-1] = nums[d-1], nums[i]
            
            
        return ans