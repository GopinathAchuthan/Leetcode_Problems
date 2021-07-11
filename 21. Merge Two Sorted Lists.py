# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3 = ListNode()
        curr = l3
        while(l1 and l2):
            if l1.val<=l2.val:
                curr.next = ListNode(l1.val)
                curr, l1 = curr.next, l1.next
            else:
                curr.next = ListNode(l2.val)
                curr, l2 = curr.next, l2.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return l3.next