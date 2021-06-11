# solution 1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        temp = result
        carry = 0
        while(l1 or l2 or carry):
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
                
            carry = val//10
            temp.next = ListNode(val%10)
            temp = temp.next
        
                
        return result.next
        
        


# solution 2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val+l2.val
        result = ListNode(val%10)
        carry = val//10
        l1 = l1.next
        l2 = l2.next
        temp = result
        
        while(l1 and l2):
            val = l1.val+l2.val+carry
            carry = val//10
            temp.next = ListNode(val%10)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        
        while(l1 and carry):
            val = l1.val+carry
            carry = val//10
            temp.next = ListNode(val%10)
            l1 = l1.next
            temp = temp.next
        
        while(l2 and carry):
            val = l2.val+carry
            carry = val//10
            temp.next = ListNode(val%10)
            l2 = l2.next
            temp = temp.next
            
        if carry:
            temp.next = ListNode(carry)
        else:
            if l1:
                temp.next = l1
            if l2:
                temp.next = l2
                
        
        
        return result
        
        