from Model2D.Line.Line import Line  # Absolute import

class Face:
    def __init__(self, id, lines):
        if not isinstance(id, int):
            raise RuntimeError("id must be an integer.")
        if not isinstance(lines, list):
            raise RuntimeError("lines must be a list.")
        self.id = id
        self.lines = lines
        for line in lines:
            if not isinstance(line, Line):
                raise RuntimeError("Each item in lines must be a Line object.")

    def __str__(self):
        return f"Face {self.id}"

    def perimeter(self):
        return sum(line.length() for line in self.lines)

    def area(self):
        return 0.0  # Area needs to be overridden in subclasses
