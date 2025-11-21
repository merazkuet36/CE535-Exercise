from .Face import Face
from ..Line import Line

class Circle(Face):
    def __init__(self, id: int, lines: list[Line]):
        super().__init__(id, lines)
        
        if len(lines) != 1:
            raise RuntimeError('Circle must have exactly 1 line')
        
        self.radius = lines[0].length() / 2  # Correctly calculate radius
        self.center = lines[0].points[0]  # Set the first point as the center

    def __str__(self):
        return f"Circle(id={self.id}, radius={self.radius}, center={self.center})"

    def perimeter(self):
        return 2 * 3.14159 * self.radius  # Correct perimeter calculation

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Correct area calculation
