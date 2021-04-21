# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x<bottomLeft.x or topRight.y<bottomLeft.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        ax, ay = bottomLeft.x, bottomLeft.y
        bx, by = topRight.x, topRight.y
        mx, my = (ax+bx)//2, (ay+by)//2
        
        count = 0
        count += self.countShips(sea, Point(mx,my), Point(ax,ay))
        count += self.countShips(sea, Point(bx,my), Point(mx+1,ay))
        count += self.countShips(sea, Point(mx,by), Point(ax,my+1))
        count += self.countShips(sea, Point(bx,by), Point(mx+1,my+1))
        
        return count