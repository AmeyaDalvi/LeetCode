class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for char in s:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        ans = ''
        for i in range(len(freq)):
            ans = ans + freq[i][0]*freq[i][1]
        
        return ans