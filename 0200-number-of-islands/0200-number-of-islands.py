
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def isValid(i, j):
            if (i >= 0 and i < rows) and (j >= 0 and j < cols):
                return True
            return False
        
        def bfs(r, c):
            fringe = collections.deque()
            visited.add((r,c))
            fringe.append((r,c))
            
            while fringe:
                row, col = fringe.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        fringe.append((r, c))
                        visited.add((r, c))
                
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count+=1
        
        
        return count
        
        

#dfs solution, karan's method, change 1's to 0's. Use a isValid function verify if node is in bounds. For loops to increment island counts and initiating dfs 
#         rows, cols = len(grid), len(grid[0])
        
#         def isValid(i, j):
#             if (i >= 0 and i < rows) and (j >= 0 and j < cols):
#                 return True
#             return False
        
#         def dfs(i, j):
#             if not isValid(i, j) or grid[i][j] == '0':
#                 return 
            
#             grid[i][j] = '0'

#             dfs(i, j-1)
#             dfs(i-1, j)
#             dfs(i, j+1)
#             dfs(i+1, j)
            
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == '1':
#                     count += 1
#                     dfs(i, j)
        
        
                
                
        # return count
        