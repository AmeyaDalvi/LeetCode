class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeros_row = set()
        zeros_col = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_row.add(i)
                    zeros_col.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zeros_row or j in zeros_col:
                    matrix[i][j] = 0
        
         