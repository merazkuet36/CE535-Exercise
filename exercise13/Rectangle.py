

from Shape import Shape


class Rectangle(Shape):


    def __init__(self, width, height):

        if width <= 0:
            raise RuntimeError("Width must be positive.")
        if height <= 0:
            raise RuntimeError("Height must be positive.")

        self.width = float(width)
        self.height = float(height)

    def __str__(self):

        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2.0 * (self.width + self.height)

    def volume(self):

        raise RuntimeError("Rectangle does not have a volume.")
