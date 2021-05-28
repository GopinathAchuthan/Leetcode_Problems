class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums

    def add(self, val: int) -> int:
        if self.nums == [] or val<self.nums[0]:     # if val is lowest element
            self.nums.insert(0,val)
        elif val> self.nums[-1]:                    # if val is highest element
            self.nums.append(val)
        else:                                       # if val is within the nums
            left = 0
            right = len(self.nums)-1
            while(left<=right):
                mid = left+(right-left)//2
                if self.nums[mid] == val:
                    self.nums.insert(mid,val)
                    break
                elif self.nums[mid]>val:
                    if mid>0 and self.nums[mid-1]<val:
                        self.nums.insert(mid,val)
                        break
                    right = mid-1
                else:
                    if self.nums[mid+1]>val:
                        self.nums.insert(mid+1,val)
                        break
                    left = mid+1
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)