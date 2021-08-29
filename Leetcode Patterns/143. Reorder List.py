# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        mid, fast = head, head
        while fast and fast.next:
            mid, fast = mid.next, fast.next.next
        
        # reverse the linked list
        curr = mid.next
        mid.next = None
        revr = None
        while curr:
            temp = curr.next
            curr.next = revr
            revr = curr
            curr = temp
        
        # join two linked list
        curr = head
        while revr:
            temp = curr.next
            temp2 = revr.next
            curr.next = revr
            revr.next = temp
            curr = temp
            revr = temp2
        
            