class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        output = []
        compare = (right+1)*(bottom+1)
        len_count = 0
        
        while True:
            for i in range(left, right+1):
                output.append(matrix[top][i])
                len_count+=1
            top += 1

            if len_count == compare:
                break

            for i in range(top, bottom+1):
                output.append(matrix[i][right])
                len_count+=1
            right -= 1

            if len_count == compare:
                break

            for i in range(right, left-1, -1):
                output.append(matrix[bottom][i])
                len_count+=1
            bottom -= 1

            if len_count == compare:
                break

            for i in range(bottom, top-1, -1):
                output.append(matrix[i][left])
                len_count+=1
            left += 1

            if len_count == compare:
                break

        return output        