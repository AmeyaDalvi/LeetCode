# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        fringe = [(root, 0)]
        op = []
        # op.append(root.val)
        
        if root == None:
            return []
        
        while fringe:
            parent, level = fringe.pop(0)
            if not fringe:
                op.append(parent.val)
            
            if fringe:
                if level < fringe[0][1]:
                    op.append(parent.val)
             
            if parent.left:
                fringe.append((parent.left, level+1))
            if parent.right:
                fringe.append((parent.right, level+1))
            
            
        return op
                    