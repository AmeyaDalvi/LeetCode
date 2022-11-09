class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return "1"
        
        say = self.countAndSay(n-1)
        
        if len(say) == 1:
            return "11"
        
        count = 1
        op = ""
        stack = []
        
        for i in range(1,len(say)):
            if say[i]==say[i-1]:
                count+=1
            else:
                stack.append(str(count))
                stack.append(say[i-1])
                count = 1
        stack.append(str(count))
        stack.append(say[len(say)-1])

        
        return ''.join(stack)
            