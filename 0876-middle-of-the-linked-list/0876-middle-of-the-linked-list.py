# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        nxt = head
        
        if head == None:
            return head
        
        
        while nxt:
            count+=1
            nxt = nxt.next
        
        count = count//2
        
        while head:
            if count == 0:
                return head
            head = head.next
            count -=1