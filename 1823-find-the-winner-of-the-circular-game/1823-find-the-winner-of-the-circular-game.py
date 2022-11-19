class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        
        while len(friends)>1:
            l = (k-1)%len(friends)
            friends.pop(l)
            friends = friends[l:] + friends[:l]
        
        return friends[0]
            