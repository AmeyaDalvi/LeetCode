class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        
        
        # Trick question - Take the max of the digits in the string
        
        ans = max(n)
        
        return 1 if ans == 0 else ans
        