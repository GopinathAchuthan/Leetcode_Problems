# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        
        slow = fast = head
        track = None
        
        while(fast and fast.next):
            fast = fast.next.next
            slow,track,track.next = slow.next,slow,track
            
        if fast:
            slow = slow.next
        
        while(track and slow):
            if track.val != slow.val:
                return False
            track,slow = track.next, slow.next
        return True