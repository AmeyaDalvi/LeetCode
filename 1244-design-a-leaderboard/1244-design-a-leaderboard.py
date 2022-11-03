class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
        else:
            self.leaderboard[playerId] += score
        
        print("Leaderboard",self.leaderboard)
            
    def top(self, K: int) -> int:
        print("Sorted scores", sorted(list(self.leaderboard.values()), reverse=True))
        topK = sorted(list(self.leaderboard.values()), reverse=True)
        answer  = 0 
        for i in range(0, K):
            answer+= topK[i]
        
        return answer

    def reset(self, playerId: int) -> None:
        # self.leaderboard[playerId] = 0
        del self.leaderboard[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)