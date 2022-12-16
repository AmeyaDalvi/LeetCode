class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        len_s = len(s)
        # a = s[0:len(s)//2]
        # b = s[(len(s)//2):len(s)]
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        max_c = 0
        count = 0
        
        for i in range(0,len_s):
            if i == (len_s//2):
                max_c = count
                count = 0
                
            if s[i] in vowels:
                count+=1
        
        return count == max_c