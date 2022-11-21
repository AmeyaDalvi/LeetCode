# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        fringe = [(root, 1)]
        max_level = 1
        
        while fringe:
            
            parent, level = fringe.pop(0)
            max_level = max(max_level, level)
            if parent.left:
                fringe.append((parent.left, level+1))
            
            if parent.right:
                fringe.append((parent.right, level+1))
        
        return max_level
            