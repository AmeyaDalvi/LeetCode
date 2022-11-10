class Solution:
    
    # DFS, you got this one, just use partial array to form the semi arrays in each path and append them to final result arr op
    # partial.copy() vv imp
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        op = []
        partial_op = []
        
        def dfs(n):
            
            if n == len(graph)-1: 
                op.append(partial_op.copy())
                return 
            
            for i in graph[n]:
                partial_op.append(i)
                dfs(i)
                partial_op.pop()
                
        
        partial_op.append(0)
        dfs(0)
        
        return op
        