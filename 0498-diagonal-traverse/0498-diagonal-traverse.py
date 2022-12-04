class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        nums = defaultdict(list)
        
        for i in range(0, len(mat)):
            for j in range(len(mat[0])):
                if (i+j)%2 == 1:
                    nums[i+j].append(mat[i][j])
                else:
                    nums[i+j].insert(0,mat[i][j])
        
        ans = []
        
        for lst in list(nums.values()):
            ans.extend(lst)
        
        return ans