class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0, 1]
        
        size = 2
        
        while size < n+1:
            temp = [curr + 1 for curr in ans]
            ans.extend(temp)
            size *= 2
        
        return ans[:n+1]
        