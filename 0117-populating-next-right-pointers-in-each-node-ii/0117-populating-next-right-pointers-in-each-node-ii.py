"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        fringe = []
        fringe.append((root, 0))
        
        while fringe:
            parent, level = fringe.pop(0)
            
            if parent != None:
                if fringe:
                    if level == fringe[0][1]:
                        parent.next = fringe[0][0]
                if parent.left != None:
                    fringe.append((parent.left, level+1))
                if parent.right != None:
                    fringe.append((parent.right, level+1))
                    
        return root