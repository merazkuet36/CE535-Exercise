class GMRES:
    def __init__(self, restart: int = 50, tolerance: float = 1e-5, max_iterations: int = 100):
        self.restart = restart
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def __str__(self):
        return f'GMRES Method with restart {self.restart}, tolerance {self.tolerance}, and max iterations {self.max_iterations}'
