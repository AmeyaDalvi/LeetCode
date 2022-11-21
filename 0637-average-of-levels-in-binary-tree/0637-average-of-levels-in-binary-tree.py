# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        fringe = [(root, 0)]
        node_dict = defaultdict(list)
        output = []
        
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        while fringe:
            
            parent, level = fringe.pop(0)
            
            node_dict[level].append(parent.val)
            
            if parent.left:
                fringe.append((parent.left, level+1))
            if parent.right:
                fringe.append((parent.right, level+1))
        
        for v in node_dict.values():
            output.append(sum(v)/len(v))
        
        return output
            
            