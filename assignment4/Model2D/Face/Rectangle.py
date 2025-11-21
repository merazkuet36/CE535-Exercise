from Model2D.Face.Face import Face  # Absolute import
from Model2D.Line.Line import Line  # Absolute import

class Rectangle(Face):
    def __init__(self, id, lines):
        super().__init__(id, lines)
        if len(lines) != 4:
            raise RuntimeError("A rectangle must have exactly four lines.")
        # Additional checks for parallel sides and perpendicular adjacent sides can be added here

    def __str__(self):
        return f"Rectangle {self.id}: {self.lines}"

    def area(self):
        length = self.lines[0].length()
        width = self.lines[1].length()
        return length * width
