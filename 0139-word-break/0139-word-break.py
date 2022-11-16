class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        fringe = [0]
        
        visited = set()
        
        while fringe:
            start = fringe.pop(0)
            
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet:
                    fringe.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        
        return False
        