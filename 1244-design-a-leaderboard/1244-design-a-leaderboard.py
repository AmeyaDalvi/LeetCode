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
        

    
# Solution using heap, heapify and numpy
# from heapq import *
# import numpy as np

# class Leaderboard:

#     def __init__(self):
#         self.leaderboard = {}
        

#     def addScore(self, playerId: int, score: int) -> None:
#         if playerId not in self.leaderboard:
#             self.leaderboard[playerId] = score
#         else:
#             self.leaderboard[playerId] += score
    
            
#     def top(self, K: int) -> int:
#         heap = list(-1*np.array(list(self.leaderboard.values())))
#         heapq.heapify(heap)
        
#         answer  = [-1*heapq.heappop(heap) for i in range(0,K) ]
        
#         return sum(answer)

#     def reset(self, playerId: int) -> None:
#         del self.leaderboard[playerId]


class Player:
    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score
    
    def updateScore(self, score: int)-> None:
        self.score += score

class Leaderboard:
    def __init__(self):
        self.leaderboard = {}
    
    def addScore(self, playerId: int, score: int) -> None:
        player = Player(playerId, score)
        
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = player
        else:
            print(self.leaderboard[playerId].score)
            self.leaderboard[playerId].updateScore(score)
            print(self.leaderboard[playerId].score)
    
    def top(self, K: int) -> int:
        heap = []
        score_sum = 0
        for k,v in self.leaderboard.items():
            heap.append(-1*v.score)
        heapq.heapify(heap)
        
        for i in range(K):
            score_sum += -1*heappop(heap)
        
        return score_sum
        
    
    def reset(self, playerId: int) -> None:
        del self.leaderboard[playerId]
        
        
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)