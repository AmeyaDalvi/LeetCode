# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, node, output):
        if not node:
            return
        

        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        
        self.inorder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        
        return True
        