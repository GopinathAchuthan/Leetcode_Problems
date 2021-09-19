# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        state = []
        state.append(head.val%2)
        state.append((head.val+1)%2)
        
        first = head
        while first.next and state[first.val%2]==state[first.next.val%2]:
                first = first.next
                
        if not first.next:
            return head
        
        prev,second = first,first.next
        
        while second:
            if state[first.val%2]==state[second.val%2]:
                prev.next = second.next
                second.next = first.next
                first.next = second
                first = first.next
                second = prev.next
            else:
                prev,second =second, second.next
        
        return head
        