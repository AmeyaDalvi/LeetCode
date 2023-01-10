class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chr_dict = {}
        
        for i in s:
            if i in chr_dict:
                chr_dict[i] += 1
            else:
                chr_dict[i] = 1
        
        for j in t:
            if j in chr_dict:
                chr_dict[j] -=1
            else:
                chr_dict[j] = 1    
            if chr_dict[j] == 0:
                del chr_dict[j]
        
        if len(chr_dict) == 0:
            return True
        else:
            return False
                