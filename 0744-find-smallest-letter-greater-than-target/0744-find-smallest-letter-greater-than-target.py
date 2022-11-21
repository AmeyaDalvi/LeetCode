class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str: 
        
        lo = 0
        hi = len(letters) - 1
        
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        while lo<= hi:
            mid = lo + (hi - lo)//2
            
            if target >= letters[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return letters[lo]
        
        
#         for letter in letters:
#             if letter > target:
#                 return letter
        
#         return letters[0]


        
            