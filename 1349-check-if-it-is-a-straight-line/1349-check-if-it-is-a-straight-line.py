class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1- x0, y1 - y0
        
        return all(dx * (y - y0) == dy * (x - x0) for x, y in coordinates[1:])