class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        
        s = s.rstrip(' ')
        
        s = s[::-1]
        
        for c in s:
            if c == ' ':
                break
            count+=1
        
        return count
        
            
        
        