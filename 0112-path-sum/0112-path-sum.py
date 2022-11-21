# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        fringe = [(root, root.val)]
        
        while fringe:
            parent, sum1 = fringe.pop()
            
            if not parent.left and not parent.right:
                if sum1 == targetSum:
                    return True
            
            if parent.left:
                fringe.append((parent.left, parent.left.val + sum1))
            
            if parent.right:
                fringe.append((parent.right, parent.right.val + sum1))
                
        return False
            
            