class Solution:
    def maxDepth(self, s: str) -> int:
        opeen = 0
        close = 0
        max_count = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                opeen+=1
            if s[i] == ')':
                if max_count < opeen:
                    max_count = opeen
                close+=1
                opeen-=1
            if opeen == 0:
                close = 0
        
        return max_count
                    
            
                    
        