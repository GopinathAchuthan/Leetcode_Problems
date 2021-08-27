# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        flag = True
        # check whether loop is present
        while(fast and fast.next):
            slow,fast = slow.next, fast.next.next
            if slow==fast:
                flag = False
                break
        if flag:
            return None
        # find entry to the loop
        slow = head
        while(slow!=fast):
            slow, fast = slow.next, fast.next
        return slow
        
        