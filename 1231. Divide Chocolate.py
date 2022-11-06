'''
Time Complexity: O(n log (S/(k+1)))
Space Complexity: O(1)

Topics: Array, Binary Search, Dynamic Programming
'''
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left, right = min(sweetness), sum(sweetness)//(k+1)
        while left<=right:
            mid = left+(right-left)//2
            val = self.__getPossibleKValue(sweetness,mid)
            if val>=k+1:
                left = mid+1
            else:
                right = mid-1
        return right
    
    def __getPossibleKValue(self,nums,level):
        ans = 0
        temp = 0
        for num in nums:
            temp+=num
            if temp>=level:
                ans+=1
                temp=0
        return ans
        