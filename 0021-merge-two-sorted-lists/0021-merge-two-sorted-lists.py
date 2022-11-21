# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(-1)
        prehead = prev
        
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prehead.next = curr1
                curr1 = curr1.next
            else:
                prehead.next = curr2
                curr2 = curr2.next
            
            prehead = prehead.next
        
        prehead.next = curr1 if curr2 is None else curr2
        
        return prev.next