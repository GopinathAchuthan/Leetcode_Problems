# Method 1:
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0]*length
        ans[0] = 1
        
        for i in range(1,length):
            ans[i] = nums[i-1]*ans[i-1]
        
        right = 1
        for i in range(length-1,-1,-1):
            ans[i] = ans[i]*right
            right*=nums[i]
        
        return ans
        
        
        
# Method 2: By keeping track of number of zeros in the nums array
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