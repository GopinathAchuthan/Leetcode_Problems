# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_value = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked_value == 0:
            self.peeked_value = self.iterator.next()
        return self.peeked_value
        

    def next(self):
        """
        :rtype: int
        """
        if self.peeked_value == 0:
            return self.iterator.next()
        else:
            temp = self.peeked_value
            self.peeked_value = 0
            return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked_value != 0:
            return True
        else:
            self.peeked_value = self.iterator.next()
            if self.peeked_value<=0:
                return False
            else:
                return True

        
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].