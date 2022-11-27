# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Use reverse list concept first and then reverse both input lists. Then start adding from end
class Solution:
    
    def reverseList(self,head):
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                
        l1 = self.reverseList(l1)
        cur1 = l1
        l2 = self.reverseList(l2)
        cur2 = l2
        
        ans = ListNode()
        curans = ans
        carry = 0
        while cur1 or cur2 or carry:
            x1 = cur1.val if cur1 else 0
            x2 = cur2.val if cur2 else 0
            
            curans.val = (x1 + x2 + carry)%10
            carry = (x1 + x2 + carry)//10
            
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            
            nxt = ListNode()
            curans.next = nxt
            curans = nxt
            
        
        # if carry:
        #     curans.val+=carry
            
        ans = self.reverseList(ans)
        
        if ans.val == 0:
            return ans.next
        else:
            return ans
            
        
        
            
        