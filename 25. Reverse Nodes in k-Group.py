# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k==1:
            return head
        ret_head = None
        node = head
        ret_tail = None
        while(node):
            temp = node
            rev = None
            rev_tail = None
            i = 0
            while(node and i<k):
                i+=1
                node=node.next
            if i==k:
                i = 0
                node = temp
                while(node and i<k):
                    i+=1
                    rev,rev.next,node = node, rev, node.next
                    if rev.next == None:
                        rev_tail = rev
                if ret_head == None:
                    ret_head = rev
                    ret_tail = rev_tail
                else:
                    ret_tail.next = rev
                    ret_tail = rev_tail
            else:
                if not ret_head:
                    return head
                else:
                    ret_tail.next = temp
                    break
            
        return ret_head