# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        op = []
        self.partial_op = ''
        
        def dfs(node): 
            if node == None:
                return
            char_len = len(str(node.val) + '->')
            self.partial_op = self.partial_op + str(node.val) + '->'
            
            if node.left == None and node.right == None:
                op.append(self.partial_op[:-2])
                self.partial_op = self.partial_op[:-char_len]
                return

            dfs(node.left)               
            dfs(node.right)
            self.partial_op = self.partial_op[:-char_len]

        dfs(root)
        return op
        