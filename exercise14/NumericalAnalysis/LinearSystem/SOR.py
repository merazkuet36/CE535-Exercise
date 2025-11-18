class SOR:
    def __init__(self, omega: float = 1.25, tolerance: float = 1e-5, max_iterations: int = 100):
        self.omega = omega
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def __str__(self):
        return f'SOR Method with omega {self.omega}, tolerance {self.tolerance}, and max iterations {self.max_iterations}'
