

import math
from Shape import Shape


class Sphere(Shape):

    def __init__(self, radius):

        if radius <= 0:
            raise RuntimeError("Radius must be positive.")
        self.radius = float(radius)

    def __str__(self):

        return f"Sphere(radius={self.radius})"

    def area(self):

        return 4.0 * math.pi * self.radius ** 2

    def perimeter(self):

        raise RuntimeError("Sphere does not have a perimeter.")

    def volume(self):

        return (4.0 / 3.0) * math.pi * self.radius ** 3
