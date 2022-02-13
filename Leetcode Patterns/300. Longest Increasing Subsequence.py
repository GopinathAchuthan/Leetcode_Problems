'''
Topics: Dynamic Programming

Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def search(arr,n,target):
            left,right = 0, n
            while(left<right):
                mid = left+(right-left)//2
                if arr[mid]<target:
                    left = mid+1
                else:
                    right = mid
            return left
        
        seq = []
        ans = 0
        
        for num in nums:
            idx = search(seq,ans,num)
            if idx==ans:
                seq.append(num)
                ans+=1
            else:
                seq[idx] = num
        
        return ans
        