# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# use chr to convert number to char ascii and ord to convert char to num ascii
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        all_paths = []
        path = ''
        self.min_len = float('inf')
        
        if root == None:
            return ""
        
        if root.left == None and root.right == None:
            return chr(root.val + 97)
        
        path = path[:-1]
        
        def dfs(node, path):
            if node.left == None and node.right == None:
                path += chr(node.val + 97)
                if len(path) < self.min_len:
                    self.min_len = len(path)
                all_paths.append(path[::-1])

                
            path += chr(node.val + 97)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path = path[:-1]
            
        dfs(root, path)
        ans = sorted(all_paths)
        return ans[0]
        
        
        
        
                
            
        