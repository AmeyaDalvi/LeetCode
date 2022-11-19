# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        fringe = [(root, 0)]
        
        ans = defaultdict(list)
        
        while fringe:
            parent, level = fringe.pop(0)
            
            ans[level].append(parent.val)
            
            if parent.left:
                fringe.append((parent.left, level+1))
            if parent.right:
                fringe.append((parent.right, level+1))
        
        result = []
        for i in list(ans.keys()):
            result.append(ans[i])
        
        return result
            
        