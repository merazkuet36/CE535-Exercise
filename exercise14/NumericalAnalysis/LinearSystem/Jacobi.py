class Jacobi:
    def __init__(self, tolerance: float = 1e-5, max_iterations: int = 100):
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def __str__(self):
        return f'Jacobi Method with tolerance {self.tolerance} and max iterations {self.max_iterations}'
