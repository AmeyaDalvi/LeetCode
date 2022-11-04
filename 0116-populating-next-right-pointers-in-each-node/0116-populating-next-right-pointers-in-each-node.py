"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Use the concept of two pointer curr and nxt
# nxt is used to bring cur back to the right location after curr traverses through 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        curr, leftmost = root, root.left if root else None
        
        while curr and leftmost:
            curr.left.next = curr.right
            
            if curr.next:
                curr.right.next = curr.next.left
            
            curr = curr.next
            
            if not curr:
                curr = leftmost
                leftmost = curr.left
            
            
        return root
        