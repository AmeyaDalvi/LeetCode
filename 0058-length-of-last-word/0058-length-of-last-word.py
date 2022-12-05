class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ans = ''
        
        s = s.rstrip(' ')
        
        s = s[::-1]
        
        for c in s:
            if c == ' ':
                break
            ans = c + ans
        
        return len(ans)
        
            
        
        