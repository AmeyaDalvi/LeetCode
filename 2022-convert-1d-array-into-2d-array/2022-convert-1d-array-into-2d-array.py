class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        twoD = []
        if m*n == len(original):
            for i in range(0, m*n, n):
                twoD.append(original[i:i+n])
                
        return twoD