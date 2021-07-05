class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        n= len(nums)
        while(index<n):
            if nums[index] == val:
                nums[index] = nums[n-1]
                n-=1
            else:
                index+=1
        
        return n