# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        val_arr = []
        
        while head:
            val_arr.append(head.val)
            
            head = head.next
        
        return True if val_arr == val_arr[::-1] else False
  
        