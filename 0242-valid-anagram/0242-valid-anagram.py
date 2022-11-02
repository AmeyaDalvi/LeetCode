class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict= {}
        
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for char in t:
            if char in char_dict:
                char_dict[char] -=1
                
            else:
                return False
        
        for val in char_dict.values():
            if val!=0:
                return False
        
        
        return True
            
        
        