# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while(head and head.val == val):
            head = head.next
        
        if not head:
            return head
        
        prev = head
        curr = head.next
        
        while(curr):
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev,curr = curr, curr.next
                    
        
        return head