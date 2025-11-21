from .Point import Point

class Line:
    def __init__(self, id: int, points: list[Point]):
        try:
            self.id = int(id)
        except Exception as e:
            raise RuntimeError('id must be an integer')
        if not isinstance(points, list):
            raise RuntimeError('points must be a list')
        for point in points:
            if not isinstance(point, Point):
                raise RuntimeError('each item in the list must be a Point object')
        self.points = points

    def __str__(self):
        return f"Line(id={self.id}, points={self.points})"

    def length(self):
        p1, p2 = self.points
        return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

    def direction(self):
        p1, p2 = self.points
        length = self.length()
        return ((p2.x - p1.x) / length, (p2.y - p1.y) / length)
