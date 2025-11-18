class Euler:
    def __init__(self, a: float = 0.0, b: float = 1.0, n: int = 10):
        self.a = a
        self.b = b
        self.n = n

    def __str__(self):
        return f'Euler Method with {self.n} steps from {self.a} to {self.b}'
