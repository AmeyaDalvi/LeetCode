class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.current = homepage
        
        self.fwd = []
        self.backward = []
        

    def visit(self, url: str) -> None:
        self.fwd = []
        
        self.backward.append(self.current)
        self.current = url
        
        
    def back(self, steps: int) -> str:
        
        if len(self.backward) == 0:
            return self.current
        
        if steps >= len(self.backward):
            self.fwd.append(self.current)
            self.fwd += self.backward[::-1]
            self.current = self.fwd.pop()
            self.backward = []
        else:
            while steps > 0:
                self.fwd.append(self.current)
                self.current = self.backward.pop()
                steps -= 1
        
        return self.current

    def forward(self, steps: int) -> str:
        
        if len(self.fwd) == 0:
            return self.current
        
        if steps >= len(self.fwd):
            self.backward.append(self.current)
            self.backward += self.fwd[::-1]
            # print(self.backward) 
            self.current = self.backward.pop()
            self.fwd = []
        else:
            while steps > 0:
                self.backward.append(self.current)
                self.current = self.fwd.pop()
                steps -= 1
        
        return self.current
            
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)