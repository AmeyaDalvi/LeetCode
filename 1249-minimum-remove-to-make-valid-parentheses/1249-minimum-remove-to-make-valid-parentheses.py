class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        indexes_to_remove = set()
        
        stack = []
        answer = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif not stack and char == ')':
                indexes_to_remove.add(i)
            elif char == ')':
                stack.pop()
            
        indexes_to_remove = indexes_to_remove.union(set(stack))
        
        for i, char in enumerate(s):
            if i in indexes_to_remove:
                continue
            else:
                answer.append(char)
        
        return "".join(answer)
            
                
        