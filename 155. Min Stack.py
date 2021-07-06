class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        heapq.heapify(self.stack)
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return heapq.nsmallest(1,self.stack)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()