class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numOfZeros = 0
        prod = 1
        
        for num in nums:
            if num == 0:
                numOfZeros += 1
                if numOfZeros>1:
                    break
            else:
                prod*=num
            
        
        if numOfZeros:
            if numOfZeros>1:
                return [0 for i in range(len(nums))]
            else:
                return [prod if num==0 else 0 for num in nums]
        else:
            return [prod//num for num in nums]