import numpy as np
from scipy.linalg import eig

class EigenvalueAnalysis:
    def __init__(self, A: np.ndarray, B: np.ndarray = None):
        # Step 1: Check if A is a square numpy matrix
        if not isinstance(A, np.ndarray) or A.shape[0] != A.shape[1]:
            raise RuntimeError("Matrix A must be square.")
        
        self.A = A
        
        # Step 2: If B is provided, check if B is a square numpy matrix and same size as A
        if B is not None:
            if not isinstance(B, np.ndarray) or B.shape[0] != B.shape[1] or B.shape != A.shape:
                raise RuntimeError("Matrix B must be square and have the same size as A.")
            self.B = B
            # Perform generalized eigenvalue analysis
            self.lam, self.x = eig(A, B)
        else:
            self.B = None
            # Perform standard eigenvalue analysis
            self.lam, self.x = np.linalg.eig(A)

    def check(self, lam_i, x_i: np.ndarray) -> bool:
        # Step 3: Ensure lam_i is a valid float
        if isinstance(lam_i, np.ndarray):
            lam_i = lam_i.item()  # Convert numpy scalar to native Python float
        
        if not isinstance(lam_i, float):
            raise RuntimeError("Eigenvalue lam_i must be a float.")
        
        # Step 4: Ensure x_i is a numpy vector with the same size as A
        if not isinstance(x_i, np.ndarray) or x_i.ndim != 1 or x_i.shape[0] != self.A.shape[0]:
            raise RuntimeError("Eigenvector x_i must be a numpy vector with the same size as A.")
        
        # Step 5: Compute the residual for standard or generalized eigenvalue problems
        if self.B is not None:
            # Generalized Eigenvalue Problem: A * x_i = lam_i * B * x_i
            residual = np.dot(self.A, x_i) - lam_i * np.dot(self.B, x_i)
        else:
            # Standard Eigenvalue Problem: A * x_i = lam_i * x_i
            residual = np.dot(self.A, x_i) - lam_i * x_i
        
        # Step 6: Compute the norm of the residual
        norm = np.linalg.norm(residual)
        
        # Step 7: Use tolerance to check if the equality is satisfied
        tol = 1e-10
        return norm < tol