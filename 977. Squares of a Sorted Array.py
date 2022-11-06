'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Two pointers
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        left, right = 0, len(nums)-1
        k = right
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                ans[k] = nums[left]*nums[left]
                left+=1
            else:
                ans[k] = nums[right]*nums[right]
                right-=1
            k-=1
        
        return ans