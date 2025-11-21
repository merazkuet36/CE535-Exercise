from .Face import Face
from ..Line import Line

class Triangle(Face):
    def __init__(self, id: int, lines: list[Line]):
        super().__init__(id, lines)
        
        if len(lines) != 3:
            raise RuntimeError('Triangle must have exactly 3 lines')

        if not self._are_lines_connected():
            raise RuntimeError('Lines of the triangle must be connected')

    def __str__(self):
        return f"Triangle(id={self.id}, lines={self.lines})"

    def area(self):
        a, b, c = [line.length() for line in self.lines]
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def _are_lines_connected(self):
        for i in range(3):
            p1 = self.lines[i].points[1]
            p2 = self.lines[(i + 1) % 3].points[0]
            if p1 != p2:
                return False
        return True
