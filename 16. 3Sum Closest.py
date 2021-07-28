class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        abs_diff = float('inf')
        ans = 0
        for i in range(N-2):
            left = i+1
            right = N-1
            while(left<right):
                val = nums[i]+nums[left]+nums[right]
                if val>target:
                    right-=1
                    if abs_diff>val-target:
                        abs_diff = val-target
                        ans = val
                elif val<target:
                    left+=1
                    if abs_diff>target-val:
                        abs_diff = target-val
                        ans = val
                else:
                    return val
        return ans