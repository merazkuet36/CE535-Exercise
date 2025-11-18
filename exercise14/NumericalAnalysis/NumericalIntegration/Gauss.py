class Gauss:
    def __init__(self, a: float = 1.0, b: float = 2.0, n: int = 2):
        self.a = a
        self.b = b
        self.n = n

    def __str__(self):
        return f'Gauss Quadrature with {self.n} intervals from {self.a} to {self.b}'
