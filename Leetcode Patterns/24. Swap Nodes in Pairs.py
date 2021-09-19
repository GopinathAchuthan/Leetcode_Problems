# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,head)
        prev,first,second = dummy,head,head.next
        
        while True:
            temp,prev.next = second.next,second
            second.next, first.next = first, temp
            prev,first = first,temp
            if not first or not first.next:
                break
            else:
                second = first.next
        return dummy.next
        