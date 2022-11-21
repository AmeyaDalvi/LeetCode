# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        fringe, min_depth = [(1, root)], float('inf')
            
        while fringe:
            depth, parent = fringe.pop()
            
            if not parent.left and not parent.right:
                min_depth = min(depth, min_depth)
            
            if parent.left:
                fringe.append((depth+1, parent.left))
            if parent.right:
                fringe.append((depth+1, parent.right))
        
        return min_depth