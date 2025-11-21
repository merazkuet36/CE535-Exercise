from Model2D.Face.Face import Face  # Absolute import
from Model2D.Line.Line import Line  # Absolute import

class Triangle(Face):
    def __init__(self, id, lines):
        super().__init__(id, lines)
        if len(lines) != 3:
            raise RuntimeError("A triangle must have exactly three lines.")

    def __str__(self):
        return f"Triangle {self.id}: {self.lines}"

    def area(self):
        # Use Heron's formula to calculate the area of the triangle
        a = self.lines[0].length()
        b = self.lines[1].length()
        c = self.lines[2].length()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
