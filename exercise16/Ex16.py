import numpy as np
import scipy.linalg

class TriDiagonal:
    def __init__(self, n):
        # Initialize a tri-diagonal matrix of size n
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer")
        
        self.n = n
        # Create a zero matrix
        self.A = np.zeros((n, n))
        
        # Fill the main diagonal with 2
        np.fill_diagonal(self.A, 2)
        
        # Fill the subdiagonal and superdiagonal with 1
        for i in range(1, n):
            self.A[i, i-1] = 1
            self.A[i-1, i] = 1
        
        # Store the LU decomposition of A
        self.LU = scipy.linalg.lu_factor(self.A)
        
    def rank(self):
        # The rank of a tri-diagonal matrix is its dimension (n)
        return self.n
    
    def solve(self, b):
        if len(b) != self.n:
            raise ValueError("Right-hand side vector b must have the same size as the system matrix A")
        
        # Use LU decomposition to solve the system
        return scipy.linalg.lu_solve(self.LU, b)
    
    def check(self, b, x):
        if len(b) != self.n or len(x) != self.n:
            raise ValueError("b and x must have the same size as the system matrix A")
        
        # Compute the residual
        residual = np.linalg.norm(np.dot(self.A, x) - b)
        
        # Use a tolerance to check if the residual is small enough
        tol = 1e-8
        return residual < tol
