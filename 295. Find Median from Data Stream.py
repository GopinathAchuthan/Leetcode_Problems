class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        i = bisect.bisect(self.nums, num)
        if i>=len(self.nums):
            self.nums.append(num)
        else:
            self.nums.insert(i,num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length%2:
            return self.nums[(length-1)//2]
        else:
            return (self.nums[(length-1)//2]+self.nums[length//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()