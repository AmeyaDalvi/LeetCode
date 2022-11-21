# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
        
#         slow = head
#         fast = head
        
#         if head == None or head.next == None:
#             return False
        
#         while fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if fast == None:
#                 break
#             if slow == fast:
#                 return True
#         return False
            