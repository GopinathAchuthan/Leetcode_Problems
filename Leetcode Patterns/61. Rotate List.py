# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if k==0 or not head:
            return head
        
        # get length of linked list
        curr = head
        length = 0
        while curr:
            curr, length = curr.next, length+1
        
        # limit the value of k within length of linked list
        k = k%length
        if k==0:
            return head
        
        # finding the dividing point in the linked list
        dummy = ListNode(0,head)
        first = dummy
        for _ in range(k):
            first = first.next
        ep,prev,ans = None,None, dummy
        while first:
            ep,first,prev, ans = first, first.next, ans, ans.next
        
        # join two linked list
        prev.next = None
        ep.next = head
        
        return ans
        
        
        