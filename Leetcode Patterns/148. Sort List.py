# Time Complexity: O(N log N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # find middle node in linked list
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        # call sortList function
        first, second, prev.next = head, slow, None
        first = self.sortList(first)
        second = self.sortList(second)
        
        # merge two sorted list
        res = ListNode()
        node = res
        while first and second:
            if first.val<=second.val:
                node.next = first               
                first, node = first.next, node.next
            else:
                node.next = second                
                second, node =second.next, node.next
        
        node.next = first if first else second
        
        return res.next