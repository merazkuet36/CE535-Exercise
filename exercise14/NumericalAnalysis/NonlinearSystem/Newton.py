class Newton:
    def __init__(self, initial_guess: float = 1.0, tolerance: float = 1e-5):
        self.initial_guess = initial_guess
        self.tolerance = tolerance

    def __str__(self):
        return f'Newton Method with initial guess {self.initial_guess} and tolerance {self.tolerance}'
