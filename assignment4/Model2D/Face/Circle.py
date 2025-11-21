from Face import Face
from Line import Line
from Point import Point

class Circle(Face):
    def __init__(self, id, lines):
        super().__init__(id, lines)
        if len(lines) != 1:
            raise RuntimeError("A circle must have exactly one line.")
        self.center = Point(id + 1, lines[0].points[0].x, lines[0].points[0].y)
        self.radius = lines[0].length()

    def __str__(self):
        return f"Circle {self.id}: Center = {self.center}, Radius = {self.radius}"

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * self.radius ** 2
