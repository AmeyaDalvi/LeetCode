# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

#Divide and conquer, use recursion to divide the rectangle into 4 rectangles

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:  #When we get to the point that has the ship
            return 1
        
        midX = (topRight.x + bottomLeft.x)// 2
        midY = (topRight.y + bottomLeft.y)// 2
        
        midPt = Point(midX, midY)
    
        return self.countShips(sea, midPt, bottomLeft) + self.countShips(sea, topRight, Point(midPt.x+1,midPt.y+1)) +self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) + self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
        