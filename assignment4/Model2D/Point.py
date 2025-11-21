class Point:
    def __init__(self, id: int, x: float, y: float):
        try:
            self.id = int(id)
        except Exception as e:
            raise RuntimeError('id must be an integer')
        try:
            self.x = float(x)
            self.y = float(y)
        except Exception as e:
            raise RuntimeError('x and y must be convertible to float')

    def __str__(self):
        return f"Point(id={self.id}, x={self.x}, y={self.y})"

    def move(self, dx: float, dy: float):
        try:
            self.x += float(dx)
            self.y += float(dy)
        except Exception as e:
            raise RuntimeError('dx and dy must be convertible to float')
