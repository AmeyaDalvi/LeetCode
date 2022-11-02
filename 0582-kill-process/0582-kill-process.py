from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]: 
        
        child_dict = defaultdict(list)
        
        if kill not in ppid:
            return [kill]
        else:
            for i in range(len(ppid)):
                child_dict[ppid[i]].append(pid[i])
        
            fringe = [kill]
            ans = []
            while fringe:
                node = fringe.pop(0)
                ans.append(node)
                fringe.extend(child_dict[node])
            
            return ans
                
                
                