# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(next=head)
        p1,p2 = node, node
        for _ in range(n+1):
            p1 = p1.next
        while p1:
            p1,p2 = p1.next, p2.next
        p2.next = p2.next.next
        return node.next