# Solution 1 - with usage of list 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        array = []
        for i in lists:
            while i:
                array.append(i.val)
                i = i.next
        
        out = temp = ListNode()
        if array:
            array.sort()
            for val in array:
                temp.next = ListNode(val)
                temp = temp.next
        
        return out.next

# Solution 2 - without usage of list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        out = ListNode()
        temp = out
        isEmpty = False
        while(True):
            isEmpty = True
            min_idx = 0
            min_val = float('inf')
            for idx in range(len(lists)):
                if lists[idx] and lists[idx].val < min_val:
                    isEmpty = False
                    min_idx = idx
                    min_val = lists[idx].val
            if isEmpty:
                break   
            lists[min_idx] = lists[min_idx].next
            temp.next = ListNode(min_val)
            temp = temp.next
        
        return out.next