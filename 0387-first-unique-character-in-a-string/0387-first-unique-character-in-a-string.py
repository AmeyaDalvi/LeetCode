class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for char in s:
            if char in char_dict and char_dict[char] == 1:
                return s.index(char)
            
        return -1
                
            