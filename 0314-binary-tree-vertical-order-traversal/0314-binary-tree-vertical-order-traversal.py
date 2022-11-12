# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        curr = root
        
        if not root:
            return []
        
        fringe = [(curr, 0)]
        
        level_dict = defaultdict(list)
        level_dict[0].append(curr.val)
        
        while fringe:
            parent, level = fringe.pop(0)
            
            if parent.left:
                fringe.append((parent.left, level-1))
                level_dict[level-1].append(parent.left.val)
                
            if parent.right:
                fringe.append((parent.right, level+1))
                level_dict[level+1].append(parent.right.val)
            

        key_list = sorted(list(level_dict.keys()))
        
        op = []
        
        for key in key_list:
            op.append(level_dict[key])
        
        return op
            
            
            
            
            
        
        
        