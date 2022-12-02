# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start = 1
        end = n
        
        ans = None
        
        while start <= end:
            mid = start + (end - start)//2
            
            if isBadVersion(mid):
                ans = mid
                end = mid-1
            else:
                start = mid + 1
        
        return ans
            
                
       