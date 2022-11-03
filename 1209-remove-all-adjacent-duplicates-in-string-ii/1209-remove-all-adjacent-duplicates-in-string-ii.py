class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        ans = ''
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1]+=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        
        for [x,y] in stack:
            ans += x*y
        
        return ans
                
                
                
                
        