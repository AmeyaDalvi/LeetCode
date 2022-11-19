# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = defaultdict(list)
        fringe = [(root, 0)]
        
        if root == None:
            return []
        
        while fringe:
            parent, level = fringe.pop(0)
                 
            if level%2==0:
                ans[level].append(parent.val)

            elif level%2!=0:
                ans[level].insert(0,parent.val)
            
            if parent.left:
                fringe.append((parent.left,level+1))
            if parent.right:
                fringe.append((parent.right,level+1))
        
        return list(ans.values())