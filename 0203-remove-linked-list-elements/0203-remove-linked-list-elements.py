# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        sentinel = ListNode(0)
        sentinel.next = head
        
        if head == None:
            return head
        
        prev = sentinel
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            
            else:
                prev = curr
            curr = curr.next
                
        
        return sentinel.next
            
                
        
        