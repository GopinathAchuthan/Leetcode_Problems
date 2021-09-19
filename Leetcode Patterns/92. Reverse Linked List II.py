# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        endPoint,first,second = None,head,head
        for _ in range(left-1):
            endPoint,first,second = first, first.next, second.next
        for _ in range(right-left):
            second = second.next
        nextPoint, second.next = second.next, None
        
        revr = None
        endPoint2 = first
        while first:
            revr, first.next, first = first, revr, first.next
        
        endPoint2.next = nextPoint
        if endPoint:
            endPoint.next  = revr 
            return head
        else:
            return revr
        
        