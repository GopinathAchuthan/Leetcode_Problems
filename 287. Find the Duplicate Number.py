# Method 1: Floyd's Tortoise and Hare
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow = nums[0]
        while fast!=slow:
            slow, fast = nums[slow], nums[fast]
        return slow

# Method 2: Set
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = set()
        for num in nums:
            if num in mem:
                return num
            mem.add(num)