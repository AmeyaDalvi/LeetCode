
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        count = 0

#dfs solution, karan's method, change 1's to 0's. Use a isValid function verify if node is in bounds. For loops to increment island counts and initiating dfs 
        rows, cols = len(grid), len(grid[0])
        
        def isValid(i, j):
            if (i >= 0 and i < rows) and (j >= 0 and j < cols):
                return True
            return False
        
        def dfs(i, j):
            if not isValid(i, j) or grid[i][j] == '0':
                return 
            
            grid[i][j] = '0'

            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                
                
        return count
        