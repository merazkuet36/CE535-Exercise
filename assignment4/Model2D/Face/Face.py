from ..Line import Line

class Face:
    def __init__(self, id: int, lines: list[Line]):
        try:
            self.id = int(id)
        except Exception as e:
            raise RuntimeError('id must be an integer')
        
        if not isinstance(lines, list):
            raise RuntimeError('lines must be a list')
        
        for line in lines:
            if not isinstance(line, Line):
                raise RuntimeError('each item in the lines list must be a Line object')
        
        self.lines = lines

    def __str__(self):
        return f"Face(id={self.id}, lines={self.lines})"

    def perimeter(self):
        return sum(line.length() for line in self.lines)

    def area(self):
        return 0.0  # Default implementation for Face
