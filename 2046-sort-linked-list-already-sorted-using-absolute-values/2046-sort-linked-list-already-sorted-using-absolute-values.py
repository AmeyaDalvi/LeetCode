# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = neg = head
        curr = head.next

        while curr:
            if curr.val < 0:
                prev.next = curr.next 
                curr.next = neg
                neg = curr
                curr = prev.next
            else: 
                prev, curr = curr, curr.next

        return neg
            
        