# class Leaderboard:

#     def __init__(self):
#         self.leaderboard = {}
        

#     def addScore(self, playerId: int, score: int) -> None:
#         if playerId not in self.leaderboard:
#             self.leaderboard[playerId] = score
#         else:
#             self.leaderboard[playerId] += score
    
            
#     def top(self, K: int) -> int:
#         topK = sorted(list(self.leaderboard.values()), reverse=True)
#         answer  = 0 
#         for i in range(0, K):
#             answer+= topK[i]
        
#         return answer

#     def reset(self, playerId: int) -> None:
#         del self.leaderboard[playerId]
        

from heapq import *
import numpy as np

class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
        else:
            self.leaderboard[playerId] += score
    
            
    def top(self, K: int) -> int:
        heap = list(-1*np.array(list(self.leaderboard.values())))
        heapq.heapify(heap)
        
        answer  = [-1*heapq.heappop(heap) for i in range(0,K) ]
        
        return sum(answer)

    def reset(self, playerId: int) -> None:
        del self.leaderboard[playerId]
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)