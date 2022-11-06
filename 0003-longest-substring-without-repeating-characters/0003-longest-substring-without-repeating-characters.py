class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s = 0
        st = ""
        d = {}
        j = 0
        for i in range(len(s)):       
            if s[i] in d:
                j = max(d[s[i]],j)
            max_s = max(max_s,i-j+1)
            d[s[i]]=i+1
        return max_s
            
                