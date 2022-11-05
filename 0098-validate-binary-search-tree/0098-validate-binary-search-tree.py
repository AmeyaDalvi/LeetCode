# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValid(self, curr, lt, gt):
        flag_left = True
        flag_right = True
        
        for x in lt:
            flag_left = curr.val < x
        
        for y in gt:
            flag_right = curr.val > y
    
        return flag_left and flag_right
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        fringe = [(root, [], [])]
        
        while fringe:
            parent, lt, gt = fringe.pop()
            print("parent==>", parent.val)
            print("left ==>", parent.left.val if parent.left else None)
            print("right ==>", parent.right.val if parent.right else None)
            print("")
            
            if parent.left:
                if parent.left.val >= parent.val:
                    return False
                flag_isValid = self.isValid(parent.left, lt, gt)
                
                if flag_isValid: 
                    fringe.append((parent.left, lt + [parent.val], gt))
                    
                else:
                    return False
            
            if parent.right:
                if parent.right.val <= parent.val:
                    return False
                flag_isValid = self.isValid(parent.right, lt, gt)
                
                if flag_isValid: 
                    fringe.append((parent.right, lt, gt + [parent.val]))
                    
                else:
                    return False
        
        return True
            
        
        
        
        
        
        