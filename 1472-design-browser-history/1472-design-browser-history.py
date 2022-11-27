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
        
        possible = min(len(self.backward), steps)
        
        while possible:
            self.fwd.append(self.current)
            self.current = self.backward.pop()
            possible -= 1
        
        return self.current

    def forward(self, steps: int) -> str:
        
        possible = min(len(self.fwd), steps)
        
        while possible:
            self.backward.append(self.current)
            self.current = self.fwd.pop()
            possible -=1
        
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)