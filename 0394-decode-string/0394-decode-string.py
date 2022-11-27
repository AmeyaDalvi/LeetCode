# Use stack and a currString and currNum variables that you update till you encounter a [

class Solution:
    def decodeString(self, s):
        stack = []
        currString = ''
        currNum = 0
        
        for c in s:
            if c == '[':
                stack.append(currString)
                stack.append(currNum)
                currNum = 0
                currString = ''
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num*currString
                
            elif c.isdigit():
                currNum = currNum*10 + int(c)
            else:
                currString += c
        
        return currString
                
                
                
                